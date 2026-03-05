FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app.py .
COPY score.py .
COPY *.pkl . 

# Expose port (Flask default uses, assume 5000)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]