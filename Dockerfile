# Use a lightweight Linux image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Install system essentials
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Snakemake and Pandas for workflow orchestration
RUN pip install --no-cache-dir snakemake pandas

# Copy project files into the container
COPY . .

# Default command when container runs
CMD ["bash"]
