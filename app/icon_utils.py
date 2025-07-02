"""
Icon utilities for the dashboard application.
Handles icon mapping and fallback logic for app icons.
"""
import os
from pathlib import Path
from typing import Optional

# Available icons from Homarr Labs
AVAILABLE_ICONS = {
    # Media
    "plex": "plex",
    "sonarr": "sonarr",
    "radarr": "radarr", 
    "lidarr": "lidarr",
    "readarr": "readarr",
    "sabnzbd": "sabnzbd",
    "qbittorrent": "qbittorrent",
    "transmission": "transmission",
    "jellyfin": "jellyfin",
    "emby": "emby",
    
    # Infrastructure
    "portainer": "portainer",
    "grafana": "grafana",
    "prometheus": "prometheus",
    "nginx": "nginx",
    "apache": "apache",
    "mysql": "mysql",
    "postgresql": "postgresql",
    "redis": "redis",
    "docker": "docker",
    "kubernetes": "kubernetes",
    "jenkins": "jenkins",
    
    # Development
    "gitlab": "gitlab",
    "github": "github",
    "vscode": "vscode",
    
    # Web Applications
    "wordpress": "wordpress",
    "nextcloud": "nextcloud",
    
    # NAS/Server
    "synology": "synology",
    "unraid": "unraid",
    "proxmox": "proxmox",
}

# Fallback icons for common app types
FALLBACK_ICONS = {
    "media": "plex",
    "download": "qbittorrent", 
    "database": "mysql",
    "web": "nginx",
    "monitoring": "grafana",
    "development": "vscode",
    "server": "docker",
    "default": "docker"
}

def get_icon_path(icon_name: str) -> Optional[str]:
    """
    Get the path to an icon file if it exists.
    
    Args:
        icon_name: Name of the icon (without extension)
        
    Returns:
        Path to the icon file if it exists, None otherwise
    """
    icon_path = Path("static/icons") / f"{icon_name}.svg"
    return str(icon_path) if icon_path.exists() else None

def get_app_icon(app_name: str, app_category: str = None) -> str:
    """
    Get the appropriate icon for an app.
    
    Args:
        app_name: Name of the application
        app_category: Category of the application
        
    Returns:
        Icon HTML string (either SVG or fallback emoji)
    """
    # Try to find a matching icon by app name
    app_name_lower = app_name.lower()
    
    # Direct match
    if app_name_lower in AVAILABLE_ICONS:
        icon_name = AVAILABLE_ICONS[app_name_lower]
        icon_path = get_icon_path(icon_name)
        if icon_path:
            return f'<img src="/static/icons/{icon_name}.svg" alt="{app_name}" class="w-12 h-12 mx-auto">'
    
    # Partial match (e.g., "my-plex-server" -> "plex")
    for icon_key, icon_name in AVAILABLE_ICONS.items():
        if icon_key in app_name_lower:
            icon_path = get_icon_path(icon_name)
            if icon_path:
                return f'<img src="/static/icons/{icon_name}.svg" alt="{app_name}" class="w-12 h-12 mx-auto">'
    
    # Category-based fallback
    if app_category:
        category_lower = app_category.lower()
        for fallback_key, fallback_icon in FALLBACK_ICONS.items():
            if fallback_key in category_lower:
                icon_path = get_icon_path(fallback_icon)
                if icon_path:
                    return f'<img src="/static/icons/{fallback_icon}.svg" alt="{app_name}" class="w-12 h-12 mx-auto">'
    
    # Default fallback
    default_icon = FALLBACK_ICONS.get("default", "docker")
    icon_path = get_icon_path(default_icon)
    if icon_path:
        return f'<img src="/static/icons/{default_icon}.svg" alt="{app_name}" class="w-12 h-12 mx-auto">'
    
    # Ultimate fallback - emoji
    return "🔗"

def get_available_icons() -> list:
    """
    Get a list of all available icon names.
    
    Returns:
        List of available icon names
    """
    return list(AVAILABLE_ICONS.keys())

def get_icon_preview_html(icon_name: str) -> str:
    """
    Get HTML for icon preview.
    
    Args:
        icon_name: Name of the icon
        
    Returns:
        HTML string for the icon preview
    """
    icon_path = get_icon_path(icon_name)
    if icon_path:
        return f'<img src="/static/icons/{icon_name}.svg" alt="{icon_name}" class="w-8 h-8">'
    return "❌" 