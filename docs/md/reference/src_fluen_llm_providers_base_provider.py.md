# src/fluen/llm_providers/base_provider.py

**Language:** Python  
**Last Modified:** 2024-11-13T17:48:17.498187

## Purpose

This code outlines an abstract base class for a language model provider interface. It defines the methods required for generating text from a prompt and obtaining text embeddings.

## Public API

- `BaseLLMProvider` (exposure)
- `generate` (exposure)
- `get_embedding` (exposure)

## Dependencies

- `abc` (external)
- `typing` (external)

## Elements

### Class

#### `BaseLLMProvider`

**Scope:** module

**Purpose:** To serve as an abstract base class for language model providers.

**Documentation:**

BaseLLMProvider defines an interface for components that interact with language models. It enforces the implementation of two asynchronous methods: generate and get_embedding, for text generation and embedding extraction respectively.

### Method

#### `generate`

**Scope:** BaseLLMProvider class

**Purpose:** Abstract method to generate text based on a prompt.

**Documentation:**

The generate method should be implemented by subclasses to take a text prompt and return generated text, asynchronously.

#### `get_embedding`

**Scope:** BaseLLMProvider class

**Purpose:** Abstract method to obtain text embeddings.

**Documentation:**

The get_embedding method should be implemented by subclasses to convert input text into a list of floats representing the text&#39;s embedding, asynchronously.


[Back to Index](../README.md)