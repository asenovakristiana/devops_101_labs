# Ensure WSL setup
* Start PowerShell terminal and run:
```powershell
wsl --version
```

* The expected output should be something like this:
```
WSL version: 2.3.26.0
Kernel version: 5.15.167.4-1
WSLg version: 1.0.65
MSRDC version: 1.2.5620
Direct3D version: 1.611.1-81528511
DXCore version: 10.0.26100.1-240331-1435.ge-release
Windows version: 10.0.22631.4317
```
**Note:** The version of WSL should be above 2.3. 

# Enable WSL systemd
WSL by default doesn't use systemd. However, we will need a docker daemon which is managed by systemd to continue with the next steps.
* Start ubuntu terminal and execute:
```bash
echo -e "[boot]\nsystemd=true" | sudo tee /etc/wsl.conf > /dev/null
```

# Shutdown WSL
* Open again the PowerShell terminal and run:
```powershell
wsl --shutdown
```
This will shutdown all the instance of WSL. This way when you run a new ubuntu terminal, it will start WSL again and it will load systemd.

# Install docker
https://www.cherryservers.com/blog/install-docker-ubuntu
* Start ubuntu terminal and execute:
```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl enable docker
sudo systemctl start docker
```

* To add the currently logged-in user in the docker group, use the usermod command. This will allow your user to interact with the docker daemon without sudo.
```bash
sudo usermod -aG docker $USER
newgrp
```

* Review if docker install properly and it running.
```bash
docker --version
sudo systemctl status docker
```

* The expected output should be similar to this:
```bash
Docker version 24.0.7, build 24.0.7-0ubuntu4.1
```

# Run hello-world Docker
* Run hello-world container
```bash
docker run hello-world
```

You should see a message from the container:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
For more examples and ideas, visit:
https://docs.docker.com/get-started/
```

# Working with images
* Pull an image
```bash
docker pull hello-world
```

* List images
```bash
docker images
```

* Remove an image
```bash
docker rmi hello-world
```

# Build your own image
We will build a docker image with a simple python app
* Enter the my-app directory
```bash
cd my-app
```

* Review the Dockerfile
```bash
cat Dockerfile
```

* Build image
```bash
docker build . -t my-app
```

* View image details
```bash
docker inspect my-app
```

# Run and manage containers
* Run docker container
```bash
docker run -p 8000:8000 -d --name my-app my-app
```
This will start a new container with name my-app and detach (-d). Docker will also map the host port 8000 to the container port 8000.

* List running containers
```bash
docker ps
```

* Review logs of my-app container
```bash
docker logs my-app -f
```

* Test connectivity to your app
```bash
curl http://localhost:8000
```

* Stop your container
```bash
docker stop my-app
```

* Start your container
```bash
docker start my-app
```

* Execute command from the container
```bash
docker exec my-app ps
```

* Execute interactive command or shell
```bash
docker exec -it my-app /bin/bash
```
**Note:** This command runs an interactive bash shell. It enables you to execute commands for troubleshooting purpose inside the container. If you want to terminate the interactive session, you can either execute exit command or click CTRL+d

* Remove your container 
```bash
docker rm my-app
```
**Note:** This command will return an error if the container is still in running state.

* Forcely remove the container
```bash
docker rm my-app --force
```

* Run docker container with environment_variable value
```bash
docker run -e MY_APP_ENV_VAR=Value -p 8000:8000 -d --name my-app my-app
```

* Check environment variable data
```bash
curl http://localhost:8000
```

* Remove current container
```bash
docker rm my-app --force
```

* Run a new docker container with mounted config file
```bash
docker run --mount type=bind,source=$(pwd)/../config.yaml,target=/app/config.yaml -p 8000:8000 -d --name my-app my-app
```

* Check config data
```bash
curl http://localhost:8000
```

* Cleanup
```bash
docker rm my-app --force
```

# Docker volumes
For this lab we will use a simple app with sqlite database. First we will run the container without a volume and we will see how our data will be lost when we remove the container. The second example will run the container with attached volume, then we will remove the container and create a new one to see that the data is available.

* Enter the my-app directory
```bash
cd my-data-app
```

* Build image
```bash
docker build . -t my-data-app
```

* Run a new container without attached volume
```bash
docker run -p 8000:8000 -d --name my-data-app my-data-app
```

* Add item using the API
```bash
curl -X 'POST' \
  'http://localhost:8000/items' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "This is my first item"
}'
```

* List item using the API
```bash
curl -X 'GET' \
  'http://localhost:8000/items' \
  -H 'accept: application/json'
```

* Now remove the container and create new one 
```bash
docker run -p 8000:8000 -d --name my-data-app my-data-app
```

* Run again list using the API
```bash
curl -X 'GET' \
  'http://localhost:8000/items' \
  -H 'accept: application/json'
```
There is no items because the data.db file was stored in the overlay layer of the container and with the remove of the container the data is also removed.

* Remove the container before the second experiment
```bash
docker rm my-data-app --force
```

* Create a new docker volume
```bash
docker volume create my-app-data-volume
```

* Run a new container with attached volume
```bash
docker run -p 8000:8000 -d --name my-data-app -v my-app-data-volume:/app/data my-data-app
```

* Add a new item using the API
```bash
curl -X 'POST' \
  'http://localhost:8000/items' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "This is my first item"
}'
```

* Remove the container and create a new one
```bash
docker rm my-data-app --force
docker run -p 8000:8000 -d --name my-data-app -v my-app-data-volume:/app/data my-data-app
```

* Run again list using the API
```bash
curl -X 'GET' \
  'http://localhost:8000/items' \
  -H 'accept: application/json'
```
Now you can see the added item from the first container. This is possible due to the fact that we use a persistent volume and not the overlay container layer. This is the proper way to use docker for applications that needs to store data.

* Cleanup
```bash
docker rm my-data-app --force
docker rmi my-data-app --force
docker volume remove my-app-data-volume
```

# Push images to registry
Currently your image lives only on your local system. Often you need to share your image with other people or systems. The process involves fews steps.

* Choose your registry
For some public projects, you will probably want to push your image to registries like DockerHub or GitHub Packages registry. For private projects, you will need to use your corporate registry or deploy such. 

* Login to registry
For this step will use the GitHub Packages registry. First you need to create a Personal Access Token (PAT) with the required scopes.
Create a Personal Access Token (PAT):

1. Go to [GitHub Developer Settings](https://github.com/settings/tokens/new).
2. Generate a new token (Classic Token) with the following scopes:
    - write:packages (to push packages)
    - read:packages (to pull packages)
3. Authenticate Docker
```bash
docker login ghcr.io
```
You will need to provide your GitHub username and the personal access token.

* Tag image
```bash
docker tag my-app ghcr.io/USERNAME/my-app:latest
```
Replace **USERNAME** with your personal GitHub account

* Push image
```bash
docker push ghcr.io/USERNAME/my-app:latest
```
Replace **USERNAME** with your personal GitHub account