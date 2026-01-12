# Design: Image Embedding Support

## Context
The current API supports text embeddings via `/embed/text` and `/embed/sparse`. We need to add image embedding support. The underlying library `fastembed` supports image embedding via `ImageEmbedding` class, which accepts file paths or PIL Images.

## Architecture
The new functionality will map to a new endpoint `/embed/image` in the existing FastAPI application.

### Input Format
Since the API client and server may not share a filesystem, passing file paths (as in the local python example) is not suitable for a general-purpose API.
**Decision:** Support **Multipart File Uploads** or **Base64 strings**.
- **Multipart:** Standard for binary files. Efficient.
- **Base64:** Easier to nest in a JSON payload alongside other metadata (like model name).
**Proposed approach:** To maintain consistency with `/embed/text` (which takes a JSON body with a list of items), we will support a JSON body containing a list of Base64 encoded image strings.
We can also consider `List[UploadFile]` for `/embed/image` if efficient binary transfer is a priority, but JSON/Base64 is often easier for simple integrations.
*Refinement:* Let's support `multipart/form-data` for `List[UploadFile]` as it's the web standard for uploading multiple files, but `fastembed` processes a batch.
*Wait:* The user example gave paths. If we want to support "paths" that only works if the user is local.
*Better Approach:* Let's stick to the pattern of `EmbedRequest`. If the user really wants to send paths, they can, but the server must be able to resolve them. But for a *web API*, receiving content is safer.
**Selected Design:** JSON payload with `documents` being a list of Base64 strings. This aligns with `EmbedRequest` schema. We will decode these to PIL Images before passing to `model.embed`.

### Model Management
We will extend `model_cache` to store `ImageEmbedding` instances, similar to `TextEmbedding`.
Key lookup: `model_name`.

### Dependencies
Update `requirements.txt` if `fastembed` version needs a bump or if `Pillow` is missing.
