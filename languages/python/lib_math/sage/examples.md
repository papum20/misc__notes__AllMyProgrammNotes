# EXAMPLES

## Modular arithmetic

handling element of Fpk (from Epk, i.e. EllipticCurve over prime p**k) :
*	```py
	p = 1331169830894825846283645180581
	a = -35
	b = 98
	E = EllipticCurve(GF(p), [0,1,0,1,0])	# ec
	k = 2	# extension degree

	Fpk = GF(p**k, 'z')	# extension field
	Epk = E.base_extend(Fpk)	# ec on fpk
	assert Fpk = Epk.base_ring()	# example usage of base_ring

	Gpk = Epk.abelian_group().gens()[0] 
	assert Gpk == (1046622187051151830476771583048*z2 + 362948857810654519977433111475 : 143398469641251292777945027238*z2 + 1078401350490801661151376542995 : 1)

	z = Fpk.gen()	# 'z' variable name in Fpk

	# Create an element of the extension field
	x = 1046622187051151830476771583048 * z2 + 362948857810654519977433111475

	assert x.list(sparse=False) == (362948857810654519977433111475, 1046622187051151830476771583048)
	#assert x.polynomial().coefficients(sparse=False) == (362948857810654519977433111475, 1046622187051151830476771583048)

	# Convert x to an integer
	print(x.to_integer())

	assert factor((x - x.list()[0]).to_integer()) == 2^3 * 11 * 3783205067 * 3143745510257080913 * 1331169830894825846283645180581
	assert factor(1046622187051151830476771583048) == 2^3 * 11 * 3783205067 * 3143745510257080913
	# it seems that what remains (i.e. 1046622187051151830476771583048*z2) is just 1046622187051151830476771583048 * p, in modulo (in fact, we're working in p**2)
	```
