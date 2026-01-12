## ADDED Requirements

### Requirement: Dense Embedding Generation
The system SHALL provide an API endpoint to generate dense vector embeddings from text input.

#### Scenario: Generate dense embeddings for valid text
- **WHEN** a POST request is made to `/embed/text` with a list of strings
- **THEN** the system returns a list of float arrays (vectors) corresponding to each input string
- **AND** the vectors have the expected dimension for the default model

#### Scenario: Handle empty input
- **WHEN** the input list is empty
- **THEN** the system returns a 400 Bad Request or an empty list (design choice: empty list)

### Requirement: Sparse (SPLADE) Embedding Generation
The system SHALL provide an API endpoint to generate sparse embeddings (indices and weights) from text input.

#### Scenario: Generate sparse embeddings for valid text
- **WHEN** a POST request is made to `/embed/sparse` with a list of strings
- **THEN** the system returns a list of sparse vector objects (containing indices and values)
- **AND** the weights correspond to the SPLADE model output

### Requirement: Configuration
The system SHALL support configuration via environment variables (loaded from a `.env` file).

#### Scenario: Configure default models
- **WHEN** `DEFAULT_DENSE_MODEL` or `DEFAULT_SPARSE_MODEL` are set in `.env`
- **THEN** the API uses these models by default if no specific model is requested

### Requirement: Containerization
The system MUST include a Dockerfile to build and run the API service.

#### Scenario: Build Docker image
- **WHEN** `docker build` is run with the provided Dockerfile
- **THEN** a valid Docker image is created containing the API and dependencies

#### Scenario: Run container
- **WHEN** the container is started
- **THEN** the API endpoints are accessible on the configured port
