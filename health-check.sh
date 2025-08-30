#!/bin/bash

# U-ITAM Health Check Script
# This script checks if all U-ITAM services are running properly

echo "=========================================="
echo "       U-ITAM Health Check"
echo "=========================================="
echo ""

# Determine which docker compose command to use
DOCKER_COMPOSE_CMD="docker-compose"
if ! command -v docker-compose &> /dev/null; then
    DOCKER_COMPOSE_CMD="docker compose"
fi

# Check if containers are running
echo "🔍 Checking container status..."
echo ""

if $DOCKER_COMPOSE_CMD ps | grep -q "uitam_db.*Up"; then
    echo "✅ Database (PostgreSQL) - Running"
    DB_STATUS="OK"
else
    echo "❌ Database (PostgreSQL) - Not Running"
    DB_STATUS="FAIL"
fi

if $DOCKER_COMPOSE_CMD ps | grep -q "uitam_api.*Up"; then
    echo "✅ Backend API (FastAPI) - Running"
    API_STATUS="OK"
else
    echo "❌ Backend API (FastAPI) - Not Running"
    API_STATUS="FAIL"
fi

if $DOCKER_COMPOSE_CMD ps | grep -q "uitam_web.*Up"; then
    echo "✅ Frontend (React) - Running"
    WEB_STATUS="OK"
else
    echo "❌ Frontend (React) - Not Running"
    WEB_STATUS="FAIL"
fi

if $DOCKER_COMPOSE_CMD ps | grep -q "uitam_discovery.*Up"; then
    echo "✅ Discovery Service - Running"
    DISCOVERY_STATUS="OK"
else
    echo "❌ Discovery Service - Not Running"
    DISCOVERY_STATUS="FAIL"
fi

echo ""
echo "🌐 Checking service connectivity..."
echo ""

# Check API health endpoint
if curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/ | grep -q "200"; then
    echo "✅ API endpoint - Accessible"
    API_CONNECT="OK"
else
    echo "❌ API endpoint - Not accessible"
    API_CONNECT="FAIL"
fi

# Check web application
if curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/ | grep -q "200"; then
    echo "✅ Web application - Accessible"
    WEB_CONNECT="OK"
else
    echo "❌ Web application - Not accessible"  
    WEB_CONNECT="FAIL"
fi

echo ""
echo "=========================================="
echo "         Health Check Summary"
echo "=========================================="
echo ""

if [ "$DB_STATUS" = "OK" ] && [ "$API_STATUS" = "OK" ] && [ "$WEB_STATUS" = "OK" ] && [ "$DISCOVERY_STATUS" = "OK" ] && [ "$API_CONNECT" = "OK" ] && [ "$WEB_CONNECT" = "OK" ]; then
    echo "🎉 All systems are healthy!"
    echo ""
    echo "🔗 Access your U-ITAM system:"
    echo "   Web App: http://localhost:3000"
    echo "   API Docs: http://localhost:8000/docs"
    echo ""
    echo "👤 Default login:"
    echo "   Email: admin@example.com"
    echo "   Password: admin123"
    exit 0
else
    echo "⚠️  Some services are not working properly"
    echo ""
    echo "🔧 Troubleshooting steps:"
    echo "1. Check logs: $DOCKER_COMPOSE_CMD logs -f"
    echo "2. Restart services: $DOCKER_COMPOSE_CMD restart"
    echo "3. Rebuild containers: $DOCKER_COMPOSE_CMD build --no-cache"
    echo ""
    exit 1
fi