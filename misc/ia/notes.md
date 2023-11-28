# NOTES

## Probabilty basics

`{x \in Omega|PROPERTY}` : _event_ - any subset of `Omega`  
*	`A \indep B` : _independent_ - iff `P(A|B)=P(A)`
	*	obs: `B` has no influence on `A`
	*	obs: `P(A&B)=P(A)P(B)`
*	`A1,A2 \indep Y` : _independent given another var_ - iff `P(Xi|Xj,Y)=P(Xi|Y)`

`P(X)` : _probability of random variable_ - fraction of times `X` is true, in repeated runs of the same experiment  
`P(E)` : _probability of event_ - probability event `E`  
*	e.g.: `P(VAR=VAL)` :  

`P(E1|E2)` : _probability conditioned on other event_ -  `P(A&B)/P(B)`

`X` : _random variable_ - measurable function over `Omega` (domain)
*	_k-valued discrete_ : iff value in `{v1,..,vk}`
*	obs: denotes an incertain outcome  

`Omega` : _sample space_ - set of possible outcomes of a random experiment  

### Theorems

`P(A|B) = ( P(A)P(B|A) )/P(B)` : _Bayes' rule_ -  
*	`P(Y=yi|X=xj) = ( P(Y=yi)P(X=xj|Y=yi) )/( sum(i)( P(Y=yi)P(X=xj|Y0yi) ) )` : other formulation
*	`P(Y|X)` : _posterior_
*	`P(X|Y)` : _likelihood_
*	`P(Y)` : _prior_
*	`P(Y) = sum(Y)( P(X|Y)P(Y) )` : _marginal likelihood_
	*	obs: _marginal_ because marginalized (i..e.. integrated) over `Y`


`P(B)P(A|B) = P(A)P(B|A)` : _chain rule_ -  