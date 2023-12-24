# OBJECTS

## Objects

### class
`Mod(a, m)` : create class `a` mod `m`  
*	e.g.: 
	```
	a = Mod(2, 5)	# a = 2
	a**3			# a = 2**3 mod 5 = 3 
	```  

#### methods

`sqrt()` : self sqrt mod n  

### equation
Expression using numbers, operators, variables.  
e.g.: `x^2 + 2` :  

### variable
`var('x y...')` : create and return symbolic variables, with given names  
*	the variables is both returned and injected in the env

`var(['x', 'y', ...])` :  
`var('x', 'y', ...)` :  

## Fucntions

`factor(n)` : factorize n  
`crt(a,b,m,n)` : chinese remainder theorem, solve for `x=a mod m`, `x=b mod n`    
`crt(a:[], b:[])` : chinese remainder theorem, solve for `x=a_i mod b_i`  
`discrete_log(a, base:Mod)` : discrete log of `a` in `base`, where base is obtained with `Mod`  
`inverse_mod(a, m)` : inverse of `a` mod `m`, i.e. `pow(n,-1,mod)`  
`solve_mod(eqns,modulus)->List[]` : return solutions to modular equation  
`xgcd(a, b)->Tuple[g,s,t]` : return gcd and Bezout's coefficients  
