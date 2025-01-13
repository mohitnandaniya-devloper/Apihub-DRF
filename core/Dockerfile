FROM python:3.11-slim

# Set environment variable to ensure Python output is displayed in real-time
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /core

# Copy the requirements file into the container
COPY requirements.txt /core/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /core/

# Expose port 8000 for the Django application
EXPOSE 8000

# Run Django commands to prepare the database and start the server
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]


# --------------------------------------------    Production    --------------------------------------------


# # Use the official Python slim image
# FROM python:3.11-slim

# # Set environment variable to ensure Python output is displayed in real-time
# ENV PYTHONUNBUFFERED=1

# # Set the working directory inside the container
# WORKDIR /core

# # Install system dependencies for Python packages (if needed)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# # Copy the requirements file into the container
# COPY requirements.txt /core/

# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire project into the container
# COPY . /core/

# # Collect static files
# RUN python manage.py collectstatic --noinput

# # Expose port 8000 for the Django application
# EXPOSE 8000

# # Command to run database migrations and start the Gunicorn server
# CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn -w 4 -b 0.0.0.0:8000 core.wsgi:application"]
