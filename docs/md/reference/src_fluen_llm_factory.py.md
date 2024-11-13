# src/fluen/llm_factory.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:47:39.735133

## Purpose

The primary purpose of this code is to provide a factory class, LLMProviderFactory, that creates instances of different LLM provider classes based on a provider name and configuration map.

## Public API

- `LLMProviderFactory` (exposure)
- `LLMProviderFactory.create` (exposure)

## Dependencies

- `typing` (external)
- `fluen.llm_providers.base_provider` (external)
- `fluen.llm_providers.openai_provider` (external)
- `fluen.llm_providers.mistral_ai_provider` (external)
- `fluen.llm_providers.ollama_provider` (external)

## Elements

### Class

#### `LLMProviderFactory`

**Scope:** global

**Purpose:** A factory class used to create LLM provider instances.

**Documentation:**

LLMProviderFactory offers a class method to create various LLM provider instances based on the given provider name and configuration.

### Method

#### `create`

**Scope:** class

**Purpose:** Creates an instance of a selected LLM provider.

**Documentation:**

Class method that receives a provider name and configuration dictionary, verifies the provider exists, and returns an instance of the requested LLM provider class.

### Variable

#### `_providers`

**Scope:** class

**Purpose:** Holds mappings of provider names to their respective classes.

**Documentation:**

A dictionary mapping string identifiers to LLM provider classes; used to determine which class to instantiate in the create method.


[Back to Index](../README.md)