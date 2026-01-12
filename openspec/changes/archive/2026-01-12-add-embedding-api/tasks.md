## 1. Scaffold API Service
- [x] 1.1 Create project structure (e.g., `src/main.py`, `src/models.py`, `src/config.py`).
- [x] 1.2 Add `requirements.txt` or `pyproject.toml` with `fastapi`, `uvicorn`, `fastembed`, `python-dotenv` (or `pydantic-settings`).
- [x] 1.3 Implement configuration loading from `.env`.

## 2. Implement Endpoints
- [x] 2.1 Implement `POST /embed/text` for dense embeddings (using config defaults).
- [x] 2.2 Implement `POST /embed/sparse` for SPLADE embeddings (using config defaults).
- [x] 2.3 Implement global model loading on startup (lifespan manager).

## 3. Containerization
- [x] 3.1 Create `Dockerfile` tailored for the Python application.
- [x] 3.2 Add `.dockerignore`.

## 4. Verification
- [x] 4.1 Write a simple test script (or use `curl`) to verify dense embedding generation.
- [x] 4.2 Write a simple test script to verify sparse embedding generation.
- [x] 4.3 Build and run the Docker container locally to verify functionality.
