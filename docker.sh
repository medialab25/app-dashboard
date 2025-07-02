#!/bin/bash

# App Dashboard Docker Management Script

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}  App Dashboard Docker Manager${NC}"
    echo -e "${BLUE}================================${NC}"
}

# Function to show usage
show_usage() {
    print_header
    echo ""
    echo "Usage: $0 [COMMAND] [OPTIONS]"
    echo ""
    echo "Commands:"
    echo "  dev, development    Start development environment with hot reload"
    echo "  prod, production    Start production environment"
    echo "  build               Build Docker images"
    echo "  logs                View logs"
    echo "  stop                Stop containers"
    echo "  restart             Restart containers"
    echo "  clean               Clean up containers and images"
    echo "  status              Show container status"
    echo "  shell               Open shell in running container"
    echo "  help                Show this help message"
    echo ""
    echo "Options:"
    echo "  -d, --daemon        Run in background (daemon mode)"
    echo "  -f, --follow        Follow logs (for logs command)"
    echo "  --dev-shell         Open shell in development container"
    echo "  --prod-shell        Open shell in production container"
    echo ""
    echo "Examples:"
    echo "  $0 dev              # Start development with hot reload"
    echo "  $0 dev -d           # Start development in background"
    echo "  $0 prod             # Start production"
    echo "  $0 logs -f          # Follow logs"
    echo "  $0 shell --dev      # Open shell in dev container"
    echo "  $0 clean            # Clean up everything"
}

# Function to check prerequisites
check_prerequisites() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi

    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    fi

    if [ ! -f "config/apps.json" ]; then
        print_warning "Configuration file not found: config/apps.json"
        print_warning "Please create the configuration file before starting the application."
        exit 1
    fi
}

# Function to start development environment
start_dev() {
    local daemon_mode=$1
    print_status "Starting development environment with hot reload..."
    
    if [ "$daemon_mode" = "true" ]; then
        print_status "Running in background mode..."
        docker-compose -f docker-compose.dev.yml up --build -d
        print_status "Development environment started in background"
        print_status "Use '$0 logs -f' to view logs"
    else
        print_status "Dashboard will be available at: http://localhost:8000"
        print_status "API documentation at: http://localhost:8000/docs"
        echo ""
        print_status "✨ Hot reload is enabled - your changes will be reflected automatically!"
        print_status "Press Ctrl+C to stop the server"
        echo ""
        docker-compose -f docker-compose.dev.yml up --build
    fi
}

# Function to start production environment
start_prod() {
    local daemon_mode=$1
    print_status "Starting production environment..."
    
    if [ "$daemon_mode" = "true" ]; then
        print_status "Running in background mode..."
        docker-compose up --build -d
        print_status "Production environment started in background"
        print_status "Use '$0 logs -f' to view logs"
    else
        print_status "Dashboard will be available at: http://localhost:8000"
        print_status "API documentation at: http://localhost:8000/docs"
        echo ""
        print_status "Press Ctrl+C to stop the server"
        echo ""
        docker-compose up --build
    fi
}

# Function to build images
build_images() {
    print_status "Building Docker images..."
    docker-compose build
    docker-compose -f docker-compose.dev.yml build
    print_status "All images built successfully!"
}

# Function to view logs
view_logs() {
    local follow_mode=$1
    local compose_file="docker-compose.yml"
    
    # Check if dev container is running
    if docker-compose -f docker-compose.dev.yml ps | grep -q "Up"; then
        compose_file="docker-compose.dev.yml"
        print_status "Showing development logs..."
    else
        print_status "Showing production logs..."
    fi
    
    if [ "$follow_mode" = "true" ]; then
        docker-compose -f "$compose_file" logs -f
    else
        docker-compose -f "$compose_file" logs
    fi
}

# Function to stop containers
stop_containers() {
    print_status "Stopping containers..."
    docker-compose down
    docker-compose -f docker-compose.dev.yml down
    print_status "All containers stopped!"
}

# Function to restart containers
restart_containers() {
    print_status "Restarting containers..."
    stop_containers
    sleep 2
    if docker-compose -f docker-compose.dev.yml ps | grep -q "Up"; then
        start_dev "false"
    else
        start_prod "false"
    fi
}

# Function to clean up
clean_up() {
    print_warning "This will remove all containers, images, and volumes!"
    read -p "Are you sure? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        print_status "Cleaning up Docker resources..."
        docker-compose down --rmi all -v
        docker-compose -f docker-compose.dev.yml down --rmi all -v
        docker system prune -a -f
        print_status "Cleanup completed!"
    else
        print_status "Cleanup cancelled."
    fi
}

# Function to show status
show_status() {
    print_status "Container Status:"
    echo ""
    echo "Production containers:"
    docker-compose ps
    echo ""
    echo "Development containers:"
    docker-compose -f docker-compose.dev.yml ps
}

# Function to open shell
open_shell() {
    local container_type=$1
    
    if [ "$container_type" = "dev" ]; then
        print_status "Opening shell in development container..."
        docker-compose -f docker-compose.dev.yml exec app-dashboard-dev /bin/bash
    elif [ "$container_type" = "prod" ]; then
        print_status "Opening shell in production container..."
        docker-compose exec app-dashboard /bin/bash
    else
        print_error "Invalid container type. Use --dev-shell or --prod-shell"
        exit 1
    fi
}

# Main script logic
main() {
    local command=""
    local daemon_mode="false"
    local follow_mode="false"
    local container_type=""

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            dev|development)
                command="dev"
                shift
                ;;
            prod|production)
                command="prod"
                shift
                ;;
            build)
                command="build"
                shift
                ;;
            logs)
                command="logs"
                shift
                ;;
            stop)
                command="stop"
                shift
                ;;
            restart)
                command="restart"
                shift
                ;;
            clean)
                command="clean"
                shift
                ;;
            status)
                command="status"
                shift
                ;;
            shell)
                command="shell"
                shift
                ;;
            help|--help|-h)
                show_usage
                exit 0
                ;;
            -d|--daemon)
                daemon_mode="true"
                shift
                ;;
            -f|--follow)
                follow_mode="true"
                shift
                ;;
            --dev-shell)
                container_type="dev"
                shift
                ;;
            --prod-shell)
                container_type="prod"
                shift
                ;;
            *)
                print_error "Unknown option: $1"
                show_usage
                exit 1
                ;;
        esac
    done

    # Check prerequisites for commands that need them
    if [[ "$command" =~ ^(dev|prod|build|restart)$ ]]; then
        check_prerequisites
    fi

    # Execute command
    case $command in
        dev)
            start_dev "$daemon_mode"
            ;;
        prod)
            start_prod "$daemon_mode"
            ;;
        build)
            build_images
            ;;
        logs)
            view_logs "$follow_mode"
            ;;
        stop)
            stop_containers
            ;;
        restart)
            restart_containers
            ;;
        clean)
            clean_up
            ;;
        status)
            show_status
            ;;
        shell)
            open_shell "$container_type"
            ;;
        "")
            print_error "No command specified"
            show_usage
            exit 1
            ;;
        *)
            print_error "Unknown command: $command"
            show_usage
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@" 