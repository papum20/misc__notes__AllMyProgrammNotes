# SYNTAX

## VARIABLES
`VAR_NAME: TYPE` : assign TYPE to VAR_NAME 

## OPERATORS
`arg!` : (in expression) indicate arg is always defined  
`arg?` : (in expression) indicate arg could be undefined  

## KEYWORDS
### TYPES
`type Name` : declare type  
`interface Name` : declare interface (generic type)  
```
interface Name {
	field1: type1,
	...
	[fieldX: typeX]: any,
} 
```
*	`[fieldX: typeX]: any` : any other args  

`declare` : ??  
*	e.g.: use interfce merging for redefining SessionData  
```
		declare module "express-session" {
			interface SessionData {
				userId: mongoose.Types.ObjectId;
			}
		}
```  
  
`asserts` : in function return type declaration, check condition before return (else throw error)   
*	e.g.: `function(): asserts COND` :  

`is` : compare types  
*	e.g.: `var is NonNullable<T>` : true if var (of type T) is non null  

`instanceof` : if var instance of type  


## CLASSES
`class` :  
`extends` :  

`this` :  
`constructor` : constructor object  
`constructor() {}` : constructor declaration  
`this.constructor.FIELD1` : access constructor field (i.e. field at construction)  
`super` : superclass  

`new` :  