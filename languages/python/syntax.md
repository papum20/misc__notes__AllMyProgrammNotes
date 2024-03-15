# SYNTAX

## README.md  
*	[README.md](./README.md)  

## Modules
`import ...` :  
`__import__('MODULE')` : use module imported at the moment  
*	e.g.: `__import__('random').choice([1,2])` :  

## Classes

`_FIELD` : protected (intended like c++)  
`_CLASS_FIELD` : access class static protected field  
`_CLASS_METHOD` : access class static protected method  
`_CLASS__METHOD` : access class static private method  
`_METHOD` : protected  
`__FIELD` : private  
`__METHOD` : private  

### special methods

`__METHOD__` : special method already defined for operators
*	so you can override them
*	e.g.: `__add__()` : 

## Decorators

decorator : 
*	```py
	@DECORATOR
	def METHOD():
		...
	```

`@classmethod` :   
`@dispatchmethod(TYPES...)` : allow overloading  
*	without, when defining a new function, even with different params, would overwrite other definition
*	e.g.: `@dispatch(int, int)` : function accepts 2 int params

`@staticmethod` :   

## Operators

`*ITERABLE` : unpack iterable  
*	e.g.: `foo(*[1,2])` 