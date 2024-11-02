# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variables to prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies for audio processing and general utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    libsndfile1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "run.py"]
