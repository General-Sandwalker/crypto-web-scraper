FROM python:3.13-slim

WORKDIR /app

# Install system dependencies for psycopg2 and matplotlib and Kivy (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    python3-tk \
    tk \
    libgl1-mesa-glx \
    libgstreamer1.0-0 \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libgstreamer-plugins-base1.0-dev \
    libmtdev-dev \
    xclip \
    xsel \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Default command: run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]