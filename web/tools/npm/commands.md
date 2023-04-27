# COMMANDS

## README.md  
*	[README.md](./README.md)  

## COMMANDS
// format: `npm COMMAND ARGS`
`audit` : check deps  
*	e.g.: vulnerabilities  

`audit fix` : fix deps problems  
`init` : create `./package.json`  
*	`-y` : use default settings for metadata  

`install [PKG[@VERSION]]` : install package PKG;  
*	optionally specify version  
*	if no specified, install all deps in `package.json`  
*	`--save-dev` : for devDependencies  
*	`-D` : _alias_ for `--save-dev`
*	e.g.: `npm install --save-dev typescript` : used to install typescript  

`i PKG` : _alias_ for install  
`run CUSTOM-COMMAND` : execute custom command added to `"scripts"` in `package.json`  
`start` : short-hand, but not defined: user should define start as custom command  
`uninstall PKG` :  