# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /proconnect_face_auth

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libgl1-mesa-glx \
    libgtk2.0-dev \
    && apt-get clean

COPY requirements.txt .
COPY . ./app
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8443 available to the world outside this container
EXPOSE 8443

# Run app.py when the container launches
# CMD ["python", "app.py"]
CMD ["gunicorn", "-b", "0.0.0.0:8443", "app.app:app"]
