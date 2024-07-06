# Pull the base image

FROM python:alpine3.12

# Specify Working Directory

WORKDIR /app

# Copy the files into Working directory

COPY ./ /app/

# Install the dependencies

RUN pip install -r requirements.txt

# Run

CMD [ "python", "main.py" ]