# Base image
FROM python:3.10-slim

# ตั้งค่า working directory
WORKDIR /app

# Install system dependencies สำหรับ network scanning
RUN apt-get update && apt-get install -y \
    nmap \
    iputils-ping \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# คัดลอกไฟล์ requirements.txt
COPY requirements.txt .

# ติดตั้ง Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอก source code
COPY . .

# รัน discovery service
CMD ["python", "src/main.py"]