# SYNTAX

## Operators

`||` :
*	**short-circuit** : **CBN**

`&&` : 

## Statements

`if (COND) VAL1 else VAL2` : alternatives
*	if condition, but doesn't change program counter

## Variables

`_` : undefined variable  

`def VAR = VAL` : lazy definition  
*	`VAR` is assigned an expression
*	**static scoping** : the expression is evaluated with the environment at time of definition (so don't consider if variables used inside were re-defined later)

`val VAR = VAL` : eager  
*	`VAR` is assigned a value

`def FUN(VAR: TYPE) = EXPR` : function definition  
`def FUN(VAR1: TYPE1)(VAR2: TYPE2) = EXPR` : curried function    
*	`FUN(VAL1)(_)` : a partially applied function (only `VAL1` is given, `_` is a placeholder)

`def FUN(VAR: => TYPE) = EXPR` : **CBN** param  
`ARG => EXPR` : **anonymous function**  

`class C{}` : class definition  
`class C extends P{}` : inheritance or **trait** usage  
`class C extends P with T1 with T2{}` : multiple inheritance  
`class C[T]{}` : generic class  
`class C[+T]{}` : generic class, with **covariant** type parameter  
`class C[-T]{}` : **contravariant** type parameter  
