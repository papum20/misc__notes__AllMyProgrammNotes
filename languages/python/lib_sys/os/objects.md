# OBJECTS  

  
`chdir(str PATH)` : cd  
`getcwd()` : get current working dir  
`list[str] listdir(str PATH)` : list of files in dir  
`rename(str SRC, str DST)` : rename  
`stat(PATH)` : stat struct
*	`.st_mode` : permissions, returned as int, to convert to octal
	*	e.g.: `oct(os.stat(FILE).st_mode)[-3:]` : get user,group,others rwx
*	`.st_size` : size in B

`Generator walk(TOP)` : all files in path tree starting at TOP, returned as list of triples `[ROOT,DIRS,FILES]`  
  
## README.md  
*	[README.md](./README.md)  

## os.path  
`abspath(PATH)` : absolute path  
`bool exists(str PATH)` : true if PATH exists  
`isDir(PATH)` :    
`getSize(PATH)` :  
