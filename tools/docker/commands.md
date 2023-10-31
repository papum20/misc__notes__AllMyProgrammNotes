# COMMANDS

## DOCKER    
`docker COMMAND` : (possible commands follow)   

`build PATH` : build image from dockerfile in `PATH`  
*	`-t TAG` : name it tag
*	`-f PATH` : (default `./Dockerfile`) use dockerfile `PATH`

`container inspect [NAME|ID]` : info (as json)  
*	`--format FORMAT` : filter only selected format
*	e.g.: get IPAddress, Name

`container ls` : list executing containers  
`container prune` : remove containers  
`docker images` : list images saved on local  
`exec ID CMD` : execute command `CMD` on container identifed by `ID`  
*	`-i` : interactive (i/o)
*	`-t` : allocate a (pseudo) terminal

`image prune` : remove images  
`ps -a` : list all containers, both executing and stopped  
`pull IMAGE` : download image from docker hub  
`rmi IMAGE` : delete image  
`run IMAGE` : run (new) container  
*	`--entrypoint CMD` : run container with entrypoint command  
*	`--rm` : rm container after  
*	`-i` : interactive
*	`-t` : allocate pseudo terminal
*	e.g.: `docker run -it ubuntu:20.04 bash` :  

`stop ID` : stop/remove container  
`system df` : disk usage of images and containers  
`volume prune` :    
  
  
## DOCKER-COMPOSE 
`docker-compose COMMAND` : (possible commands follow)  

`down` : stop and remove containers and networks  
`logs -f [service_name]` : show log  
`start -d` : start services  
`stop` : stop services  
`up -d` : build images, execute services  
  

