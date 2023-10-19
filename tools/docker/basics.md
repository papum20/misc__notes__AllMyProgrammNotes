# BASICS
  
## Image
A configuration for an os.  
  
## Container
Instance of image.  

## Intermediate container
After each `dockerfile` command, a copy of the last container used is saved as an image on a new _layer_.
Each command is executed in an intermediate container, built from the last image.  
The first image is used specified by `FROM image`.  

## README.md  
*	[README.md](./README.md)  

