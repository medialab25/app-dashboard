import json
import os
from pathlib import Path
from typing import List, Optional, Dict
from app.models import App, AppConfig, Category


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
            
            # Handle both old and new config formats
            if "categories" in config_data:
                # New category-based format
                self._cached_config = AppConfig(**config_data)
            elif "apps" in config_data:
                # Old format - convert to new format
                apps = config_data["apps"]
                categories = {}
                
                # Group apps by category
                for app in apps:
                    category_name = app["category"]
                    if category_name not in categories:
                        categories[category_name] = {
                            "description": f"{category_name} applications",
                            "icon": "docker",  # Default icon
                            "color": "#6C757D",  # Default color
                            "apps": []
                        }
                    categories[category_name]["apps"].append(app)
                
                self._cached_config = AppConfig(categories=categories)
            else:
                raise ValueError("Invalid configuration format: missing 'categories' or 'apps'")
            
            self._last_modified = current_mtime
            return self._cached_config
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in configuration file: {e}")
        except Exception as e:
            raise RuntimeError(f"Error loading configuration: {e}")
    
    def get_apps(self) -> List[App]:
        """Get the list of all applications from the configuration."""
        config = self.load_config()
        all_apps = []
        for category in config.categories.values():
            all_apps.extend(category.apps)
        return all_apps
    
    def get_app_by_id(self, app_id: str) -> Optional[App]:
        """Get a specific application by its ID."""
        apps = self.get_apps()
        return next((app for app in apps if app.id == app_id), None)
    
    def get_apps_by_category(self, category: str) -> List[App]:
        """Get all applications in a specific category."""
        config = self.load_config()
        category_obj = config.categories.get(category)
        if category_obj:
            return category_obj.apps
        return []
    
    def get_categories(self) -> List[str]:
        """Get all unique categories from the configuration."""
        config = self.load_config()
        return sorted(list(config.categories.keys()))
    
    def get_category_info(self, category: str) -> Optional[Category]:
        """Get category information including metadata."""
        config = self.load_config()
        return config.categories.get(category)
    
    def get_all_categories(self) -> Dict[str, Category]:
        """Get all categories with their metadata."""
        config = self.load_config()
        return config.categories


# Global configuration manager instance
config_manager = ConfigManager() 