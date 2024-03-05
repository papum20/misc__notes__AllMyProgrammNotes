# BASICS

Properties and definitions:
*	Take:
	*	a set S
	*	an operation, let's call it ⊕
	*	another operation, say ⊙
	*	fix an element O∈S, such that ∀s∈S:O⊕s=s
	*	fix another element I∈S, such that ∀s∈S:I⊙s=s
*	Now I will list a set of properties and behind some properties I'll write names. If all the previous points apply, then the name can be applied to the named tuple.
	*	(closure under addition) ∀s1,s2∈S:(s1⊕s2)∈S
	*	(additive associativity) ∀s1,s2,s3∈S:(s1⊕s2)⊕s3=s1⊕(s2⊕s3) . We can now call (S,⊕) a semigroup.
	*	(additive identity) ∃O∈S:∀s∈S:O⊕s=s⊕O=s . We can now call (S,⊕,O)  a monoid.
	*	(additive inverses) ∀s∈S:∃s′∈S:s′+s=s+s′=O . We can now call (S,⊕,O)  a group.
	*	(additive commutativity) ∀s1,s2∈S:s1⊕s2=s2⊕s1 . We can now call (S,⊕,O)  an abelian group.
	*	(multiplicative closure) ∀s1,s2∈S:s1⊙s2∈S
	*	(multiplicative associativity) ∀s1,s2,s3∈S:s1⊙(s2⊙s3)=(s1⊙s2)⊙s3 . We can now call (with 6 and 7) (S,⊙)  a semigroup.
	*	(multiplicative identity) ∃I∈S:∀s∈S:I⊙s=s⊙I=s . We can now call (with 6-8) (S,⊙,I)  a monoid.
	*	(right distributivity) ∀s1,s2,s3∈S:(s1⊕s2)⊙s3=(s1⊙s3)⊕(s2⊙s3)
	*	(left distributivity) ∀s1,s2,s3∈S:s1⊙(s2⊕s3)=(s1⊙s2)⊕(s1⊙s3) . We can now call (S,⊕,⊙,O,I)  a ring. Note: In some definitions having a multiplicative identity is optional.
	*	(multiplicative commutativity) ∀s1,s2∈S:s1⊙s2=s2⊙s1 . We can now call (S,⊕,⊙,O,I)  a commutative ring.
	*	(multiplicative inverses) ∀s∈(S∖{O}):∃s′∈S:s⊙s′=s′⊙s=I . We can now call (S,⊕,⊙,O,I)  a field.
*	src: https://crypto.stackexchange.com/questions/55147/what-is-the-main-difference-between-finite-fields-and-rings#:~:text=But%20finite%20fields%20have%20another,of%20same%20order%20are%20isomorphic.

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
	*	the inverse is **unique**, if exists
	*	proof: there's a `b` inverse of `a` mod `p` iff `gcd(a,p)=1`, always true for finite fields (but not for rings)
*	`a**(p-1) mod p` : `p-1` - for any `a` in `Fp`  
*	`a**(kp) mod p` : `a` - for `k` integer  
*	`p**phi(q)=1 mod q` : _euler's theorem_ - if `p`,`q` coprime, with `phi` totient

**ring** : set of integers modulo `n` not prime  

## exponentiation
`q=gcd(N,mod(q**e,N))` : if `N=pq` primes, for any exp `e`  

## multiplicative groups

**multiplicative group** : `Zp*={1,2,...,p-1}` - finite field where elements cyclically generate all the other elements  
*	`Fg(x)=g*x mod p` : generator function, for generator `g`

**generator** : `g` - iff cycling to `1` (`g**x mod p` for `x=1,2,...,p-1`) doesn't occur before `p-1` times  
*	**order** : `k` - smallest `k` s.t. `g**k=1 mod p`
	*	th: `k|p-1`
	*	obs: `g` generator iff `k=p-1`
*	algo: test if `g` is a generator - iff `g**((p-1)/q)!=1 mod p` for any prime factor `q` of `p-1`
	*	proof:
		*	`p-1=ku`
		*	if `u!=1` (because not a generator), `u=qv`, thus `p-1=kqv`
		*	`g**k=1 mod p` since `k` is its order
		*	so `g**k = 1 = (g**k)**v = g**kv = g**((p-1)/q) = 1 mod p`

src:
*	https://crypto.stackexchange.com/questions/40654/find-the-generators-of-multiplicative-group-of-units-efficiently?newreg=5899d2f2288b407980ddb4133d7864c5
*	https://crypto.stackexchange.com/questions/102292/proof-that-checking-if-gk-bmod-p-ne1-finds-a-generator-of-a-cyclic-group/102301#102301

## quadratic residues

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


Legendre's Symbol : `(a / p) ≡ pow(a,(p-1)/2, p)`, for `p>2` prime
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

## linear congruences
`a=b mod n` : 
*	sol iff `(d=gcd(a,n))|b`
	*	solutions: divide both sides by `d` to find solution `c`, then all `n/d` solutions are `c+kd` for any `k`
	*	obs: _finite field_ - always, as `d=1` with prime

## linear congruences system

linear congruences system :
```
x=a1 mod n1
...
x=ak mod nk
```

**Chinese remainder theorem** : if `ni` coprimes, unique solution `x=a mod N`, where `N=n1*...*nk`  
*	proof: from `x%n1=a1` you can rewrite `x=a+k*ni` for any k
*	e.g.: sage `crt()`
