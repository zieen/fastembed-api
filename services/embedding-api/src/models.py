from pydantic import BaseModel
from typing import List, Optional

class EmbedRequest(BaseModel):
    documents: List[str]
    model_name: Optional[str] = None

class DenseEmbeddingResponse(BaseModel):
    embeddings: List[List[float]]

class SparseVector(BaseModel):
    indices: List[int]
    values: List[float]

class SparseEmbeddingResponse(BaseModel):
    embeddings: List[SparseVector]
