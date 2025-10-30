FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (for better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entrypoint script first and fix permissions
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh && \
    # Convert to Unix line endings just in case
    sed -i 's/\r$//' entrypoint.sh

# Copy only the necessary Python files
COPY app.py .

# Create flag directory with proper permissions
RUN mkdir -p /flag && \
    chmod 777 /flag

EXPOSE 5000

# Use entrypoint script
ENTRYPOINT ["./entrypoint.sh"]
