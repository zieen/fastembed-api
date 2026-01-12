# Tasks: Add Image Embedding

- [x] Update `requirements.txt` to ensure `fastembed` has image support and include `Pillow` if needed <!-- id: 0 -->
- [x] Implement `ImageEmbedRequest` model (or reuse `EmbedRequest` if suitable) <!-- id: 1 -->
- [x] Implement `get_image_model` factory and caching logic <!-- id: 2 -->
- [x] Implement `/embed/image` endpoint <!-- id: 3 -->
    - [x] Decode Base64 strings to PIL Images
    - [x] Pass to `ImageEmbedding.embed`
    - [x] Return vectors
- [x] Add tests for image embedding <!-- id: 4 -->
- [x] Update `verify_api.py` to test the new endpoint <!-- id: 5 -->
