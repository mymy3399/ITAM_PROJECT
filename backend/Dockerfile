# Stage 1: Build stage - ติดตั้ง Dependencies
FROM python:3.10-slim as builder

# ตั้งค่า working directory
WORKDIR /app

# คัดลอกไฟล์ requirements.txt เข้าไปใน container
COPY requirements.txt .

# ติดตั้ง Python libraries ที่จำเป็น
# --no-cache-dir เพื่อไม่ให้เก็บ cache, ทำให้ image เล็กลง
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final stage - รันแอปพลิเคชัน
FROM python:3.10-slim

# ตั้งค่า working directory
WORKDIR /app

# คัดลอก Python libraries ที่ติดตั้งไว้จาก stage 'builder'
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# คัดลอก source code ของแอปพลิเคชันเข้าไป
COPY . .

# Expose port 8000 เพื่อให้สามารถเข้าถึง API จากภายนอก container ได้
EXPOSE 8000