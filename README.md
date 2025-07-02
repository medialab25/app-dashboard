# App Dashboard

A modern, responsive web dashboard for managing and accessing locally installed web applications. Built with FastAPI and featuring a clean, intuitive interface.

## Features

- 🚀 **Fast & Modern**: Built with FastAPI for high performance
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- 🔍 **Search & Filter**: Find apps quickly with search and category filtering
- 🎨 **Beautiful UI**: Modern design with smooth animations and hover effects
- 📊 **Organized**: Apps are grouped by categories for easy navigation
- 🔗 **Direct Access**: Click any app to launch it in a new tab
- 🎯 **Professional Icons**: High-quality SVG icons from Homarr Labs
- 📝 **API Documentation**: Built-in API docs with FastAPI
- ⚙️ **Easy Configuration**: Simple JSON configuration file

## Screenshots

The dashboard features:
- Clean, modern interface with gradient navigation
- App cards with icons, names, and descriptions
- Category-based organization
- Search and filter functionality
- Responsive grid layout

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd app-dash-test
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your applications**
   Edit `config/apps.json` to add your local web applications:
   ```json
   {
     "apps": [
       {
         "id": "myapp",
         "name": "My Application",
         "url": "http://localhost:3000",
         "icon": "🚀",
         "description": "My awesome web app",
         "category": "Development"
       }
     ]
   }
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Access the dashboard**
   Open your browser and go to: `http://localhost:8000`

## Configuration

### App Configuration Format

The configuration file `config/apps.json` now uses a category-based structure for better organization:

```json
{
  "categories": {
    "Category Name": {
      "description": "Category description",
      "icon": "category-icon",
      "color": "#HEXCOLOR",
      "apps": [
        {
          "id": "unique-app-id",
          "name": "Display Name",
          "url": "http://localhost:port",
          "icon": "app-name",
          "description": "Brief description of the app",
          "category": "Category Name"
        }
      ]
    }
  }
}
```

**Note**: The `icon` field is optional for both categories and apps. The system will automatically match names to appropriate icons from the Homarr Labs icon collection. You can view all available icons at `/icons`.

### Configuration Fields

#### Category Fields
- **description**: Description of what the category contains
- **icon**: Icon name for the category (optional)
- **apps**: Array of applications in this category

#### App Fields
- **id**: Unique identifier for the app (used in URLs)
- **name**: Display name shown on the dashboard
- **url**: Full URL where the app is accessible
- **icon**: Icon name (optional - system will auto-match based on app name)
- **description**: Brief description of what the app does
- **category**: Category name (must match the category key)

### Example Configuration

```json
{
  "categories": {
    "Media": {
      "description": "Media streaming, management, and automation tools",
      "icon": "plex",
      "apps": [
        {
          "id": "plex",
          "name": "Plex",
          "url": "http://localhost:32400",
          "description": "Media server and streaming platform",
          "category": "Media"
        }
      ]
    },
    "Infrastructure": {
      "description": "System management, containers, and infrastructure tools",
      "icon": "docker",
      "apps": [
        {
          "id": "portainer",
          "name": "Portainer",
          "url": "http://localhost:9000",
          "description": "Docker container management",
          "category": "Infrastructure"
        }
      ]
    }
  }
}
```

### Icon System

The dashboard uses high-quality SVG icons from the [Homarr Labs Dashboard Icons](https://github.com/homarr-labs/dashboard-icons) repository. The system automatically matches app names to appropriate icons:

- **Direct Match**: "Plex" → Plex icon
- **Partial Match**: "My Plex Server" → Plex icon  
- **Category Fallback**: Media category → Plex icon
- **Default Fallback**: Docker icon

Visit `/icons` to see all available icons and their names.

## Usage

### Dashboard Interface

1. **Browse Apps**: View all your applications organized by category
2. **Search**: Use the search bar to find specific applications
3. **Filter**: Use the category dropdown to filter by app type
4. **Launch**: Click "Launch App" to open any application in a new tab

### API Endpoints

The application provides several API endpoints:

- `GET /` - Main dashboard page
- `GET /api/apps` - Get all applications (JSON)
- `GET /api/apps/{app_id}` - Get specific application
- `GET /api/categories` - Get all categories
- `GET /api/categories/detailed` - Get all categories with metadata
- `GET /api/categories/{category}` - Get detailed category information
- `GET /api/apps/category/{category}` - Get apps by category
- `GET /redirect/{app_id}` - Redirect to specific application
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation

### API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development

### Project Structure

```
app-dash-test/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── models.py        # Pydantic models
│   └── config.py        # Configuration management
├── config/
│   └── apps.json        # Application configuration
├── templates/
│   ├── base.html        # Base template
│   ├── dashboard.html   # Main dashboard
│   └── error.html       # Error page
├── static/              # Static files (CSS, JS, images)
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### Running in Development Mode

```bash
python main.py
```

The application will run with auto-reload enabled, so changes to the code will automatically restart the server.

### Production Deployment

For production deployment, consider:

1. **Using a production ASGI server** like Gunicorn with Uvicorn workers
2. **Setting up a reverse proxy** (nginx, Apache)
3. **Using environment variables** for configuration
4. **Setting up SSL/TLS** certificates
5. **Implementing authentication** if needed

## Docker Support

### Prerequisites

- Docker
- Docker Compose

### Development Mode (with Hot Reload)

For development with automatic code reloading:

```bash
# Using the unified Docker script
./docker.sh dev

# Or manually with Docker Compose
docker-compose -f docker-compose.dev.yml up --build
```

**Features:**
- 🔄 **Hot Reload**: Code changes are automatically reflected
- 📁 **Volume Mounting**: Your local code is mounted into the container
- 🐛 **Debugging**: Full access to logs and debugging capabilities
- ⚡ **Fast Development**: No need to rebuild container for code changes

### Production Mode

For production deployment:

```bash
# Using the unified Docker script
./docker.sh prod

# Or manually with Docker Compose
docker-compose up --build
```

**Features:**
- 🚀 **Optimized**: Production-optimized container
- 🔒 **Secure**: Runs as non-root user
- 🏥 **Health Checks**: Built-in health monitoring
- 📊 **Monitoring**: Ready for production monitoring

### Docker Commands

#### Using the Unified Script (Recommended)
```bash
# Development
./docker.sh dev              # Start development with hot reload
./docker.sh dev -d           # Start development in background
./docker.sh logs -f          # Follow logs
./docker.sh stop             # Stop all containers

# Production
./docker.sh prod             # Start production
./docker.sh prod -d          # Start production in background

# Utility
./docker.sh build            # Build all images
./docker.sh status           # Show container status
./docker.sh clean            # Clean up everything
./docker.sh shell --dev      # Open shell in dev container
./docker.sh help             # Show all available commands
```

#### Manual Docker Compose Commands
```bash
# Development
docker-compose -f docker-compose.dev.yml up --build
docker-compose -f docker-compose.dev.yml up --build -d
docker-compose -f docker-compose.dev.yml logs -f
docker-compose -f docker-compose.dev.yml down

# Production
docker-compose up --build
docker-compose up --build -d
docker-compose logs -f
docker-compose down

# General
docker-compose build
docker-compose -f docker-compose.dev.yml build
docker-compose down --rmi all
docker system prune -a
```

### Docker Configuration

The project includes several Docker-related files:

- `Dockerfile` - Production container configuration
- `Dockerfile.dev` - Development container configuration
- `docker-compose.yml` - Production Docker Compose configuration
- `docker-compose.dev.yml` - Development Docker Compose configuration
- `.dockerignore` - Files to exclude from Docker builds
- `requirements.dev.txt` - Development dependencies
- `docker.sh` - Unified Docker management script

### Environment Variables

You can customize the Docker environment using environment variables:

```bash
# Development
ENVIRONMENT=development
PYTHONPATH=/app

# Production
ENVIRONMENT=production
```

### Volume Mounting

In development mode, the following volumes are mounted:
- `.:/app` - Your local code directory
- `./config:/app/config:ro` - Configuration files (read-only in production)

This ensures that:
- Code changes are immediately reflected
- Configuration can be updated without rebuilding
- Development is fast and efficient

Example production command:
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Customization

### Styling

The application uses Tailwind CSS for styling. You can customize the appearance by:

1. Modifying the CSS in `templates/base.html`
2. Adding custom CSS classes
3. Replacing Tailwind with your own CSS framework

### Adding Features

The modular structure makes it easy to add new features:

- **New API endpoints**: Add to `app/main.py`
- **New models**: Add to `app/models.py`
- **New templates**: Add to `templates/` directory
- **Static files**: Add to `static/` directory

## Troubleshooting

### Common Issues

1. **Port already in use**
   - Change the port in `main.py` or kill the process using the port

2. **Configuration file not found**
   - Ensure `config/apps.json` exists and is properly formatted

3. **Apps not loading**
   - Check the JSON syntax in `config/apps.json`
   - Verify all required fields are present

4. **Redirects not working**
   - Ensure the URLs in your configuration are correct and accessible

### Logs

The application logs to the console. Check for error messages when troubleshooting.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the API documentation at `/docs`
3. Open an issue on the project repository

---

**Built with ❤️ using FastAPI and Tailwind CSS** # app-dashboard
