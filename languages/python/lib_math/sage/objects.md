# OBJECTS

## elliptic curves
`ecm.PROP` : pkg `ecm`  

`factor(N)` : return a (probable) prime factorization with elliptic curve factorization method  
`find_factor(N)` : return 2 factors of `N`, of which one is prime  

## equations
`solve(eqns:List[equation],vars...)->List[]` : return solutions to equations, using variables `vars`  
*	e.g.: `var('x y')` : can use `x`, `y` as vars

### modular
`crt(a,b,m,n)` : chinese remainder theorem, solve for `x=a mod m`, `x=b mod n`    
`crt(a:[], b:[])` : chinese remainder theorem, solve for `x=a_i mod b_i`  

`solve_mod(eqns,modulus)->List[]` : return solutions to modular equation  

### (Equation)
Expression using numbers, operators, variables.  
e.g.: `x^2 + 2` :  

### Matrix
`Matrix(rows: List[float])` : matrix  
*	e.g.:
		```python
		>>> matrix([[1,2],[3,4]])
		[1 2]
		[3 4]
		```
`Matrix(finite_ring, rows)` : matrix in finite field/ring  
*	e.g.: `Matrix( GF(5), [[1,2],[3,4]] )` :  

### (Variable)
`var('x y...')` : create and return symbolic variables, with given names  
*	the variables is both returned and injected in the env

`var(['x', 'y', ...])` :  
`var('x', 'y', ...)` :  

## factors
`factor(n)` : factorize n  
`xgcd(a, b)->Tuple[g,s,t]` : return gcd and Bezout's coefficients  

## modular arithmetics
`discrete_log(a, base:Mod)` : discrete log of `a` in `base`, where base is obtained with `Mod`  
`inverse_mod(a, m)` : inverse of `a` mod `m`, i.e. `pow(n,-1,mod)`  

### EllipticCurve
`E = EllipticCurve(ring: Ring, invariants: List[float])` :  
*	`ring` : a commutative ring (but most functionalities need field)
	*	can be omitted
*	`invariants` : `[a1,a2,a3,a4,a6]` or `[a4,a6]`, from `y**2+a1 xy+a3 y = x**3+a2 x**2+a4 x+a6`

`E(x,y)` : get point in `E` (`EllipticCurvePoint`)  
`E.base_extend(F)` : return with changed field as base  
`E.defining_polynomial()` : polynomial using projective coordinates (points `x`,`y`,`z`)
*	with `z=1` it's the form with `x`,`y`, with `z=0` it's the solution at infinity

`E.order()` :  
`E.set_order()` : set if known  
*	good for performance?

#### EllipticCurvePoint

`discrete_log(Q:EllipticCurvePoint)` : for `P`, get `n` s.t. `P=nQ`  
`xy()` : get `(x,y)`  

### finite fields
`GF(dimension: int)` : finite field of `dimension`  
`GF(dimension: int, s: string)` : ??  
*	e.g.:
		```python
		>>> k = GF(9, 'a')
		>>> for i,x in enumerate(k):  print("{} {}".format(i, x))
		0 0
		1 a
		2 a + 1
		3 2*a + 1
		4 2
		5 2*a
		6 2*a + 2
		7 a + 2
		8 1
		```

### finite rings
`IntegerModRing(n)` :  
`Integers(n)` : (same)  

### Mod
`M = Mod(a, m)` : create class `a` mod `m`  
*	e.g.: 
	```
	a = Mod(2, 5)	# a = 2
	a**3			# a = 2**3 mod 5 = 3 
	```  

`M.sqrt()` : self sqrt mod n  
