# EXAMPLES

backup volume :  
*	src: https://stackoverflow.com/a/69292739
```bash
docker cp --archive CONTAINER:/MOUNT_POINT_OF_VOLUME ./LOCAL_FOLDERdocker run -v ./LOCAL_FOLDER:/MOUNT_POINT_OF_VOLUME some_image
```

Set permissions for bind mount volumes : 
*	useful especially when migrating volumes (and it will give permission problems)
*	src: my own solution
*	`Dockerfile` :
	```Dockerfile
	ARG LOCAL_GID

	# change volumes permissions
	USER root
	RUN groupadd -g ${LOCAL_GID} docker
	RUN usermod -aG docker user_name

	USER user_name # set proper user not to run as root
	```
*	`Dockerfile` : alternative if missing `groupadd` and `usermod`
	```Dockerfile
	ARG LOCAL_GID

	# change volumes permissions
	USER root
	RUN addgroup -g ${LOCAL_GID} docker
	RUN addgroup user_name docker

	USER user_name # set proper user not to run as root
	```
*	`docker-compose.yml` :  
	```yml
	service:
		build:
			context: ...
			dockerfile: ...
			args:
				LOCAL_GID: ${LOCAL_DOCKER_GID}
	```
*	`.env` :  
	```.env
	LOCAL_DOCKER_GID=997 # your docker gid, got with 'id`
	```