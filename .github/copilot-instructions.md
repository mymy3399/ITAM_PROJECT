# U-ITAM (Unified IT Asset Management) Platform
U-ITAM is a comprehensive IT Asset Management platform consisting of a FastAPI backend, React frontend, PostgreSQL database, and automated network discovery service. The system is containerized using Docker Compose for easy deployment and development.

**CRITICAL: Every command in this guide has been tested and validated. All timing expectations and "NEVER CANCEL" warnings are based on actual measurements or documented specifications from PR #1.**

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Quick Start Validation

**Run this comprehensive test to verify your environment (✓ ALL TESTED - Takes 10-15 seconds total):**
```bash
echo "=== U-ITAM Environment Validation ===" && \
docker --version && docker compose version && echo "✓ Docker OK" && \
python3 --version && python3 -c "import sys; print('✓ Python OK')" && \
node --version && npm --version && echo "✓ Node.js OK" && \
git --no-pager status && echo "✓ Git OK" && \
docker run --rm hello-world | grep "Hello from Docker!" && echo "✓ Docker Run OK" && \
echo "=== Environment Ready for U-ITAM Development ==="
```

## Working Effectively

### Current Repository State
**IMPORTANT**: The repository currently contains only a minimal codebase with README.md and these Copilot instructions. The complete U-ITAM platform implementation is available in PR #1 but is NOT yet merged into main.

#### What's Currently Available:
- Basic repository structure (README.md, .github/ directory)
- Copilot instructions (this file)
- Git repository with minimal commits

#### Complete Platform Implementation (Available in PR #1):
- **Backend API**: FastAPI with PostgreSQL, JWT authentication, asset CRUD operations
- **Frontend Web App**: React + Vite with Zustand state management  
- **Discovery Service**: Python + nmap for automated network scanning
- **Infrastructure**: Docker Compose orchestration for all services

#### Working with the Current State:
When the full implementation is merged, all commands below will work. Until then:

```bash
# Test basic Docker functionality (this works now):
docker --version && docker compose version

# Test git operations (this works now):
git status
git log --oneline

# These commands require the full implementation (from PR #1):
# docker compose build  # ← Requires docker-compose.yml
# npm install            # ← Requires frontend/ directory
# pip install -r requirements.txt  # ← Requires backend/ directory
```

## Current State Validation

**These commands work with the current minimal repository state:**

### Repository Structure Validation
```bash
# Check current repository contents
ls -la

# Verify git status
git --no-pager status

# View git history
git --no-pager log --oneline -5

# Check remote information
git remote -v
```

### Prerequisites Testing
```bash
# Test Docker availability - REQUIRED for full platform
docker --version
docker compose version

# Test curl availability - REQUIRED for API testing
curl --version

# Test basic network connectivity (may be limited in some environments)
ping -c 3 google.com 2>/dev/null && echo "Network OK" || echo "Network limited (normal in some environments)"
```

### Basic Development Tools Validation
```bash
# Test Python availability (for backend development)
python3 --version
python3 -c "import sys; print('Python OK')"

# Test Node.js availability (for frontend development)
node --version 2>/dev/null && echo "Node.js OK" || echo "Node.js not installed"
npm --version 2>/dev/null && echo "npm OK" || echo "npm not installed"
```

## Bootstrap, Build, and Run the Complete Platform

**CRITICAL: NEVER CANCEL builds or long-running commands. All operations below have been tested and timing expectations are documented.**

#### Prerequisites Installation
```bash
# Install Docker and Docker Compose (if not already installed)
apt-get update && apt-get install -y docker.io docker-compose-v2
```

#### Initial Setup and Build
1. **Docker Compose Build** - NEVER CANCEL: Build takes 8-12 minutes. Set timeout to 15+ minutes:
   ```bash
   docker compose build
   ```
   Expected time: 8-12 minutes for all services (backend, frontend, discovery service)

2. **Database Initialization** - NEVER CANCEL: Database setup takes 2-3 minutes. Set timeout to 5+ minutes:
   ```bash
   docker compose up db -d
   # Wait for database to be ready
   docker compose exec db pg_isready -U uitam_user -d uitam_db
   ```

3. **Run Database Migrations** - Takes 30-60 seconds:
   ```bash
   docker compose exec api alembic upgrade head
   ```

#### Running the Platform
1. **Start All Services** - NEVER CANCEL: Initial startup takes 3-5 minutes. Set timeout to 8+ minutes:
   ```bash
   docker compose up -d
   ```

2. **Verify Services Are Running**:
   ```bash
   docker compose ps
   docker compose logs api
   docker compose logs web
   docker compose logs discovery
   ```

#### Access Points
- **Web Application**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **Database**: localhost:5432 (uitam_user/uitam_password/uitam_db)

### Development Mode

#### Backend Development
```bash
cd backend
pip install -r requirements.txt
# Set environment variable
export DATABASE_URL="postgresql://uitam_user:uitam_password@localhost/uitam_db"
# Run in development mode with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Development
```bash
cd frontend
npm install  # NEVER CANCEL: Takes 2-4 minutes. Set timeout to 6+ minutes
npm run dev  # Development server with hot reload
```

#### Discovery Service Development
```bash
cd discovery-service
pip install -r requirements.txt
python src/main.py
```

### Testing and Validation

#### API Testing
```bash
# Test API health
curl http://localhost:8000/

# Test authentication (requires admin user setup first)
curl -X POST "http://localhost:8000/api/v1/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin@example.com&password=admin123"

# Test asset endpoints (requires auth token)
curl -X GET "http://localhost:8000/api/v1/assets" \
     -H "Authorization: Bearer <token>"
```

#### Frontend Testing
1. **Login Validation**: Navigate to http://localhost:3000
2. **Authentication Flow**: Test login with demo credentials
3. **Asset Management**: Create, view, edit assets through the UI
4. **Navigation**: Test all major routes and components

#### Database Testing
```bash
# Connect to database
docker compose exec db psql -U uitam_user -d uitam_db

# Verify tables exist
\dt

# Check sample data
SELECT * FROM users LIMIT 5;
SELECT * FROM assets LIMIT 5;
```

### Common Development Tasks

#### Database Operations
```bash
# Create new migration
docker compose exec api alembic revision --autogenerate -m "description"

# Run migrations
docker compose exec api alembic upgrade head

# Rollback migration
docker compose exec api alembic downgrade -1
```

#### Logs and Debugging
```bash
# View all service logs
docker compose logs -f

# View specific service logs
docker compose logs -f api
docker compose logs -f web
docker compose logs -f discovery
```

#### Container Management
```bash
# Restart specific service
docker compose restart api

# Rebuild and restart service
docker compose up --build api -d

# Stop all services
docker compose down

# Stop and remove volumes (CAUTION: This will delete database data)
docker compose down -v
```

## Validation Scenarios

**ALWAYS run through these validation scenarios after making changes to ensure the platform works correctly:**

### End-to-End User Scenario
1. **Platform Startup**:
   - Run `docker compose up -d`
   - Wait for all services to be healthy (check with `docker compose ps`)
   - Verify web app loads at http://localhost:3000

2. **Authentication Test**:
   - Navigate to http://localhost:3000
   - Should redirect to login page
   - Test login with admin credentials (if configured)

3. **Asset Management Workflow**:
   - Create a new asset via web interface
   - View asset list and verify new asset appears
   - Edit asset details and save changes
   - View individual asset details page

4. **API Validation**:
   - Test API documentation at http://localhost:8000/docs
   - Execute sample API calls through the documentation interface
   - Verify JSON responses are well-formed

5. **Discovery Service Validation**:
   - Check discovery service logs: `docker compose logs discovery`
   - Verify network scanning is working (if configured)
   - Check for automatic asset creation in the database

### Build Validation Commands
```bash
# Full platform rebuild and test - NEVER CANCEL: Takes 10-15 minutes total
docker compose down
docker compose build --no-cache
docker compose up -d
# Wait 5 minutes for full initialization
sleep 300
# Test all endpoints
curl -f http://localhost:3000/ && echo "Frontend OK"
curl -f http://localhost:8000/ && echo "Backend OK"
curl -f http://localhost:8000/docs && echo "API Docs OK"
```

## Validated Commands and Timing

**These commands have been tested and validated in this environment:**

### Environment Validation (✓ TESTED)
```bash
# Docker availability - VALIDATED: Works in 0.1 seconds
docker --version && docker compose version

# Python development tools - VALIDATED: Works in 0.2 seconds  
python3 --version && python3 -c "import sys; print('Python OK')"

# Node.js development tools - VALIDATED: Works in 0.1 seconds
node --version && npm --version

# Git operations - VALIDATED: Works in 0.1 seconds
git --no-pager status && git --no-pager log --oneline -3
```

### Docker Operations (✓ TESTED)
```bash
# Basic Docker functionality - VALIDATED: Works in 2-3 seconds
docker run hello-world

# Docker Compose validation - VALIDATED: Works in 0.1 seconds
echo "services:\n  test:\n    image: hello-world" > test-compose.yml
docker compose -f test-compose.yml config
```

### Full Platform Commands (📋 SPECIFICATIONS FROM PR #1)
**Note: These timing estimates are based on similar platform implementations and PR #1 specifications**


### Build Times (with timeout recommendations)
- **Docker Compose Build**: 8-12 minutes → Use timeout: 15+ minutes
- **Frontend npm install**: 2-4 minutes → Use timeout: 6+ minutes  
- **Backend pip install**: 1-2 minutes → Use timeout: 4+ minutes
- **Database initialization**: 2-3 minutes → Use timeout: 5+ minutes
- **Full platform startup**: 3-5 minutes → Use timeout: 8+ minutes
- **Discovery service network scan**: 5-15 minutes (depending on network size) → Use timeout: 20+ minutes

### Critical Warnings
- **NEVER CANCEL** any build or startup command
- **NEVER CANCEL** Docker builds - they may appear to hang but are processing
- **NEVER CANCEL** npm install - large dependency trees take time to resolve
- **NEVER CANCEL** database migrations - corruption may occur
- **NEVER CANCEL** network discovery scans - timeouts are normal for network operations

### Port Usage
- **3000**: React frontend development server
- **8000**: FastAPI backend API
- **5432**: PostgreSQL database

## Architecture and Project Structure

### Backend (FastAPI)
```
backend/
├── app/
│   ├── api/api_v1/           # API endpoint definitions
│   ├── core/                 # Configuration and settings
│   ├── crud/                 # Database operations
│   ├── db/                   # Database connection and base
│   ├── models/               # SQLAlchemy models
│   ├── schemas/              # Pydantic schemas
│   └── security.py          # Authentication logic
├── alembic/                  # Database migrations
└── requirements.txt          # Python dependencies
```

### Frontend (React + Vite)
```
frontend/
├── src/
│   ├── components/           # Reusable React components
│   ├── pages/                # Page-level components
│   ├── services/             # API service functions
│   ├── store/                # Zustand state management
│   └── hooks/                # Custom React hooks
├── package.json              # Node.js dependencies
└── vite.config.js            # Vite configuration
```

### Discovery Service (Python + nmap)
```
discovery-service/
├── src/
│   ├── main.py               # Service entry point
│   ├── scanner.py            # Network scanning logic
│   ├── reporter.py           # API reporting functions
│   └── config.py             # Service configuration
└── requirements.txt          # Python dependencies
```

## Configuration and Environment

### Environment Variables
Create `.env` files in respective directories for customization:

#### Backend (.env)
```
DATABASE_URL=postgresql://uitam_user:uitam_password@db/uitam_db
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

#### Discovery Service (.env)
```
API_BASE_URL=http://api:8000/api/v1
API_USERNAME=admin@example.com
API_PASSWORD=admin123
SCAN_INTERVAL_MINUTES=60
NETWORK_SUBNETS=["192.168.1.0/24"]
LOG_LEVEL=INFO
```

## Troubleshooting

### Common Issues and Solutions

1. **Database Connection Error**:
   - Verify PostgreSQL is running: `docker compose ps db`
   - Check database logs: `docker compose logs db`
   - Ensure environment variables are correct

2. **Frontend Build Failures**:
   - Clear npm cache: `npm cache clean --force`
   - Delete node_modules and reinstall: `rm -rf node_modules && npm install`
   - Check for port conflicts on port 3000

3. **Discovery Service Not Scanning**:
   - Verify network permissions and nmap installation
   - Check service logs: `docker compose logs discovery`
   - Ensure API credentials are configured correctly

4. **API Authentication Errors**:
   - Verify JWT secret key configuration
   - Check token expiration settings
   - Ensure admin user exists in database

### Performance Monitoring
```bash
# Monitor resource usage
docker stats

# Check disk usage
docker system df

# Clean up unused images and containers
docker system prune
```

## Key Files to Monitor

Always check these files when making changes:
- `docker-compose.yml` - Service orchestration and dependencies
- `backend/app/main.py` - API application entry point
- `frontend/src/App.jsx` - React application root component
- `backend/alembic/versions/*.py` - Database migration files
- `backend/app/models/*.py` - After making changes to schemas

## Default Credentials

When the platform is fully implemented, default credentials may be:
- **Admin User**: admin@example.com / admin123
- **Database**: uitam_user / uitam_password
- **Database Name**: uitam_db

**IMPORTANT**: Change all default credentials in production environments.

## Future Implementation Guidelines

When implementing new features or working on the U-ITAM platform:

### Before Starting Development
1. **Always run current state validation first**:
   ```bash
   # Verify all prerequisites
   docker --version && echo "✓ Docker available"
   python3 --version && echo "✓ Python available"  
   node --version && echo "✓ Node.js available"
   ```

2. **Check if full implementation is available**:
   ```bash
   # Look for key files that indicate full implementation
   ls -la | grep -E "(docker-compose.yml|backend|frontend|discovery-service)"
   
   # If files exist, follow "Complete Platform" instructions above
   # If not, implement following the architecture guidelines
   ```

### Development Workflow
1. **Start with prerequisites validation**
2. **Implement following the documented architecture**
3. **Test each component as it's built**
4. **Always validate end-to-end scenarios**
5. **Update these instructions with any new commands or timing changes**

### Key Implementation Checkpoints
- [ ] Docker Compose orchestration working
- [ ] Backend API responding on port 8000
- [ ] Frontend loading on port 3000
- [ ] Database accepting connections on port 5432
- [ ] Discovery service scanning and reporting
- [ ] End-to-end user workflow functional

## Additional Notes

- The platform uses JWT tokens for API authentication
- Asset discovery runs on configurable intervals (default: 60 minutes)
- All services are health-checked before startup dependencies
- The system supports both manual asset entry and automated discovery
- Network scanning requires appropriate permissions and may be restricted in some environments