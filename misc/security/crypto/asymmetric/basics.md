# BASICS

rsa: 2048 bit  

## Diffie-Hellman

**diffie-hellman** : uses **discrete log** as hard problem.  
*	input:
	*	`p` : prime, defining the field `Fp` (multiplicative group)
	*	`g` : generator of `Fp`
	*	`a` : `a<p` - private key 
*	steps:
	*	`c=g**a mod p` : encrypted

**safe prime** : `p=2q+1` with `p`,`q` prime - avoid efficient attacks if not safe (_pohlig hellman_)  

### DLP

**Index Calculus** : best algo
*	`2048b` for `112b` security


## ECC

**Elliptic Curve Cryptography** : uses **scalar multiplication** as trapdoor f   
*	`E(Fp) = {(x,y) | x,y ∈ Fp, y**2 = x**3+ax+b} ∪ O` : uses an **elliptic curve** over a **finite field** `Fp`
	*	so it's a "curve modulo the characteristic `p`", a collection of points
		*	foreach point, `x`,`y` are integers in `Fp` 
		*	`a`,`b` are integers in `Fp`
	*	can be visualized as cartesian plane of integers with `x`,`y` in `[0,p[`
		*	obs: same cartesian math applies
	*	vulnerability: choose carefully (use already existing ones), or easy discrete log

**Elliptic Curve** : defined as set of solutions to a **Weierstrass equation** `E`, together with a **point at infinity** `O`   
*	**cardinality** : number of elements
*	**order** : number of elements (according to chatgpt, how many times an element can be summed to become again itself)
	*	`(p+1)−2sqrt(p) <= #E(F) <= (p+1)+2sqrt(p)` : _Hasse's theorem on elliptic curvers_ - order `#E(f)` in range
		*	src: https://math.stackexchange.com/questions/3166688/find-the-order-of-an-elliptic-curve/3988222#3988222?newreg=d78b4a040b644bbab2aabdced5dc8824

`Y**2 = X**3+aX+b` : **Weierstrass equation** -  

**point addition** : operator which takes two points on some curve and produces a third point on the curve  
*	`lambda = (y2-y1)/(x2-x1)`
	*	`lambda = (dE/dx)(dE/y) = (3x**2+a)/(2y)` : for tangent (if `x1=x2`)
*	`x3 = lambda**2-x1-x2`
*	`y3 = lambda(x1-x3)-y1`
*	steps:
	1.	given `P` and `Q`, track a line and find a third intersection `R=(x,y)` with `E`
		*	use the tangent if `P = Q`
	2.	`P+Q = R' = (x,-y)` - reflection of `R` over the x-axis
		*	`P+(-P) = O` : if there's no third intersection `R`
*	defines an **abelian group**
*	**point at infinity** : `O` - identity operator
	*	a single point located at the end of every vertical line at infinity
	*	properties:
		1.	`P+O = O+P = P`
		2.	`P+(−P) = O`
		3.	`(P+Q)+R = P+(Q+R)`
		4.	`P+Q = Q+P`
	*	`4a**3 + 27b**2 != 0` : `O` must satisfy this
		*	to ensure there are no singularities on `E`
*	**negate** : `-(x,y) = (x,-y)` 

**scalar multiplication** : repeated **point addition**
*	**Elliptic Curve Discrete Logarithm Problem** : (**ECDLP**) - hard to find `n` s.t. `Q = nP`
	*	complexity: `p**1/2`
*	e.g.: `Q = 2P = P+P` : 
*	**double-and-add** : 
	*	algo: for `n*P`, from lsb
		```python
		Q = P
		R = O
		while n > 0:
			if n%2 == 1:
				R = R + Q
			Q = Q + Q
			n = floor(n/2)
		return R
		```
	*	algo: from msb (msb-1)
		```python
		R = P
		for b in bits_representation(n)[1:]: # traversing from second MSB to LSB
			R = R + R
			if b == 1:
				R = R + P
		return R
		```
	*	vulnerability: side-channel; different time for different if branches
*	**double-and-add** : 
	*	algo: for `n*P` 
		```python
		R0 = O
		R1 = P
		for b in bit_representation(n):	# with msb on left
			if b == 0:
				R1 = R0 + R1
				R0 = R1 + R1
			else:
				R0 = R0 + R1
				R1 = R1 + R1
		return R0
		```
	*	if branches require same time

src:
*	https://curves.xargs.org/

### Key exchange

#### ECDH
`G` : generator point  
`nA` : private key of Alice  
`nB` : private key of Bob
`Qa` : `nA*G` - public key of Alice  
`Qb` : `nB*G` - public key of Bob  
`S` : `nA*Qb = nB*Qa = nA*nB*G` - shared secret  
`sha1(S.x)` : used as key  
*	e.g.: for **AES**
*	`x` is enough to know, since only 2 possible `y` associated

_cofactor_ : `h=E.order/n`
*	should be as small as possible
	*	e.g.: `1` ; `h<=4` ok

_domain parameters_ : `(p,a,b,G,n,h)`  
*	`a`,`b` : curve parameters
*	`n` : `G.order`


##### MOV attack

**MOV attack** : reduce _ECDLP_ to _DLP_, when _embedding degree_ `k` is small
*	e.g.: `k > 20` is secure; ed25519 has `k=8`
*	src: [https://risencrypto.github.io/WeilMOV/](https://risencrypto.github.io/WeilMOV/)
*	src: [https://crypto.stackexchange.com/a/1875/115423](https://crypto.stackexchange.com/a/1875/115423)
*	src: [www.github.com/papum20/tasks__security__cryptohack/elliptic/moving_exploit.py](www.github.com/papum20/tasks__security__cryptohack/elliptic/moving_exploit.py)  
*	steps:
	0.	given `E` in `F` (finite field in prime `p`), with (main) generator `G`, and _embedding degree_ `k` of `p` wrt `G.order()`; we want the discrete log `r` of `P=rQ` with base `Q`
		*	e.g.: `Q=G`
	1.	compute :
		*	the _extension field_ `Fpk` (over `p^k`)
		*	`Epk` on `Fpk`
		*	orders `m=#E`, `n=#Epk`
		*	note: since the m-_Torsion group_ of `E` is a subgroup of `Epk`, `m` divides `n` (lagrange's th)
	2.	Choose a random point `T` in `Epk` (and not in `E` ?? )
	3.	if `S=(n/m)*T == O`, choose another `T`, else it means `T` is a point of order `m`
	4.	compute _Weil Pairing_ values (in `Fpk`) :
		*	`u = em(Q,S)`
		*	`v = em(P,S) = em(rQ,S)`
		*	note: src #1 uses `S`, i (in my example) used `T`
		*	note: since the _Weil Pairing_ is _bilinear_ and `r` is a scalar, `v=em(P,S)^r`
	5.	we can solve the discrete log of `v` with base `u`
		*	(if `p^k` not too big ?? )

_linear map_ : `f1:V->W` (from `V` to `W`) if has properties
*	U,V,W vector spaces
*	{u,u1,u2∈U}
*	{v,v1,v2∈V}
*	a is a scalar
*	properties :
	*	f1(v1+v2)=f1(v1)+f1(v2)
	*	f1(a v)=a f1(v)
 
_bilinear map_ : `f2:V->W` 
*	properties :
	*	f2(u1+u2,v)=f2(u1,v)+f2(u2,v)
	*	f2(u,v1+v2)=f2(u,v1)+f2(u,v2)
	*	f2(a u,v)=a f2(u,v)=f2(u,a v)
*	note: then linear in u if v
 is fixed, and in v if u fixed.

_embedding degree_ : wrt `m`, smallest `k` s.t. `p^k%m = 1`  
_extension field_ : `Fpk` of `Fp`, on `p^k`, with `p` prime (??)  
_torsion point_ : `P` is `m`-_torsion_ if `mP=O`  
_torsion group_ : `m`-_torsion_ group is set of all `m`-_torsion_ points  
_Weil pairing_ : a _bilinear map_ from `E` to `F`  


##### ECDLP

best algo : `224b` for `112b` security

### Signing

#### ECDSA

_signing_ : 
*	`G` : generator
*	`n` : curve's order
	*	must be prime (...)
		*	src: wikipedia
*	`dA` : priv key
*	`Qa` : pub key
*	`m` : msg to send (sign)
*	steps:
	1.	`e = hash(m)`
	2.	`Ln = n.bit_length()`
	3.	`z = e[:Ln]` : (`Ln` leftmost bits)
	4.	`k` : selected cryptographically secure random from `[1,n-1]`
	5.	`(x1,y1) = k*G`
	6.	`r = x1 mod n` : if `0`, back to step 4
	7.	`s = k**-1 (z+r*dA) mod n` : if `0`, back to step 4
	8.	`(r,s)` : signature
		*	note: `(r,-s mod n)` : is also a valid signature
	*	note: `k` is a `nonce`, and can't be reused
*	vulnerability: reuse `k`, for 2 different `m1`,`m2`
	*	`dA = (s*k-z)/r`
	*	proof:
		1.	if `k=k1=k2` then `r=r1=r2=(k*G).x`
		2.	`si = (zi+r*dA)/k`
		3.	`s1-s2 = (z1-z2)/k`
		4.	`m = (z1-z2)/(s1-s2)`
		5.	get `dA = (s*k-z)/r`

_verification_ :
*	steps:
	0.	check :
		*	`Qa != O`
		*	`Qa` in `E`
		*	`n*Qa = O`
	1.	`r`,`s` in `[1,n-1]`
	2.	`e = hash(m)`
	3.	`z = e[:Ln]`
	4.	`u1 = z*s**-1 mod n`, `u2 = r*s**-1 mod n`
	5.	`(x1,y1) = u1*G + u2*Qa` : if `(x1,y1) = O` signature invalid
	6.	`r = x1 mod n` : if true, signature valid


## RSA

### NOTATION
`m` : plain text msg  
`c` : encrypted msg  
`p, q` : prime numbers (keys)  
`n=p*q` :   
`d=` :   
`e=` :   

### factorization

**General Number Field Sieve for integer factorization** : best algo  
*	`2048b` for `112b` security

#### elliptic curve factorization method
Much more effective if there's at least one small prime (up to approximately 80 bits / 25 decimal digits).  

e.g.: `ecm.factor(n)` : sage  

### totient function
`totient(n)` = `phi(n)` = number of x coprime with n s.t. 0<=x<=n  
*	`phi(p)=p-1` : if `p` prime
*	`phi(x*y)=phi(x)*phi(y)` : if `x`,`y` coprime
	*	`totient(n)=(p-1)*(q-1)` : if p!=q primes  
*	note: `p**phi(q)=1 mod q` if `p`,`q` coprime - euler's th uses phi
`totient(n)=p*(p-1)` : if n=p**2
e.g.: `tot(20)=tot(2**2*5)=20*(1-1/2)*(1-1/5)=2*(2-1)*(5-1)=8`: (wikipedia) ?  


### FORMULAS
`d=e**-1 mod tot`  
`d*e mod tot = 1`  
`totient = (p-1) * (q-1)`  
`m**e mod n = c`  
`c**d mod n = decrypted`  

### HACKS
#### find n: 
*	method 1 - if you know e:  
	*	note: e is usually 65537  
	1.	choose any two messages `𝑥`, `𝑦`  
	2.	get the encrypted `enc(x)=x**e%n`, `enc(y)`  
	3.	calc `x**e`, `y**e` (without modular reduction)  
		*	note: `x**e - enc(x)` is a multiple of `n`  
	4.	`n=gcd(x**e - enc(x), y**e - enc(y))`  
	5.	Repeat with different values if necessary (?)  
*	method 2 - if you don't know e:
	1.	get (for instance) `c2=enc(2)`, `c4=enc(4)`, `c8=enc(8)`  
	2.	calc `pn=c2**2-c4`, `qn=c2**3-c8`
		*	note: these are multiples of n (`p*n`, `q*n`)  
	3.	`n=gcd(pn, qn)`
	4.	Repeat with different values if necessary  
*	method 3:  
	1.	encrypt/decrypt -1  
	2.	guess (doesn't work with values < n)  

#### decrypt any ciphertext `c`
*	method 1:
	1.	encrypt a chosen `x`: `x**e`  
	2.	decrypt (by oracle) `x**e * c`  
	3.	`dec(x**e * c) = dec(x**e) * dec(c) = x * dec(c)`, so `m=dec(c) = dec(x**e * c) / x`  
	4.	alternative: `dec(x**e * c)=mx%n`, so `m` is the inverse of `x`
		*	note: easy to calc, as `x` and `n` are mutually prime  

#### find d
*	mod inverse is not hard, the hard part is to factorize n and get p, q  
#### decrypt when gcd(e,phi)!=1
*	note: used in Rabin system.  
*	`n`, `p`, `q`, `e`, `ct` are given.  
*	work in q (don't know why):
	```python
	ct_q = ct % q
	phi_q = q-1
	d_q = inverse_mod(e, phi_q / gcd(e,phi_q) )
	m = pow(ct_q, d_q, q)
	```
	
