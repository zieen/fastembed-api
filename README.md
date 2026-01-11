# FastEmbed Experiments

This repository contains experiments and services using [FastEmbed](https://github.com/qdrant/fastembed), a lightweight, fast, Python library for embedding generation.

## Projects

### 1. Embedding API

A containerized FastAPI service for generating dense and sparse embeddings.

**Directory**: `services/embedding-api`

#### Quick Start (Docker)

```bash
# Build the image (use DOCKER_BUILDKIT=0 if you encounter 403 errors with base image)
DOCKER_BUILDKIT=0 docker build -t fastembed-api:latest services/embedding-api

# Run the container
docker run -d -p 8000:8000 --name fastembed-api fastembed-api:latest

# Check status
curl http://localhost:8000/health
```

#### Local Development

You can run the service locally using the provided helper scripts:

```bash
# Start the service (background)
./services/embedding-api/start.sh

# Stop the service
./services/embedding-api/stop.sh
```

Logs are written to `services/embedding-api/service.log`.

#### Endpoints

-   **POST `/embed/text`**: Generate dense embeddings.
    -   Input: `{"documents": ["text1", "text2"]}`
    -   Output: `{"embeddings": [[0.1, ...], [0.2, ...]]}`
    -   Default Model: `BAAI/bge-small-en-v1.5`
-   **POST `/embed/sparse`**: Generate sparse (SPLADE) embeddings.
    -   Input: `{"documents": ["text1", "text2"]}`
    -   Output: `{"embeddings": [{"indices": [...], "values": [...]}, ...]}`
    -   Default Model: `prithivida/Splade_PP_en_v1`

Configuration is managed via `.env` (see `services/embedding-api/src/config.py`).

### 2. Notebooks

Exploratory notebooks for various embedding tasks:

-   `try_fastembed_text_embeding.ipynb`: Basic dense text embedding.
-   `try_fastembed_sparse_embedding.ipynb`: Sparse embedding (SPLADE) exploration.
-   `try_fastembed_image_embedding.ipynb`: Image embedding experiments.
