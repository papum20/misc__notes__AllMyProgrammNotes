# docker  
  
  
  
DOCKER :   
docker …  
build -t <image> : build image from dockerfile  
container ls : list executing containers  
docker images : list images saved on local  
exec -it <containerID> <cmd> : execute command  
ps -a : list executing / stopped containers  
pull <image> : download image from docker hub  
rmi <image> : delete image  
run <image>	: run container  
run –entrypoint <newcmd> <image> : run container,  
overwriting default entrypoints with newcmd  
stop <containerID> : stop/remove container  
  
  
  
DOCKER-COMPOSE :   
docker-compose …  
down : stop and remove containers and networks  
logs -f [service_name] : show log  
start -d : start services  
stop : stop services  
up -d : build images, execute services  
  
  
DOCKERFILE :   
MISC :  
\ : go to new line (in same line / command / keyword)  
  
KEYWORDS :  
CMD “cmd”	: command executed at startup  
COPY	from to : from pc to container  
ENTRYPOINT [“cmd1”, …] :   
FROM	“str”	: import (install)  
	e.g. docker.io/python:3.9.5-alpine  
RUN cmd	: run shell command(s)  
WORKDIR path: dir open at startup  
  
