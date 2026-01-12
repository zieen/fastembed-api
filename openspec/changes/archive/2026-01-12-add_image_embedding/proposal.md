# Add Image Embedding Support

## Change ID
`add-image-embedding`

## Intent
Enable the API to generate embeddings for images using `fastembed`'s `ImageEmbedding` capabilities. This will allow users to obtain vector representations of images for tasks like visual search and retrieval.

## Summary
This change introduces a new endpoint `/embed/image` that accepts a list of images (files or explicitly defined input format) and returns their dense vector embeddings. It leverages the existing `fastembed` integration and extends the `model_cache` to support image models.

## Dependencies
- `fastembed` (already in `requirements.txt`, need to verify version supports `ImageEmbedding`)
- `Pillow` (likely needed for image processing if not already pulled by `fastembed`)
- `qdrant-fastembed` (implied by usage, but standard `fastembed` package usually covers it)
