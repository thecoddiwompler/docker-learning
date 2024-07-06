# Use Python as base image
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Install Git and clone the Streamlit roadmap app from GitHub
RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/streamlit/roadmap.git ./roadmap/

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 (default port for Streamlit apps)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "roadmap/streamlit_app.py"]