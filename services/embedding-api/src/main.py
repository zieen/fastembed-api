from contextlib import asynccontextmanager
from typing import Dict, Any
import base64
import io
from PIL import Image
from fastapi import FastAPI, HTTPException
from fastembed import TextEmbedding, SparseTextEmbedding, ImageEmbedding
from .config import settings
from .models import EmbedRequest, DenseEmbeddingResponse, SparseEmbeddingResponse, SparseVector, ImageEmbedRequest

# Global storage for loaded models
# Using a dict to allow caching of different models if we want to expand later
model_cache: Dict[str, Any] = {}

def get_text_model(model_name: str) -> TextEmbedding:
    if model_name not in model_cache:
        model_cache[model_name] = TextEmbedding(model_name=model_name)
    return model_cache[model_name]

def get_sparse_model(model_name: str) -> SparseTextEmbedding:
    if model_name not in model_cache:
        model_cache[model_name] = SparseTextEmbedding(model_name=model_name)
    return model_cache[model_name]

def get_image_model(model_name: str) -> ImageEmbedding:
    if model_name not in model_cache:
        model_cache[model_name] = ImageEmbedding(model_name=model_name)
    return model_cache[model_name]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Preload default models on startup
    print(f"Loading default dense model: {settings.DEFAULT_DENSE_MODEL}")
    get_text_model(settings.DEFAULT_DENSE_MODEL)
    
    print(f"Loading default sparse model: {settings.DEFAULT_SPARSE_MODEL}")
    get_sparse_model(settings.DEFAULT_SPARSE_MODEL)

    print(f"Loading default image model: {settings.DEFAULT_IMAGE_MODEL}")
    get_image_model(settings.DEFAULT_IMAGE_MODEL)
    
    yield
    
    # Cleanup if necessary (fastembed doesn't strictly require explicit teardown)
    model_cache.clear()

app = FastAPI(title="FastEmbed API", lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/embed/text", response_model=DenseEmbeddingResponse)
def embed_text(request: EmbedRequest):
    model_name = request.model_name or settings.DEFAULT_DENSE_MODEL
    try:
        model = get_text_model(model_name)
        # embed returns a generator, convert to list
        embeddings = list(model.embed(request.documents))
        # embeddings is a list of numpy arrays, convert to list of lists
        embeddings_list = [e.tolist() for e in embeddings]
        return DenseEmbeddingResponse(embeddings=embeddings_list)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/embed/sparse", response_model=SparseEmbeddingResponse)
def embed_sparse(request: EmbedRequest):
    model_name = request.model_name or settings.DEFAULT_SPARSE_MODEL
    try:
        model = get_sparse_model(model_name)
        # embed returns a generator of SparseEmbedding objects
        embeddings = list(model.embed(request.documents))
        
        # Convert to response model
        response_vectors = []
        for e in embeddings:
            response_vectors.append(SparseVector(
                indices=e.indices.tolist(),
                values=e.values.tolist()
            ))
            
        return SparseEmbeddingResponse(embeddings=response_vectors)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def decode_image(base64_string: str) -> Image.Image:
    # Remove header if present (e.g., "data:image/jpeg;base64,")
    if "," in base64_string:
        base64_string = base64_string.split(",")[1]
    image_data = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(image_data))

@app.post("/embed/image", response_model=DenseEmbeddingResponse)
def embed_image(request: ImageEmbedRequest):
    model_name = request.model_name or settings.DEFAULT_IMAGE_MODEL
    try:
        model = get_image_model(model_name)
        
        pil_images = [decode_image(img_str) for img_str in request.images]
        
        # embed returns a generator, convert to list
        embeddings = list(model.embed(pil_images))
        # embeddings is a list of numpy arrays, convert to list of lists
        embeddings_list = [e.tolist() for e in embeddings]
        return DenseEmbeddingResponse(embeddings=embeddings_list)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
