# BASICS

rsa: 2048 bit  

## Diffie-Hellman

**diffie-hellman** : uses discrete log as hard problem.  
*	input:
	*	`p` : prime, defining the field `Fp` (multiplicative group)
	*	`g` : generator of `Fp`
	*	`a` : `a<p` - private key 
*	steps:
	*	`c=g**a mod p` : encrypted

**safe prime** : `p=2q+1` with `p`,`q` prime - avoid efficient attacks if not safe (_pohlig hellman_)  


## RSA

### NOTATION
`m` : plain text msg  
`c` : encrypted msg  
`p, q` : prime numbers (keys)  
`n=p*q` :   
`d=` :   
`e=` :   

### factorization

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
		*	note: these are multiple of n (`p*n`, `q*n`)  
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
	```
	ct_q = ct % q
	phi_q = q-1
	d_q = inverse_mod(e, phi_q / gcd(e,phi_q) )
	m = pow(ct_q, d_q, q)
	```
	
