# Docker Cheat Sheet

This cheat sheet covers commonly used Docker commands for managing containers and images.

## Basic Commands

- **docker run <image_name>**
  - Create and run a Docker container by pulling the image from DockerHub or local registry.

- **docker run <image_name> <command>**
  - Override the default command of the image and run the given command instead.

- **docker run --name=<container_name> <image_name>**
  - Create and run a Docker container with a custom name.

- **docker ps**
  - List all running containers.

- **docker ps -a**
  - List all containers (including stopped ones).

## Container Lifecycle

- **docker create <image_name>**
  - Create a Docker container from the given image.

- **docker start -a <container_id>**
  - Run or restart a stopped container and print its logs.

- **docker start <container_id>**
  - Run or restart a stopped container in the background.

- **docker stop <container_id>**
  - Stop a running container gracefully (SIGTERM).

- **docker kill <container_id>**
  - Forcefully kill a running container (SIGKILL).

- **docker rm <container_id>**
  - Remove a stopped container.

## Logging and Debugging

- **docker logs <container_id>**
  - Fetch the logs of a container without restarting it.

- **docker exec -it <container_id> <command>**
  - Execute a command inside a running container.

- **docker exec -it <container_id> sh**
  - Open an interactive shell session inside a running Docker container.

## Image Management

- **docker build .**
  - Build an image from a Dockerfile in the current directory.

- **docker build -t <dockerid>/<img_name>:<tag> .**
  - Build an image from a Dockerfile with a custom name and tag.

- **docker tag <existing_image> <new_image_name>**
  - Tag an existing image with a new name.

- **docker push <image_name>**
  - Push an image to DockerHub.

- **docker rmi <image_name>**
  - Remove a specific Docker image.

- **docker rmi $(docker images -q)**
  - Remove all Docker images.

## Networking and Ports

- **docker run -p <port_on_local>:<port_inside_container> <image_name>**
  - Create and run a Docker container with port forwarding.

## Volume Management

- **docker volume create <volume_name>**
  - Create a named volume.

- **docker run -d -p 3000:3000 --mount type=volume,src=<volume_name>,target=<target_path> <image_name>**
  - Run a container with a mounted volume.

## System Maintenance

- **docker system prune**
  - Delete all stopped containers and clear the image cache.