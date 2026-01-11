# Change: Add Embedding API Service

## Why
The project requires a mechanism to generate text embeddings (both dense and sparse/SPLADE) via a network interface. Currently, usage is limited to local notebooks. A containerized API service will allow other systems to consume these embedding capabilities easily.

## What Changes
- Create a new Python-based API service using FastAPI.
- Implement endpoints for:
  - Dense Text Embeddings (using `fastembed.TextEmbedding`).
  - Sparse/SPLADE Embeddings (using `fastembed.SparseTextEmbedding`).
- Add a `Dockerfile` to containerize the application for deployment.
- Create a `.env` file to configure default model names (and potentially other settings).

## Impact
- **New Capability**: `embedding-api`
- **New Code**: A new service directory (likely `app/` or `services/embedding-api/`) containing the FastAPI application.
- **New Infrastructure**: Dockerfile for building the service image.
