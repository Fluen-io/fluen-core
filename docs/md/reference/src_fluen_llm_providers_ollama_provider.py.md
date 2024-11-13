# src/fluen/llm_providers/ollama_provider.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:54:02.187307

## Purpose

The primary purpose of this code is to provide an implementation of a language model provider that interacts with an asynchronous HTTP API to generate text and retrieve embeddings using a specified language model.

## Public API

- `OllamaProvider` (exposure)
- `generate` (exposure)
- `get_embedding` (exposure)

## Dependencies

- `json` (external)
- `aiohttp` (external)
- `typing` (external)
- `BaseLLMProvider` (external)

## Elements

### Class

#### `OllamaProvider`

**Scope:** class-level

**Purpose:** Implements methods to communicate with a remote language model service.

**Documentation:**

This class inherits from BaseLLMProvider and provides methods to generate text and get embeddings by interacting with a remote service through HTTP requests.

### Method

#### `__init__`

**Scope:** OllamaProvider

**Purpose:** Initializes the OllamaProvider instance with configuration settings.

**Documentation:**

Sets up necessary configuration parameters like API base URL, model name, maximum retries, and timeout values for API requests.

#### `generate`

**Scope:** OllamaProvider

**Purpose:** Generates text based on a given prompt.

**Documentation:**

Makes an asynchronous POST request to the /generate API endpoint with the provided prompt and retrieves the generated text.

#### `get_embedding`

**Scope:** OllamaProvider

**Purpose:** Retrieves the embedding for a given text.

**Documentation:**

Makes an asynchronous POST request to the /embeddings API endpoint with the provided text and retrieves the corresponding embedding.

### Variable

#### `api_base_url`

**Scope:** OllamaProvider

**Purpose:** Stores the base URL for API requests.

**Documentation:**

Initialized from the provided configuration, defaults to &#39;http://localhost:11434/api&#39;.

#### `max_retries`

**Scope:** OllamaProvider

**Purpose:** Specifies the maximum number of retries for API requests.

**Documentation:**

Configured through the initialization configuration, defaults to 3 retries.

#### `model`

**Scope:** OllamaProvider

**Purpose:** Defines the model to be used for generating responses and embeddings.

**Documentation:**

Retrieved from the configuration, defaults to &#39;gemma&#39;.

#### `timeout`

**Scope:** OllamaProvider

**Purpose:** Sets the request timeout duration in seconds.

**Documentation:**

Configured through the initialization configuration, defaults to 60 seconds.


[Back to Index](../README.md)