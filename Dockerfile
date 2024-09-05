# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv and dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


# Run database migrations and import data
RUN  python manage.py migrate
RUN  python manage.py import_imdb  

# Expose the port the app runs on
EXPOSE 8000

# Run the server and gRPC service
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000 "]