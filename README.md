# App Dashboard

A modern, responsive web dashboard for managing and accessing locally installed web applications. Built with FastAPI and featuring a clean, intuitive interface.

## Features

- 🚀 **Fast & Modern**: Built with FastAPI for high performance
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- 🔍 **Search & Filter**: Find apps quickly with search and category filtering
- 🎨 **Beautiful UI**: Modern design with smooth animations and hover effects
- 📊 **Organized**: Apps are grouped by categories for easy navigation
- 🔗 **Direct Access**: Click any app to launch it in a new tab
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

Each application in `config/apps.json` should have the following structure:

```json
{
  "id": "unique-app-id",
  "name": "Display Name",
  "url": "http://localhost:port",
  "icon": "🎯",
  "description": "Brief description of the app",
  "category": "Category Name"
}
```

### Configuration Fields

- **id**: Unique identifier for the app (used in URLs)
- **name**: Display name shown on the dashboard
- **url**: Full URL where the app is accessible
- **icon**: Emoji or icon to represent the app
- **description**: Brief description of what the app does
- **category**: Category for grouping apps (e.g., "Development", "Media", "Monitoring")

### Example Configuration

```json
{
  "apps": [
    {
      "id": "homeassistant",
      "name": "Home Assistant",
      "url": "http://localhost:8123",
      "icon": "🏠",
      "description": "Home automation platform",
      "category": "Home"
    },
    {
      "id": "portainer",
      "name": "Portainer",
      "url": "http://localhost:9000",
      "icon": "🐳",
      "description": "Docker container management",
      "category": "Development"
    }
  ]
}
```

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
