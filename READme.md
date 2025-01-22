# Docker Cheat Sheet

This cheat sheet covers commonly used Docker commands for managing containers and images.

## Basic Commands

- **docker run [image_name]**
  - Create and run a Docker container by pulling the image from DockerHub or local registry.

- **docker run [image_name] [command]**
  - Override the default command of the image and run the given command instead.

- **docker run --name=[container_name] [image_name]**
  - Create and run a Docker container with a custom name.

## Container Lifecycle

- **docker create [image_name]**
  - Create a Docker container from the given image.
  
- **docker start [container_id]**
  - Run or restart a stopped container in the background.

- **docker start -a [container_id]**
  - Run or restart a stopped container and print its logs.

- **docker restart [container_id]**
  - Restart a running or stopped container.

- **docker stop [container_id]**
  - Stop a running container gracefully (SIGTERM).

- **docker kill [container_id]**
  - Forcefully kill a running container (SIGKILL).3

- **docker ps**
  - List all running containers.

- **docker ps -a**
  - List all containers (including stopped ones).

- **docker rm [container_id]**
  - Remove a stopped container.

- **docker system prune**
  - Delete all stopped containers and clear the image cache.

## Logging and Debugging

- **docker logs [container_id]**
  - Fetch the logs of a container without restarting it.

- **docker exec -it [container_id] [command]**
  - Execute a command inside a running container.

- **docker exec -it [container_id] sh**
  - Open an interactive shell session inside a running Docker container.

## Image Management

- **docker build .**
  - Build an image from a Dockerfile in the current directory.

- **docker build -t [dockerid]/[image_name]:[tag] .**
  - Build an image from a Dockerfile with a custom name and tag. If no tag is specified, the default tag would be latest.

- **docker tag [existing_image_name] [new_image_name]**
  - Tag an existing image with a new name.

- **docker push [image_name]**
  - Push an image to DockerHub.

- **docker rmi [image_name]**
  - Remove a specific Docker image.

- **docker rmi $(docker images -q)**
  - Remove all Docker images.

## Networking and Ports

- **docker run -p [port_on_local]:[port_inside_container] [image_name]**
  - Create and run a Docker container with port forwarding.

## Volume Management

- **docker volume create [volume_name]**
  - Create a named Volume.

- **docker volume ls**
  - List all the Volumes.

- **docker inspect [volume_name]**
  - Inspect the Volume.

- **docker run rm [volume_name]**
  - Remove the Volume.

- **docker run -d --mount type=volume,src=[volume_name],target=[target_path] [image_name]**
  - Run a container with a mounted volume. The tag -d specifies that the container would run in detached mode. The [target_path] is the path inside the container which needs to be persisted in the volume.

## Bind Mount

- **docker run -d --mount type=bind,src='[host_path]',target='[container_path]' [image_name]**
  - Run a container with a bind mount. Do give absolute path for host and target both.

## Miscellaneous

- **docker cp [source_path] [container_name]:[container_path]**
  - Copy file(s) from source path to container path inside the container.

- **docker cp [container_name]:[container_path] [destination_path]**
  - Copy file(s) from container to Host machine.