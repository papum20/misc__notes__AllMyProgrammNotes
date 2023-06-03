# OBJECTS

`Mod(a, m)` : create class `a` mod `m`  
*	e.g.: 
	```
	a = Mod(2, 5)	# a = 2
	a**3			# a = 2**3 mod 5 = 3 
	```  

`crt(a:[], b:[])` : chinese remainder theorem, solve for `a_i=m mod b_i`  
`discrete_log(a, base:Mod)` : discrete log of `a` in `base`, where base is obtained with `Mod`  
`inverse_mod(a, m)` : inverse of `a` mod `m`  
