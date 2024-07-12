# Use Python as base image
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Install Git and clone the Streamlit Cheat Sheet app from GitHub
RUN apt-get update && \
    apt-get install -y git

# Copy the Project from Host Relative directory to Container's Working Directory
COPY ./ ./

# Copy the requirements file and install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 (default port for Streamlit apps)
EXPOSE 8501

# Run the Streamlit app
ENTRYPOINT [ "streamlit", "run" ]
CMD [ "app.py" ]