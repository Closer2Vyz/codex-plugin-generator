"""Configuration management for plugin generator."""

from pathlib import Path
from typing import Optional
import json
from pydantic import BaseModel


class Config(BaseModel):
    """Plugin generator configuration."""
    
    author: Optional[str] = ""
    email: Optional[str] = ""
    github: Optional[str] = ""
    include_tests: bool = True
    include_ci: bool = True
    default_license: str = "MIT"
    
    @classmethod
    def load(cls) -> "Config":
        """Load config from user's home directory."""
        config_path = Path.home() / ".plugin-generator.json"
        
        if not config_path.exists():
            return cls()
        
        try:
            with open(config_path, 'r') as f:
                data = json.load(f)
            return cls(**data)
        except Exception:
            return cls()
    
    def save(self) -> None:
        """Save config to user's home directory."""
        config_path = Path.home() / ".plugin-generator.json"
        
        with open(config_path, 'w') as f:
            json.dump(self.model_dump(), f, indent=2)
