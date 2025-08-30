# Stage 1: Build stage - ติดตั้ง Dependencies และ Build แอปพลิเคชัน
FROM node:18-alpine as builder

# ตั้งค่า working directory
WORKDIR /app

# คัดลอกไฟล์ package.json และ package-lock.json (ถ้ามี)
COPY package*.json ./

# ติดตั้ง dependencies
RUN npm ci --only=production

# คัดลอก source code ทั้งหมด
COPY . .

# Build แอปพลิเคชัน
RUN npm run build

# Stage 2: Production stage - รัน Nginx เพื่อ serve static files
FROM nginx:alpine

# คัดลอกไฟล์ build จาก stage 'builder'
COPY --from=builder /app/dist /usr/share/nginx/html

# คัดลอก nginx configuration (ถ้ามี)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# รัน nginx
CMD ["nginx", "-g", "daemon off;"]