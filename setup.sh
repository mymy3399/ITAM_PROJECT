#!/bin/bash

# U-ITAM Setup Script
# This script sets up the complete U-ITAM system

set -e

echo "=========================================="
echo "       U-ITAM Setup Script"
echo "=========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "   Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose is not available. Please install Docker Compose."
    echo "   Visit: https://docs.docker.com/compose/install/"
    exit 1
fi

# Determine which docker compose command to use
DOCKER_COMPOSE_CMD="docker-compose"
if ! command -v docker-compose &> /dev/null; then
    DOCKER_COMPOSE_CMD="docker compose"
fi

echo "✅ Docker and Docker Compose are available"
echo ""

# Create .env file for backend if it doesn't exist
if [ ! -f backend/.env ]; then
    echo "📝 Creating backend .env file..."
    cat > backend/.env << EOF
DATABASE_URL=postgresql://uitam_user:uitam_password@db/uitam_db
SECRET_KEY=your-super-secret-key-change-this-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
EOF
    echo "✅ Backend .env file created"
fi

# Create .env file for discovery service if it doesn't exist
if [ ! -f discovery-service/.env ]; then
    echo "📝 Creating discovery service .env file..."
    cat > discovery-service/.env << EOF
API_BASE_URL=http://api:8000/api/v1
API_USERNAME=admin@example.com
API_PASSWORD=admin123
SCAN_INTERVAL_MINUTES=60
NETWORK_SUBNETS=["192.168.1.0/24"]
LOG_LEVEL=INFO
EOF
    echo "✅ Discovery service .env file created"
fi

# Create .env file for frontend if it doesn't exist
if [ ! -f frontend/.env ]; then
    echo "📝 Creating frontend .env file..."
    cat > frontend/.env << EOF
VITE_API_URL=http://localhost:8000
EOF
    echo "✅ Frontend .env file created"
fi

echo ""
echo "🚀 Starting U-ITAM system..."
echo ""

# Build and start the services
echo "📦 Building Docker containers..."
$DOCKER_COMPOSE_CMD build

echo ""
echo "🔧 Starting services..."
$DOCKER_COMPOSE_CMD up -d

echo ""
echo "⏳ Waiting for database to be ready..."
sleep 10

# Check if containers are running
if $DOCKER_COMPOSE_CMD ps | grep -q "uitam_db.*Up"; then
    echo "✅ Database is running"
else
    echo "❌ Database failed to start"
    exit 1
fi

if $DOCKER_COMPOSE_CMD ps | grep -q "uitam_api.*Up"; then
    echo "✅ Backend API is running"
else
    echo "❌ Backend API failed to start"
    exit 1
fi

if $DOCKER_COMPOSE_CMD ps | grep -q "uitam_web.*Up"; then
    echo "✅ Frontend web app is running"
else
    echo "❌ Frontend web app failed to start"
    exit 1
fi

if $DOCKER_COMPOSE_CMD ps | grep -q "uitam_discovery.*Up"; then
    echo "✅ Discovery service is running"
else
    echo "❌ Discovery service failed to start"
    exit 1
fi

echo ""
echo "🏗️  Running database migrations..."
$DOCKER_COMPOSE_CMD exec -T api alembic upgrade head

echo ""
echo "👤 Creating initial admin user..."
$DOCKER_COMPOSE_CMD exec -T api python -c "from app.db.init_db import main; main()"

echo ""
echo "=========================================="
echo "       🎉 Setup Complete! 🎉"
echo "=========================================="
echo ""
echo "Your U-ITAM system is now running!"
echo ""
echo "📱 Access the web application:"
echo "   http://localhost:3000"
echo ""
echo "🔗 API Documentation:"
echo "   http://localhost:8000/docs"
echo ""
echo "👤 Default admin credentials:"
echo "   Email:    admin@example.com"
echo "   Password: admin123"
echo ""
echo "🐳 Useful Docker commands:"
echo "   View logs:     $DOCKER_COMPOSE_CMD logs -f"
echo "   Stop system:   $DOCKER_COMPOSE_CMD down"
echo "   Restart:       $DOCKER_COMPOSE_CMD restart"
echo ""
echo "📚 For more information, see README.md"
echo ""