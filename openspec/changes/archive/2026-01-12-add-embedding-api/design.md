## Context
The goal is to expose `fastembed` capabilities via a REST API. This allows decoupling the embedding generation from the main application or enabling usage across multiple services. We need to support both standard dense embeddings (e.g., BGE) and sparse embeddings (SPLADE).

## Decisions

### 1. Framework Selection
- **Decision**: Use **FastAPI**.
- **Rationale**: standard for modern Python APIs, high performance, automatic OpenAPI documentation, and native async support.

### 2. API Structure
- **POST /embed/text**: Accepts a list of strings, returns dense vectors.
- **POST /embed/sparse**: Accepts a list of strings, returns sparse vectors (indices and values).
- **Health Check**: Standard `/health` endpoint.

### 3. Configuration
- **Decision**: Use environment variables (via `.env` file) for configuration.
- **Rationale**: Standard practice for 12-factor apps; allows easy changing of default models without code changes.
- **Variables**:
  - `DEFAULT_DENSE_MODEL`: Default model for dense embeddings.
  - `DEFAULT_SPARSE_MODEL`: Default model for sparse embeddings.

### 4. Containerization
- **Decision**: Use a multi-stage Dockerfile or a slim Python base image.
- **Rationale**: Minimal image size and ease of deployment. Ensure models are either baked in or downloaded on startup/volume mounted (startup download is simpler for now, but caching strategy should be considered).

## Risks / Trade-offs
- **Model Loading**: Models are large. Loading them on every request is impossible, so they must be loaded on startup. This increases startup time and memory usage.
- **Concurrency**: `fastembed` might be CPU bound. simple `async` might not be enough for high throughput without multiple workers (Gunicorn/Uvicorn w/ workers). For this proposal, we start with a simple Uvicorn setup.

## Open Questions
- Should we allow model selection via API parameters?
  - *Proposal*: Yes, allow an optional `model_name` parameter, but default to a sensible standard (e.g., `BAAI/bge-small-en-v1.5` for dense, `prithivida/Splade_PP_en_v1` for sparse).
