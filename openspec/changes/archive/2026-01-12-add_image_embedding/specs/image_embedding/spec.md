## ADDED Requirements

### Requirement: Image Embedding Generation
The system SHALL provide an API endpoint to generate dense vector embeddings from image inputs.

#### Scenario: Generate embeddings for base64 encoded images
- **WHEN** a POST request is made to `/embed/image` with a list of Base64 encoded image strings
- **THEN** the system decodes the images
- **AND** returns a list of float arrays (vectors) corresponding to each input image

#### Scenario: Handle invalid image data
- **WHEN** the input string is not a valid Base64 image
- **THEN** the system returns a 400 Bad Request

### Requirement: Image Model Configuration
The system SHALL support determining the image model via request or default configuration.

#### Scenario: Default Image Model
- **WHEN** no model is specified in the request
- **THEN** the system uses the configured `DEFAULT_IMAGE_MODEL` (e.g., "Qdrant/clip-ViT-B-32-vision")
