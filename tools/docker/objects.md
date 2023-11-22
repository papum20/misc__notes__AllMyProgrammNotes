# OBJECTS

## Dockerfile
  
### KEYWORDS 

`ARG arg_name` : specify arg used in builing image  
*	note: need to specify in order to pass and use it

`CMD cmd` : command executed at startup (gets pid 1)  
*	`cmd` : if inline, spawns a shell which executes it
	*	e.g.: `CMD node server.js` : 
*	`["cmd", "arg1"]` : if as array, just launch it 
	*	e.g.: `CMD ["node", "server.js"]` : 

`COPY src dst` : from local `src` to `dst` in container  
*	`--from IMG` : copy from image to current (useful when multi-stage dockerfile)
*	`--chown=USER:GROUP` : change owner to

`FROM image` : starting image (see basics->layers)  
*	if img is already installed (like a cache), use it, otherwise will download  
*	`FROM image AS name` : you can refer it later as name 
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
			args:	# arguments to ue in build (in Dockerfile); they must be specified in the Dockerfile with `ARG arg_name`
				arg1: val1
		deploy:
			resources:
				limits:		# resources usage limits
					cpus: '0.5'
					memory: 512M	# megabytes
		env_file:
		-	PATH/TO/ENVFILE
		environment:
		-	ENV_VARS
		networks:
			NETWORK_NAME:
				# top-level `networks`` must also specify ipam to allow static ip assigning
				# and must also include used ips in its range of usable oès
				ipv4_address: 0.0.0.0
				ipv6_address: 0:0:0:0::0
		ports:
		-	LOCAL:CONTAINER	# ports mapping
		volumes:
		-	VOLUME_NAME:VOLUME/PATH

networks:
	NETWORK_NAME:
		name: NAME
		attachable: true|false # new containers can attach
		external: true|false # if true is defined outside (i.e. not created at docker compose up)
		internal: true|false # if true, network is isolated
		labels:
			LABEL1: VAL
		ipam:
			driver: default
			config:
			-	subnet: 172.28.0.0/16
				ip_range: 172.28.5.0/24
				gateway: 172.28.5.254 # gateway is your machine: in a bridge type driver the gateway adderess is reserved to it for communicating with containers
				aux_addresses:
					host1: 172.28.1.5
					host2: 172.28.1.6
					host3: 172.28.1.7
			options: # driver-specific
				foo: bar
				baz: "0"

volumes:
	VOLUME_NAME:
```  

