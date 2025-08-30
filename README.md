# U-ITAM (Unified IT Asset Management) Platform

U-ITAM เป็นระบบจัดการทรัพย์สิน IT แบบครบวงจรที่ออกแบบมาเพื่อช่วยองค์กรในการติดตาม จัดการ และควบคุมทรัพย์สิน IT ทั้งหมดในระบบเครือข่าย

## ความสามารถหลัก

- **การจัดการทรัพย์สิน IT** - ติดตามและจัดการข้อมูลทรัพย์สิน IT ทั้งหมด
- **การค้นหาอุปกรณ์อัตโนมัติ** - สแกนและค้นหาอุปกรณ์ในเครือข่ายโดยอัตโนมัติ
- **การจัดการผู้ใช้และการพิสูจน์ตัวตน** - ระบบ Authentication และ Authorization
- **API RESTful** - API สำหรับการเชื่อมต่อกับระบบอื่น ๆ
- **Web Interface** - หน้าเว็บสำหรับการจัดการและติดตามทรัพย์สิน

## สถาปัตยกรรมระบบ

ระบบประกอบด้วย 4 ส่วนหลัก:

### 1. Backend API (FastAPI)
- **Framework**: FastAPI + Python 3.10
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy
- **Authentication**: JWT tokens
- **Features**: 
  - CRUD operations สำหรับทรัพย์สิน IT
  - User management
  - RESTful API endpoints
  - Database migrations with Alembic

### 2. Frontend Web App (React + Vite)
- **Framework**: React 18
- **Build Tool**: Vite
- **State Management**: Zustand
- **HTTP Client**: Axios
- **Routing**: React Router
- **Features**:
  - Asset management interface
  - User authentication
  - Responsive design
  - Real-time data updates

### 3. Discovery Service (Python)
- **Scanner**: Nmap + Python-nmap
- **Protocols**: SSH, SNMP, WMI (configurable)
- **Features**:
  - Network scanning
  - Asset discovery and identification
  - Automatic data reporting to API
  - Configurable scan intervals

### 4. Database (PostgreSQL)
- **Version**: PostgreSQL 15 Alpine
- **Features**:
  - Asset information storage
  - User management
  - Relationship management
  - Data persistence

## ความต้องการระบบ

- Docker และ Docker Compose
- อย่างน้อย 2GB RAM
- 10GB พื้นที่ดิสก์ว่าง
- Port 3000, 5432, และ 8000 ที่ว่าง

## การติดตั้งและใช้งาน

### 1. Clone Repository
```bash
git clone <repository-url>
cd ITAM_PROJECT
```

### 2. รัน Docker Compose
```bash
# รัน services ทั้งหมด
docker-compose up -d

# ดู logs
docker-compose logs -f

# หยุด services
docker-compose down
```

### 3. เข้าถึงระบบ
- **Web Application**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **Database**: localhost:5432

## การตั้งค่า

### Environment Variables
สามารถสร้างไฟล์ `.env` ในแต่ละ service directory เพื่อปรับแต่งการตั้งค่า:

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

### การตั้งค่าเครือข่าย
แก้ไขไฟล์ `docker-compose.yml` เพื่อปรับแต่ง network subnets ที่ต้องการสแกน

## การใช้งาน API

### Authentication
```bash
# Login
curl -X POST "http://localhost:8000/api/v1/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=user@example.com&password=password"
```

### Asset Management
```bash
# Get all assets
curl -X GET "http://localhost:8000/api/v1/assets" \
     -H "Authorization: Bearer <token>"

# Create new asset
curl -X POST "http://localhost:8000/api/v1/assets" \
     -H "Authorization: Bearer <token>" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Computer-001",
       "asset_tag": "COMP-001",
       "category": "Computer",
       "status": "Active"
     }'
```

## การพัฒนา

### Structure Overview
```
├── backend/                # FastAPI Backend
│   ├── app/
│   │   ├── api/           # API endpoints
│   │   ├── core/          # Configuration
│   │   ├── db/            # Database setup
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── crud/          # Database operations
│   │   └── security.py    # Authentication
│   └── requirements.txt
├── frontend/              # React Frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── services/      # API services
│   │   └── store/         # State management
│   └── package.json
├── discovery-service/     # Network Discovery
│   ├── src/
│   │   ├── scanner.py     # Network scanning
│   │   ├── reporter.py    # API reporting
│   │   └── config.py      # Configuration
│   └── requirements.txt
└── docker-compose.yml     # Docker orchestration
```

### Development Mode
```bash
# Backend development
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend development
cd frontend
npm install
npm run dev

# Discovery service development
cd discovery-service
pip install -r requirements.txt
python src/main.py
```

## การแก้ไขปัญหา

### ปัญหาที่พบบ่อย

1. **Database Connection Error**
   - ตรวจสอบว่า PostgreSQL service ทำงานอยู่
   - ตรวจสอบ credentials ใน environment variables

2. **API Authentication Error**
   - ตรวจสอบ JWT secret key
   - ตรวจสอบว่า token ยังไม่หมดอายุ

3. **Network Scanning Issues**
   - ตรวจสอบ network permissions
   - ตรวจสอบการตั้งค่า subnets
   - ตรวจสอบว่า nmap ติดตั้งอย่างถูกต้อง

### Logs
```bash
# ดู logs ของ service ทั้งหมด
docker-compose logs

# ดู logs ของ service เฉพาะ
docker-compose logs api
docker-compose logs web
docker-compose logs discovery
```

## การสนับสนุนและการพัฒนาต่อ

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการพัฒนา การปรับแต่ง หรือการขยายระบบ กรุณาติดต่อทีมพัฒนา

## License

This project is licensed under the MIT License.