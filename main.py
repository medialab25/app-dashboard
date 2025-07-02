#!/usr/bin/env python3
"""
App Dashboard - A FastAPI web application for managing locally installed web apps
"""

import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 