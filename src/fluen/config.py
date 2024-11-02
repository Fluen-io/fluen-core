from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Any
import yaml
import os

@dataclass
class LLMConfig:
    provider: str
    api_key: Optional[str] = None
    model: Optional[str] = None
    api_base_url: Optional[str] = None
    max_retries: int = 3
    timeout: int = 60

@dataclass
class FluenConfig:
    llm: LLMConfig
    output_dir: Path = Path("docs")
    cache_dir: Path = Path(".fluen/cache")
    temp_dir: Path = Path(".fluen/temp")
    default_export_type: str = "html"
    
    @classmethod
    def load(cls, config_path: Path) -> 'FluenConfig':
        """Load configuration from YAML file."""
        if not config_path.exists():
            return cls.create_default(config_path)
        
        with open(config_path, 'r') as f:
            config_data = yaml.safe_load(f)
            
        llm_config = LLMConfig(**config_data.get('llm', {}))
        return cls(
            llm=llm_config,
            output_dir=Path(config_data.get('output_dir', 'docs')),
            cache_dir=Path(config_data.get('cache_dir', '.fluen/cache')),
            temp_dir=Path(config_data.get('temp_dir', '.fluen/temp')),
            default_export_type=config_data.get('default_export_type', 'html')
        )
    
    @classmethod
    def create_default(cls, config_path: Path) -> 'FluenConfig':
        """Create and save default configuration."""
        config = cls(
            llm=LLMConfig(
                provider="openai",
                model="gpt-3.5-turbo"
            )
        )
        
        # Create parent directories if they don't exist
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save default configuration
        config_dict = {
            'llm': {
                'provider': config.llm.provider,
                'model': config.llm.model,
                'max_retries': config.llm.max_retries,
                'timeout': config.llm.timeout
            },
            'output_dir': str(config.output_dir),
            'cache_dir': str(config.cache_dir),
            'temp_dir': str(config.temp_dir),
            'default_export_type': config.default_export_type
        }
        
        with open(config_path, 'w') as f:
            yaml.dump(config_dict, f, default_flow_style=False)
        
        return config
    
    def ensure_directories(self):
        """Ensure all required directories exist."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
