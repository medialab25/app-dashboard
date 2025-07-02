from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict


class App(BaseModel):
    """Model representing a single application in the dashboard."""
    id: str
    name: str
    url: HttpUrl
    icon: str
    description: str
    category: str


class Category(BaseModel):
    """Model representing a category with its metadata and apps."""
    description: str
    icon: str
    color: str
    apps: List[App]


class AppConfig(BaseModel):
    """Model representing the complete application configuration."""
    categories: Dict[str, Category]


class AppResponse(BaseModel):
    """Response model for API endpoints."""
    success: bool
    message: str
    data: Optional[List[App]] = None


class CategoryResponse(BaseModel):
    """Response model for category API endpoints."""
    success: bool
    message: str
    data: Optional[Dict[str, Category]] = None 