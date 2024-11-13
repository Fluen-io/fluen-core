# fluen_config.yml

**Language:** Unknown  
**Last Modified:** 2024-11-13T17:50:50.689991

## Purpose

This configuration file is for setting up parameters for an application using GPT models via a provider like OpenAI.

## Public API

- `llm settings` (exposure)
- `output directories` (exposure)
- `cache directories` (exposure)

## Dependencies

- `openai` (external)

## Elements

### Variable

#### `api_key`

**Scope:** llm

**Purpose:** Stores the API key for authentication.

**Documentation:**

Contains the secret API key used to authenticate requests to the LLM service.

#### `cache_dir`

**Scope:** global

**Purpose:** Specifies the directory where cache data is stored.

**Documentation:**

Defines the location of the cache used by the application.

#### `default_export_type`

**Scope:** global

**Purpose:** Sets the default type for export operations.

**Documentation:**

Specifies the format in which data will be exported, defaulting to &#39;html&#39;.

#### `llm`

**Scope:** global

**Purpose:** Configuration block for the language model (LLM) settings.

**Documentation:**

Holds settings related to the interaction with the language model, including retries, model type, provider, and timeout.

#### `max_retries`

**Scope:** llm

**Purpose:** Determines the number of retry attempts for a failed request.

**Documentation:**

Specifies the number of times a request to the LLM can be retried upon failure.

#### `model`

**Scope:** llm

**Purpose:** Defines the specific version of the model to use.

**Documentation:**

Indicates which version of the GPT model is to be used (gpt-4o).

#### `output_dir`

**Scope:** global

**Purpose:** Designates the output directory for exported data.

**Documentation:**

The location where processed and exported data is saved.

#### `provider`

**Scope:** llm

**Purpose:** Specifies the LLM service provider.

**Documentation:**

Dictates which service provider, such as OpenAI, will be supplying the LLM functionality.

#### `temp_dir`

**Scope:** global

**Purpose:** Defines the temporary directory for intermediate data.

**Documentation:**

Stores temporary files used during the execution of the application.

#### `timeout`

**Scope:** llm

**Purpose:** Sets the request timeout duration.

**Documentation:**

Specifies the maximum time in seconds to wait for a response from the LLM.


[Back to Index](../README.md)