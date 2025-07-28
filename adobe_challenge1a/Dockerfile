FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the solution code
COPY . .

# Create input and output directories
RUN mkdir -p /app/input /app/output

# Set the entry point for Challenge A
CMD ["python", "main.py"]