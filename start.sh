#!/bin/bash

# App Dashboard Startup Script

echo "🚀 Starting App Dashboard..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if requirements are installed
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check if config file exists
if [ ! -f "config/apps.json" ]; then
    echo "❌ Configuration file not found: config/apps.json"
    echo "Please create the configuration file before starting the application."
    exit 1
fi

# Start the application
echo "🌟 Starting FastAPI server..."
echo "📱 Dashboard will be available at: http://localhost:8000"
echo "📚 API documentation at: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python main.py 