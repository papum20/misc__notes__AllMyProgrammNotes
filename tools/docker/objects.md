# OBJECTS

## Dockerfile
  
### KEYWORDS 

`CMD cmd` : command executed at startup  
`CMD [cmd1, cmd2]` : list of commands to exec  
`COPY src dst` : from local `src` to `dst` in container  
ENTRYPOINT [“cmd1”, …] :   
`FROM image` `: starting image (see basics->layers)  
*	if img is already installed (like a cache), use it, otherwise will download  
*	e.g.: `FROM docker.io/python:3.9.5-alpine` :  
*	e.g.: `FROM ubuntu:20.04` :  

`ENV var val` : exec command `env`, to set env var to val
*	e.g.: `ENV PATH /app/node_modules/.bin:$PATH`
*	e.g.: `ENV TZ=Europe/Rome`

`RUN cmd` : run command on a terminal in container  
`SHELL shell` : set shell to `shell` executable  
`SHELL ["shell", "arg1"]` : with args  
*	e.g.: `SHELL ["/bin/bash", "-c"]` : 

`WORKDIR path` : `cd path`  


## docker-compose.yml


```yml
version: VERSION # `docker-compose` version (version of file language, not command)  

services:
	SERVICE_NAME:
		container_name: NAME
		image: IMAGE	# build from image, no dockerfile
		tty: true
		restart: unless-stopped
		build:
			context: ./PATH/
			dockerfile: ./PATH/TO/FILE
		deploy:
			resources:
				limits:		# resources usage limits
					cpus: '0.5'
					memory: 512M	# megabytes
		env_file:
		-	PATH/TO/ENVFILE
		environment:
		-	ENV_VARS
		ports:
		-	LOCAL:CONTAINER	# ports mapping
		volumes:
		-	VOLUME_NAME:VOLUME/PATH

volumes:
	VOLUME_NAME:
```  

