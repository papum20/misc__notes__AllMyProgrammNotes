# BASICS

## Execution

**JVM** : can be compiled to Java bytecode and run on the JVM  
**REPL** : **Read-Eval-Print Loop** - give instructions and eval in real time
*	imperative languages : work on a memory, on which a program's instructions work in order to obtain its final state, as output
*	functional languages : work on an environment (**REPL**), where definitions can be added


## Expressions

### Evaluation

expression evaluation : 
*	**Call-by-value** : **CBV** - evaluate each term, from left to right
	*	a variable name is replaced with its value
	*	operators are applied
	*	primitive terms can't be further evaluated
	*	e.g.: `FUNCTION(EXPRESSION)` : evaluate `EXPRESSION` before call
*	**Call-by-name** : **CBN** - delay evaluation until value is needed
	*	pro: a function's param isn't evaluated, if not used
		*	e.g.: when there are if branches
*	if there are no **side effects**, both evaluations terminate (otherwise **CBV** may not)
	*	`(CBV ends => CBN ends) && not (CBN ends => CBV ends)`
	*	e.g.: a param evaluation doesn't end
*	obs: an expression evaluation may not terminate
	*	e.g.: `def loop: Int = loop+1` : infinite loop
*	dflt: **CBV**
	*	**CBN** with `=> TYPE` 

**scoping** :
*	**static(/lexical)** : evaluating with environment at def time

### Functions

function :
*	can be nested, i.e. they don't have to be all at top level
*	**tail recursion** : optimized, in Scala

**higher-order** : if takes as arg or returns another function  

### Types

**class** : 
*	can inherit 1 parent class, multiple **trait**s
*	a **trait** inherited later will override conflicting declarations (methods etc.) inherited before
*	**super** : refer to parent class
	*	**dynamic binding** : 
		*	if **super** used in a **trait**, will work, for a class, considering its parent class as super
*	**covariance** : if `A <: B`, then `C[A] <: C[B]`
	*	**Scala** has a syntax to specify it
*	**contravariance** : if `A <: B`, then `C[B] <: C[A]`

**nothing** : type of expression that doesn't return a value, but throws an **exception**  
*	e.g.: `def e = throw new Exception("error")` : `e` has type `Nothing`
*	subtype of all others
	*	e.g.: int, class...

**type inference module** : 

