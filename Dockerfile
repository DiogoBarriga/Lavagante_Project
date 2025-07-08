FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ ./src/

# Copy project artifacts
COPY project-artifacts/ ./project-artifacts/

# Copy tools for automation and reporting
COPY tools/ ./tools/

# Copy configuration files
COPY config/ ./config/

# Set the command to run the application
CMD ["python", "src/dashboard/metrics-collector.py"]