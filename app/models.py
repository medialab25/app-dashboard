from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class App(BaseModel):
    """Model representing a single application in the dashboard."""
    id: str
    name: str
    url: HttpUrl
    icon: str
    description: str
    category: str


class AppConfig(BaseModel):
    """Model representing the complete application configuration."""
    apps: List[App]


class AppResponse(BaseModel):
    """Response model for API endpoints."""
    success: bool
    message: str
    data: Optional[List[App]] = None 