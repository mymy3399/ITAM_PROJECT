# ITAM_PROJECT - ระบบจัดการทรัพย์สิน IT สำหรับหน่วยงานราชการไทย

โปรเจกต์นี้เป็นระบบจัดการทรัพย์สิน IT (IT Asset Management) สำหรับหน่วยงานราชการไทย โดยใช้เทคโนโลยีเว็บแอปพลิเคชันที่ทันสมัย

**ให้อ้างอิงคำแนะนำนี้เป็นอันดับแรก และใช้การค้นหาหรือคำสั่ง bash เฉพาะเมื่อพบข้อมูลที่ไม่ตรงกับที่ระบุไว้ที่นี่**

## วัตถุประสงค์และบริบทของโปรเจกต์

### เป้าหมายหลัก
- **สร้างเว็บแอปพลิเคชัน IT Asset Management สำหรับหน่วยงานราชการไทย**
- ระบบติดตาม ควบคุม และจัดการทรัพย์สิน IT ครบวงจร
- รองรับการทำงานแบบ Multi-user และ Multi-department
- มีระบบรายงานและการวิเคราะห์ข้อมูลทรัพย์สิน

### หลักการภาษาและการเขียนโค้ด
- **ข้อความที่ปรากฏกับผู้ใช้**: ภาษาไทยเท่านั้น (UI labels, messages, notifications)
- **คอมเมนต์และเอกสาร**: ภาษาไทยเท่านั้น (comments, documentation, README)
- **โค้ดทั้งหมด**: ภาษาอังกฤษเท่านั้น (variables, functions, classes, filenames, API endpoints)

```javascript
// ✅ ถูกต้อง - คอมเมนต์เป็นภาษาไทย โค้ดเป็นภาษาอังกฤษ
const assetManager = {
  // ฟังก์ชันสำหรับสร้างทรัพย์สินใหม่
  createAsset: (assetData) => {
    return processAssetCreation(assetData);
  }
};

// ❌ ผิด - ตัวแปรเป็นภาษาไทย
const ผู้จัดการทรัพย์สิน = {
  สร้างทรัพย์สิน: (ข้อมูลทรัพย์สิน) => {
    return processAssetCreation(ข้อมูลทรัพย์สิน);
  }
};
```

## เทคโนโลยีและ Architecture

### Core Technology Stack
```
Frontend:
├── React 18 (Functional Components + Hooks)
├── Vite (Build Tool)
├── Tailwind CSS (Styling)
├── React Router v6 (Routing)
├── React Hook Form (Form Management)
└── Axios (HTTP Client)

Backend:
├── Node.js
├── Express.js
├── JWT (Authentication)
└── bcrypt (Password Hashing)

Database:
├── PostgreSQL
└── Connection via process.env.DATABASE_URL

Deployment:
├── Docker
├── Docker Compose
└── Multi-stage builds
```

### 3-Tier Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │    Database     │
│   (React/Vite)  │◄──►│  (Node/Express) │◄──►│  (PostgreSQL)   │
│   Port: 3000    │    │   Port: 5000    │    │   Port: 5432    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### RESTful API Design
- **HTTP Methods**: GET (อ่าน), POST (สร้าง), PUT (แก้ไข), DELETE (ลบ)
- **API Endpoints**: ใช้ plural nouns เสมอ (เช่น `/api/assets`, `/api/users`)
- **Status Codes**: ใช้รหัสสถานะ HTTP ที่เหมาะสม (200, 201, 400, 401, 404, 500)
- **Response Format**: JSON เสมอ พร้อมข้อความภาษาไทย

```javascript
// ✅ ถูกต้อง - API endpoint และ response structure
GET /api/assets
{
  "success": true,
  "message": "ดึงข้อมูลทรัพย์สินสำเร็จ",
  "data": [
    {
      "id": 1,
      "assetName": "Computer-001",
      "assetType": "desktop",
      "department": "IT"
    }
  ]
}

// ❌ ผิด - endpoint เป็นเอกพจน์
GET /api/asset
```

## โครงสร้างโปรเจกต์และไดเรกทอรี

### Frontend Structure
```
src/
├── components/          # Component ที่ใช้ซ้ำได้
│   ├── common/         # Component พื้นฐาน (Button, Modal, etc.)
│   ├── forms/          # Form components
│   └── layout/         # Layout components (Header, Sidebar, etc.)
├── pages/              # Page components
│   ├── assets/         # หน้าจัดการทรัพย์สิน
│   ├── users/          # หน้าจัดการผู้ใช้
│   ├── reports/        # หน้ารายงาน
│   └── dashboard/      # หน้าแดชบอร์ด
├── services/           # API services
│   ├── api.js          # Axios configuration
│   ├── assetService.js # Asset-related API calls
│   └── authService.js  # Authentication API calls
├── utils/              # Utility functions
├── hooks/              # Custom React hooks
├── styles/             # Global styles และ Tailwind config
└── App.jsx             # Main application component
```

### Backend Structure
```
server/
├── routes/             # Express routes (ใช้ Express Router)
│   ├── assets.js       # Asset management routes
│   ├── users.js        # User management routes
│   ├── auth.js         # Authentication routes
│   └── reports.js      # Reporting routes
├── middleware/         # Express middleware
│   ├── auth.js         # JWT authentication middleware
│   ├── validation.js   # Input validation middleware
│   └── errorHandler.js # Error handling middleware
├── models/             # Database models/schemas
├── controllers/        # Business logic controllers
├── config/             # Configuration files
│   └── database.js     # Database connection config
├── utils/              # Server utility functions
└── index.js            # Main server entry point
```

### Database Schema
- **ใช้ database_schema.sql** เป็นแนวทางในการสร้างตาราง
- **Table names**: ใช้ plural nouns (เช่น `assets`, `users`, `departments`)
- **Column names**: ใช้ snake_case (เช่น `asset_name`, `created_at`)
- **Foreign keys**: ใช้รูปแบบ `table_id` (เช่น `user_id`, `department_id`)

```sql
-- ✅ ตัวอย่างโครงสร้างตารางที่ถูกต้อง
CREATE TABLE assets (
    id SERIAL PRIMARY KEY,
    asset_name VARCHAR(255) NOT NULL,
    asset_type VARCHAR(100) NOT NULL,
    serial_number VARCHAR(255) UNIQUE,
    purchase_date DATE,
    warranty_expiry DATE,
    department_id INTEGER REFERENCES departments(id),
    user_id INTEGER REFERENCES users(id),
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## การเขียนโค้ดและมาตรฐาน

### Coding Conventions

#### Frontend (React)
```javascript
// ✅ Component naming - PascalCase
const AssetManagementPage = () => {
  // ✅ Hook และ state - camelCase
  const [assetList, setAssetList] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  
  // ✅ Function naming - camelCase
  const handleAssetCreate = async (assetData) => {
    try {
      setIsLoading(true);
      const response = await assetService.createAsset(assetData);
      
      // ✅ User message - ภาษาไทย
      showSuccessMessage('สร้างทรัพย์สินสำเร็จ');
    } catch (error) {
      // ✅ Error message - ภาษาไทย
      showErrorMessage('ไม่สามารถสร้างทรัพย์สินได้');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="asset-management-container">
      {/* ✅ UI Text - ภาษาไทย */}
      <h1 className="page-title">จัดการทรัพย์สิน IT</h1>
      <Button onClick={handleAssetCreate}>
        เพิ่มทรัพย์สินใหม่
      </Button>
    </div>
  );
};
```

#### Backend (Express)
```javascript
// ✅ Route definition - plural endpoint
router.get('/api/assets', authenticateToken, async (req, res) => {
  try {
    // ✅ Variable naming - camelCase
    const assetList = await Asset.findAll();
    
    // ✅ Response - JSON format พร้อมข้อความไทย
    res.status(200).json({
      success: true,
      message: 'ดึงข้อมูลทรัพย์สินสำเร็จ',
      data: assetList
    });
  } catch (error) {
    // ✅ Error logging - English
    console.error('Failed to fetch assets:', error);
    
    // ✅ Error response - ข้อความไทย
    res.status(500).json({
      success: false,
      message: 'ไม่สามารถดึงข้อมูลทรัพย์สินได้',
      error: error.message
    });
  }
});
```

### File Naming Conventions
- **Components**: PascalCase (เช่น `AssetCard.jsx`, `UserProfile.jsx`)
- **Pages**: PascalCase (เช่น `AssetListPage.jsx`, `DashboardPage.jsx`)
- **Services**: camelCase (เช่น `assetService.js`, `authService.js`)
- **Utilities**: camelCase (เช่น `dateUtils.js`, `formatUtils.js`)
- **Routes**: camelCase (เช่น `assets.js`, `users.js`)

## ความปลอดภัย (Security)

### Authentication & Authorization
```javascript
// ✅ JWT Token verification middleware
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; // Bearer TOKEN
  
  if (!token) {
    return res.status(401).json({
      success: false,
      message: 'ไม่พบ token การยืนยันตัวตน'
    });
  }
  
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({
        success: false,
        message: 'token ไม่ถูกต้องหรือหมดอายุ'
      });
    }
    req.user = user;
    next();
  });
};
```

### Password Security
```javascript
// ✅ Password hashing ด้วย bcrypt
const bcrypt = require('bcrypt');
const saltRounds = 12;

const hashPassword = async (plainPassword) => {
  return await bcrypt.hash(plainPassword, saltRounds);
};

const verifyPassword = async (plainPassword, hashedPassword) => {
  return await bcrypt.compare(plainPassword, hashedPassword);
};
```

### Input Validation & Sanitization
```javascript
// ✅ Input validation middleware
const validateAssetInput = (req, res, next) => {
  const { assetName, assetType, serialNumber } = req.body;
  
  // ตรวจสอบข้อมูลที่จำเป็น
  if (!assetName || !assetType) {
    return res.status(400).json({
      success: false,
      message: 'กรุณากรอกชื่อทรัพย์สินและประเภททรัพย์สิน'
    });
  }
  
  // ทำความสะอาดข้อมูล (sanitize)
  req.body.assetName = assetName.trim();
  req.body.assetType = assetType.trim();
  req.body.serialNumber = serialNumber ? serialNumber.trim() : null;
  
  next();
};
```

### Environment Variables
```bash
# ✅ ข้อมูลสำคัญใน .env เท่านั้น
DATABASE_URL=postgresql://username:password@localhost:5432/itam_db
JWT_SECRET=your-super-secret-jwt-key-here
JWT_EXPIRE_TIME=24h
BCRYPT_SALT_ROUNDS=12
NODE_ENV=development
PORT=5000
```

## การพัฒนาและ Deployment

### Development Setup
```bash
# ติดตั้ง dependencies
npm install

# เริ่มต้น development servers
npm run dev          # เริ่ม frontend (Vite)
npm run server       # เริ่ม backend (Express)

# หรือใช้ Docker Compose
docker-compose up -d
```

### Docker Configuration
```dockerfile
# ✅ Multi-stage build สำหรับ Frontend
FROM node:18-alpine AS frontend-build
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# ✅ Production image
FROM nginx:alpine
COPY --from=frontend-build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
```

```dockerfile
# ✅ Backend Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
USER node
EXPOSE 5000
CMD ["npm", "start"]
```

### Database Migration
```sql
-- ✅ ติดตาม migration ใน migrations/ directory
-- migrations/001_create_users_table.sql
-- migrations/002_create_assets_table.sql
-- migrations/003_create_departments_table.sql
```

## การทดสอบและ Quality Assurance

### Testing Strategy
```javascript
// ✅ Unit tests สำหรับ components
import { render, screen, fireEvent } from '@testing-library/react';
import AssetCard from '../components/AssetCard';

test('แสดงข้อมูลทรัพย์สินถูกต้อง', () => {
  const mockAsset = {
    id: 1,
    assetName: 'Computer-001',
    assetType: 'desktop'
  };
  
  render(<AssetCard asset={mockAsset} />);
  
  expect(screen.getByText('Computer-001')).toBeInTheDocument();
  expect(screen.getByText('desktop')).toBeInTheDocument();
});
```

### API Testing
```javascript
// ✅ API endpoint tests
const request = require('supertest');
const app = require('../server/index');

describe('Assets API', () => {
  test('GET /api/assets ควรคืนข้อมูลทรัพย์สิน', async () => {
    const response = await request(app)
      .get('/api/assets')
      .set('Authorization', `Bearer ${validToken}`)
      .expect(200);
      
    expect(response.body.success).toBe(true);
    expect(response.body.message).toBe('ดึงข้อมูลทรัพย์สินสำเร็จ');
    expect(Array.isArray(response.body.data)).toBe(true);
  });
});
```

## การใช้งาน Git และ Workflow

### Branch Naming
- **Feature branches**: `feature/asset-management`, `feature/user-authentication`
- **Bug fixes**: `bugfix/asset-form-validation`, `bugfix/login-error`
- **Hotfixes**: `hotfix/security-patch`, `hotfix/database-connection`

### Commit Messages
```bash
# ✅ ข้อความ commit เป็นภาษาไทย
git commit -m "เพิ่มฟีเจอร์การจัดการทรัพย์สิน IT"
git commit -m "แก้ไขบัคการตรวจสอบสิทธิ์ผู้ใช้"
git commit -m "ปรับปรุงประสิทธิภาพการค้นหาทรัพย์สิน"

# ❌ ข้อความ commit เป็นภาษาอังกฤษ
git commit -m "Add asset management feature"
```

## การ Deploy และ Production

### Environment Setup
```yaml
# docker-compose.prod.yml
version: '3.8'
services:
  frontend:
    build: 
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "80:80"
    depends_on:
      - backend
      
  backend:
    build:
      context: ./server
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=${DATABASE_URL}
      - JWT_SECRET=${JWT_SECRET}
    depends_on:
      - database
      
  database:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=itam_production
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      
volumes:
  postgres_data:
```

### Monitoring และ Logging
```javascript
// ✅ Application logging
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' })
  ]
});

// การใช้งาน logging
logger.info('ผู้ใช้เข้าสู่ระบบสำเร็จ', { userId: user.id, timestamp: new Date() });
logger.error('เกิดข้อผิดพลาดในการเชื่อมต่อฐานข้อมูล', { error: error.message });
```

## การ Troubleshooting และ Debug

### Common Issues
1. **Database Connection Issues**
   ```bash
   # ตรวจสอบการเชื่อมต่อ PostgreSQL
   psql $DATABASE_URL -c "SELECT 1;"
   ```

2. **JWT Token Issues**
   ```javascript
   // ตรวจสอบ JWT token validity
   const jwt = require('jsonwebtoken');
   try {
     const decoded = jwt.verify(token, process.env.JWT_SECRET);
     console.log('Token valid:', decoded);
   } catch (error) {
     console.log('Token invalid:', error.message);
   }
   ```

3. **Frontend Build Issues**
   ```bash
   # ล้าง cache และ rebuild
   rm -rf node_modules
   rm package-lock.json
   npm install
   npm run build
   ```

## Performance Optimization

### Database Optimization
```sql
-- ✅ สร้าง indexes สำหรับ queries ที่ใช้บ่อย
CREATE INDEX idx_assets_department_id ON assets(department_id);
CREATE INDEX idx_assets_status ON assets(status);
CREATE INDEX idx_assets_created_at ON assets(created_at);

-- ✅ Pagination สำหรับข้อมูลจำนวนมาก
SELECT * FROM assets 
WHERE department_id = $1 
ORDER BY created_at DESC 
LIMIT $2 OFFSET $3;
```

### Frontend Optimization
```javascript
// ✅ React.memo สำหรับ components ที่ไม่เปลี่ยนแปลงบ่อย
const AssetCard = React.memo(({ asset, onEdit, onDelete }) => {
  return (
    <div className="asset-card">
      <h3>{asset.assetName}</h3>
      <p>{asset.assetType}</p>
    </div>
  );
});

// ✅ useMemo สำหรับ expensive calculations
const filteredAssets = useMemo(() => {
  return assets.filter(asset => 
    asset.assetName.toLowerCase().includes(searchTerm.toLowerCase())
  );
}, [assets, searchTerm]);
```

## สรุปแนวทางการพัฒนา

1. **ใช้ภาษาไทยสำหรับผู้ใช้**: UI, messages, comments, documentation
2. **ใช้ภาษาอังกฤษสำหรับโค้ด**: variables, functions, classes, files
3. **ตรวจสอบความปลอดภัย**: JWT auth, bcrypt, input validation
4. **ใช้ RESTful APIs**: HTTP verbs, plural endpoints, JSON responses
5. **ทำ testing อย่างครบถ้วน**: unit tests, integration tests, API tests
6. **ใช้ Docker**: containerization, multi-stage builds
7. **Monitor และ log**: application performance และ errors

โปรเจกต์นี้มุ่งเน้นการสร้างระบบจัดการทรัพย์สิน IT ที่มีประสิทธิภาพ ปลอดภัย และใช้งานง่ายสำหรับหน่วยงานราชการไทย