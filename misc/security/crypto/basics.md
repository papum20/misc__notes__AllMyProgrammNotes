# BASICS.MD

rsa: 2048 bit  

## Modular arithmetics

**finite field** : **Fp**/**GF(p)** (_galois field_) - `{0,1,...,p-1}` set of integers modulo `p` prime  
*	**inverse** element : there's always an inverse element `b` for every `a` in the set...
	*	for addition : ...such that `a+b=0`
	*	for multiplication : ...such that `a*b=1`
		*	`pow(a,p-2,p)` :
			*	proof:
					```
					a**(p-1) = 1 mod p
					a**(p-1) a**(-1) = a**(-1) mod p
					a**(p-2) a a**(-1) = a**(-1) mod p
					a**(p-2) = a**(-1) mod p
					```
	*	proof: there's a `b` inverse of `a` mod `p` iff `gcd(a,p)=1`, always true for finite fields (but not for rings)
*	`a**(p-1) mod p` : `p-1` - for any `a` in `Fp`  
*	`a**(kp) mod p` : `a` - for `k` integer  

**ring** : set of integers modulo `n` not prime  

### quadratic residues

uses:
*	elliptic curves  

quadratic residue : iff has square root mod n (`a` iff `pow(b,2,n)==a`)  
quadratic non-residue : else  
*	prop: 
	*	a residue * a residue = a residue
	*	a residue * a non residue = a non residue
	*	a non residue * a non residue = a residue
	*	tip: like `+1,-1`
	*	e.g.: pow(a residue, n) = a residue, for any n


Legendre's Symbol : `(a / p) ≡ pow(a,(p-1)/2), p)`, for `p>2` prime
*	`(a/p) = 1` : if a is a quadratic residue and `a%p != 0`
*	`(a/p) = -1` : if a is a quadratic non-residue mod p
*	`(a/p) = 0` : if `a%p == 0`

square root `r` of `a` when `p%4=3`, `p>2` prime (note that `p%4` is either 1 or 3) : `r=+-pow(a,(p-1)/4,p)`
*	proof:
	1.	if `p%4=3` then, in `mod p`, `pow(pow(+-a,(p+1)/4),2)=pow(a,(p+1)/2)=pow(a,(p-1)/2+1)=pow(a,(p-1)/2)*a`
	2.	since a is a quadratic residue, `pow(a,(p-1)/2)=1 mod p`
*	src: https://crypto.stackexchange.com/a/20994

Tonelli-Shanks : square root `r` for any `p>2` prime
*	e.g.: implemented in sage `Mod.sqrt()`

### linear congruences system

linear congruences system :
```
x=a1 mod n1
...
x=ak mod nk
```

**Chinese remainder theorem** : if `ni` coprimes, unique solution `x=a mod N`, where `N=n1*...*nk`  
*	proof: from `x%n1=a1` you can rewrite `x=a+k*p` for any k
*	e.g.: sage `crt()`


## RSA
### NOTATION
`m` : plain text msg  
`c` : encrypted msg  
`p, q` : prime numbers (keys)  
`n=p*q` :   
`d=` :   
`e=` :   
#### totient function
`totient(n)` = `phi(n)` = number of 0<=x<=n prime with n  
`totient(n)=(p-1)*(q-1)` : if p!=q primes  
`totient(n)=p*(p-1)` : if n=p**2
e.g.: `tot(20)=tot(2**2*5)=20*(1-1/2)*(1-1/5)=2*(2-1)*(5-1)=8`: (wikipedia)  

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
	