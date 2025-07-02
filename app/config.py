import json
import os
from pathlib import Path
from typing import List, Optional
from app.models import App, AppConfig


class ConfigManager:
    """Manages application configuration loading and caching."""
    
    def __init__(self, config_path: str = "config/apps.json"):
        self.config_path = Path(config_path)
        self._cached_config: Optional[AppConfig] = None
        self._last_modified: Optional[float] = None
    
    def load_config(self) -> AppConfig:
        """Load and parse the configuration file with caching."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        # Check if file has been modified since last load
        current_mtime = self.config_path.stat().st_mtime
        if (self._cached_config is not None and 
            self._last_modified is not None and 
            current_mtime <= self._last_modified):
            return self._cached_config
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
            
            self._cached_config = AppConfig(**config_data)
            self._last_modified = current_mtime
            return self._cached_config
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in configuration file: {e}")
        except Exception as e:
            raise RuntimeError(f"Error loading configuration: {e}")
    
    def get_apps(self) -> List[App]:
        """Get the list of applications from the configuration."""
        config = self.load_config()
        return config.apps
    
    def get_app_by_id(self, app_id: str) -> Optional[App]:
        """Get a specific application by its ID."""
        apps = self.get_apps()
        return next((app for app in apps if app.id == app_id), None)
    
    def get_apps_by_category(self, category: str) -> List[App]:
        """Get all applications in a specific category."""
        apps = self.get_apps()
        return [app for app in apps if app.category.lower() == category.lower()]
    
    def get_categories(self) -> List[str]:
        """Get all unique categories from the applications."""
        apps = self.get_apps()
        return sorted(list(set(app.category for app in apps)))


# Global configuration manager instance
config_manager = ConfigManager() 