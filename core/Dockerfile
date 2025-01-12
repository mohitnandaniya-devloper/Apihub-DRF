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


