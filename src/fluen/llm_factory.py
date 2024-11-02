from typing import Dict, Any
from fluen.llm_providers.base_provider import BaseLLMProvider
from fluen.llm_providers.openai_provider import OpenAIProvider
from fluen.llm_providers.mistral_ai_provider import MistralAIProvider
from fluen.llm_providers.ollama_provider import OllamaProvider

class LLMProviderFactory:
    _providers = {
        'openai': OpenAIProvider,
        'mistral': MistralAIProvider,
        'ollama': OllamaProvider
    }
    
    @classmethod
    def create(cls, provider_name: str, config: Dict[str, Any]) -> BaseLLMProvider:
        """Create an LLM provider instance based on the configuration."""
        if provider_name not in cls._providers:
            raise ValueError(f"Unsupported LLM provider: {provider_name}")
        
        provider_class = cls._providers[provider_name]
        return provider_class(config)
