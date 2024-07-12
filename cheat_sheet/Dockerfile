# Use Python as base image
FROM python:latest

# Add user app and switch to this user
RUN adduser app
USER app

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file from host to the container with app user as owner
COPY --chown=app requirements.txt requirements.txt

# Upgrade pip and install dependencies
RUN pip install --user --upgrade pip && \
    pip install --user --no-cache-dir -r requirements.txt

# Copy the Project from Host Relative directory to Container's Working Directory with app user as owner
COPY --chown=app . .

# Add the user-specific bin directory to the PATH environment variable.
ENV PATH="/home/app/.local/bin:${PATH}"

# Expose port 8501 (default port for Streamlit apps)
EXPOSE 8501

# Run the Streamlit app
ENTRYPOINT [ "streamlit", "run" ]
CMD [ "app.py" ]