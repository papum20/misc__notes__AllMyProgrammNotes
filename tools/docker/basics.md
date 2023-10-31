# BASICS
  
## Image
A configuration for an os.  
  
## Container
Instance of image.  

### Logs

Logs (showed with `docker logs CONTAINER`) are collected from container's stdout and stderr.  
So to write container's error to docker logs you should redirect to -> `/dev/stderr`/`/dev/stdout`.  

## Intermediate container
After each `dockerfile` command, a copy of the last container used is saved as an image on a new _layer_.
Each command is executed in an intermediate container, built from the last image.  
The first image is used specified by `FROM image`.  

## README.md  
*	[README.md](./README.md)  

