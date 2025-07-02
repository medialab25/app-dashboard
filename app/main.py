from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import logging
from typing import List

from app.config import config_manager
from app.models import App, AppResponse
from app.icon_utils import get_app_icon

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="App Dashboard",
    description="A dashboard selector for locally installed web applications",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Main dashboard page."""
    try:
        apps = config_manager.get_apps()
        categories = config_manager.get_categories()
        
        # Group apps by category
        apps_by_category = {}
        for category in categories:
            apps_by_category[category] = config_manager.get_apps_by_category(category)
        
        return templates.TemplateResponse(
            "dashboard.html",
            {
                "request": request,
                "apps": apps,
                "categories": categories,
                "apps_by_category": apps_by_category,
                "get_app_icon": get_app_icon
            }
        )
    except Exception as e:
        logger.error(f"Error loading dashboard: {e}")
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error_message": "Failed to load dashboard configuration"
            }
        )


@app.get("/api/apps", response_model=AppResponse)
async def get_apps():
    """API endpoint to get all applications."""
    try:
        apps = config_manager.get_apps()
        return AppResponse(
            success=True,
            message="Applications retrieved successfully",
            data=apps
        )
    except Exception as e:
        logger.error(f"Error retrieving apps: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/apps/{app_id}", response_model=AppResponse)
async def get_app(app_id: str):
    """API endpoint to get a specific application by ID."""
    try:
        app = config_manager.get_app_by_id(app_id)
        if not app:
            raise HTTPException(status_code=404, detail="Application not found")
        
        return AppResponse(
            success=True,
            message="Application retrieved successfully",
            data=[app]
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving app {app_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/categories")
async def get_categories():
    """API endpoint to get all categories."""
    try:
        categories = config_manager.get_categories()
        return {
            "success": True,
            "message": "Categories retrieved successfully",
            "data": categories
        }
    except Exception as e:
        logger.error(f"Error retrieving categories: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/apps/category/{category}")
async def get_apps_by_category(category: str):
    """API endpoint to get applications by category."""
    try:
        apps = config_manager.get_apps_by_category(category)
        return {
            "success": True,
            "message": f"Applications in category '{category}' retrieved successfully",
            "data": apps
        }
    except Exception as e:
        logger.error(f"Error retrieving apps for category {category}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/redirect/{app_id}")
async def redirect_to_app(app_id: str):
    """Redirect to a specific application."""
    try:
        app = config_manager.get_app_by_id(app_id)
        if not app:
            raise HTTPException(status_code=404, detail="Application not found")
        
        logger.info(f"Redirecting to {app.name} at {app.url}")
        return RedirectResponse(url=str(app.url))
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error redirecting to app {app_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Dashboard is running"}


@app.get("/icons", response_class=HTMLResponse)
async def icon_gallery(request: Request):
    """Icon gallery page showing all available icons."""
    return templates.TemplateResponse("icon_gallery.html", {"request": request})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 