# SYNTAX

## README.md  
*	[README.md](./README.md)  

## VARIABLES
*	everything is a variable (variables, functions, types, operators...)
### variable declaration
`varName :: Type1 -> Type2 -> ...` : 
### variable definition
`varName arg1 arg2 = EPRESSION` : 
*	first letter lowercase
### value assignment
`varName <- EXPR1` : assign EXPR1 value to varName  
### LAMBDA-ABSTRACTION
`lambdaName = EXPR -> VAL` : lambda function, replace EXPR with VAL  
*	e.g.: `plusOne = \x -> x + 1` : 

---

## TYPES
*	first letter uppercase

### type variable
first letter lowercase

### ALGEBRAIC DATA TYPE
`data TypeName arg1 arg2 = Constructor1 arg1 | Constructor2 arg2` :   
*	`TypeName` = type-constructor  
*	`Constructor1`, `Constructor2` = data-constructor  
```
data TypeName arg1 = 
	TypeName
		{ var1 :: type1
		, var2 :: type2
		...
		, var3 :: arg1
		}
```
*	`arg1` = "similiar to a template"  

### TYPE ALIAS
`type TypeName arg1 = ExistingType arg1` : like typedef  
### TYPE-CLASS
```
class ClassName arg1 where
	(OP1) :: arg1 -> ...
	(OP2) :: ...
	(OP2) arg1 ... = EXPR1
```
*	declares/defines its operators  
	*	(to define later, in instance, if only declared);  
*	OP2 has both decaration and "default" definition (valid if not defined later)  
### INSTANCE
```
data TypeName = EXPR1 | EXPR2
instance ClassName TypeName where
	(OP1) EXPR1
	(OP1) EXPR2
```
*	ClassName referring to previous example, of type-classes;  
*	defining 2 cases for OP1  

## STATEMENTS
#### concatenation
```
do
	EXPR1
	...
```
*	evaluate expressions in order  
#### let ... in
`let EXPRESSION1 in EXPRESSION2` :
*	evaluate to EXPR2, in environment EXPR1  
*	EXPR1 only evaluated at call  
	*	(lazy language)
	*	(difference from do)  
#### if-then-else
```
if EXPR1
then EXPR2
else EXPR3
```
#### pattern matching
```
varName arg1 arg2 = 
	case arg1 of
		PATTERN1 -> EXPR1
		PATTERN2 -> EXPR2
		...
```


## OPERATORS
#### bind
`>>=` : like concatenation:
*	compute expression, use result for next one  
#### 
`>>` : like bind, but discard computed expression  

## TYPES
`()` : singleton
#### function
`->`

