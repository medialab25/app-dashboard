# Docker Quick Reference

## 🚀 Quick Start

### Development (with Hot Reload)
```bash
# Using the unified script
./docker.sh dev

# Or manually
docker-compose -f docker-compose.dev.yml up --build
```

### Production
```bash
# Using the unified script
./docker.sh prod

# Or manually
docker-compose up --build
```

## 📋 Common Commands

### Using the Unified Script (Recommended)
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

### Manual Docker Compose Commands
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

# Utility
docker-compose build
docker-compose -f docker-compose.dev.yml build
docker-compose down --rmi all
docker system prune -a
```

## 🔧 Features

- **Hot Reload**: Code changes automatically restart the server in development
- **Volume Mounting**: Your local code is mounted into the container
- **Health Checks**: Built-in health monitoring in production
- **Security**: Runs as non-root user
- **Lightweight**: Minimal dependencies (no gcc/g++ required)

## 🌐 Access

- **Dashboard**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health 