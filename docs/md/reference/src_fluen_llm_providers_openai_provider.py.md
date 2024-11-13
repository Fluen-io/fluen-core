# src/fluen/llm_providers/openai_provider.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:57:36.051069

## Purpose

The primary purpose of this code is to serve as a provider for interacting with OpenAI&#39;s APIs to generate text and retrieve embeddings using asynchronous operations.

## Public API

- `OpenAIProvider` (exposure)

## Dependencies

- `openai` (external)
- `typing` (external)
- `base_provider` (external)

## Elements

### Class

#### `OpenAIProvider`

**Scope:** global

**Purpose:** Serves as an interface to interact with OpenAI&#39;s API for generating text and retrieving embeddings.

**Documentation:**

The OpenAIProvider class inherits from BaseLLMProvider and provides asynchronous methods to communicate with OpenAI&#39;s services for generating text completions and fetching text embeddings.

### Method

#### `__init__`

**Scope:** OpenAIProvider

**Purpose:** Initializes the OpenAIProvider with configuration for the API client.

**Documentation:**

The constructor method for OpenAIProvider which sets up the AsyncOpenAI client using the provided API key and model from the configuration dictionary.

#### `generate`

**Scope:** OpenAIProvider

**Purpose:** Asynchronously generates a text completion based on the given prompt.

**Documentation:**

The generate method takes a prompt string and uses the OpenAI API to generate a text completion asynchronously, returning the completion as a string.

#### `get_embedding`

**Scope:** OpenAIProvider

**Purpose:** Asynchronously retrieves the embedding for a given text input.

**Documentation:**

The get_embedding method uses the OpenAI API to obtain an embedding for the provided text, returning the embedding as a list of floats asynchronously.

### Variable

#### `self.client`

**Scope:** OpenAIProvider

**Purpose:** Holds the AsyncOpenAI client instance used for API interactions.

**Documentation:**

Instance variable initialized to manage API requests via the AsyncOpenAI class, requiring an API key.

#### `self.model`

**Scope:** OpenAIProvider

**Purpose:** Holds the model name identifier to be used in API calls.

**Documentation:**

Instance variable representing the model to use for API requests, defaulting to &#39;gpt-3.5-turbo&#39; if not provided.


[Back to Index](../README.md)