# BASICS

## Methods


### Probabilistic approaches
(probability basics notes in [note.md](./notes.md))

`p:P(Y|X)` : **approximating functions** - compute probability instead of `f:X->Y`  

`Omega` : should choose _sample space_ where outcomes have same `P()`  

#### Joint distribution

_joint distribution_ :  
*	steps:
	1.	build a table with all possible combination of values of all random variables (_features_)
	2.	compute `P()` for each combination of values
*	obs: need to compute `2**n-1` params

`P(E) = sum(row \in E)( P(row) )` : probability of any event `E`  
`P(E1|E2) = P(E1&E2)/P(E2) = ( sum(row \in E1+E2)(P(row)) )/( sum(row \in E2)(P(row)) )` : easy to get `P(E1)` given `P(E2)`  
`P(Y=yi|X1,..,Xn) = ( P(Y=yi)P(X1,..,Xn|Y=yi) )/( P(X1,..,Xn) )` : _bayes rule_ for _joint distribution_, in general  

#### Logistic regression

assume:
*	`Y` : bool rand var
	*	`pi` : `Y` has **bernoulli distribution**
*	`Xi` : cont rand var, indep from each other `Y`
*	`P(Xi|Y=k)` : _gaussian distribution_ `N(mu_ik,sigma_i)`
	*	obs: not `delta_ik`


idea:
*	_naive bayes_ computes `P(Y|X)` after learned `P(Y)` and `P(X|Y)`

note:
*	`sigma(x)` : _logistic function_ - `1/(1+e**-x)` 

_logistic regression_ : `P(Y=1|X=<x1,..,xn>)` : `1/( 1 + e**(w0+sum(i)(wi xi)) )`
*	obs: `P(Y=1|X=<x1,..,xn>)` : `sigma*(w0+sum(i)(wi xi))`
*	proof: ...

**training** : 
*	input: independent samples `<x**l,y**l>`
	*	obs: their prob is `prod(l)(P(y**l|x**l,w)) = prod(l)( P(y**l=1|x**l,w)**(y**l) P(y**l=0|x**l,w)**(1-y**l) )`
	*	obs: in log `sum(l)(log P(y**l|x**l,w)) = sum(l)( y**l P(y**l=1|x**l,w) + ()1-y**l) P(y**l=0|x**l,w) )`
*	steps:
	1.	`w` : _gradient technique_, until satisfying accuracy/increment < threshold `eps`
		*	`wi` : `wi + mu sum(l)( xi**l (y**l-P(Y=y**l|xi wi)) )`
	*	note: there's no analytic solution

##### Gradient technique

assume:
*	`alpha**l` : `sigma(w0+sum(i)(wi xi_l))`

_gradient technique_ : minimize some error function `theta(w)`, on all training examples  
*	steps:
	1.	_gradient descent_ : iteratively take (small) steps in the direction opposite to the gradient
		*	obs: that's the max growth (or decrease) direction
		*	obs: can add _regularizer_
*	types: how many points, of all the training samples, to use for measuring error and gradient
	*	_full batch_ : all
		*	obs: steepest descent
		*	obs: perpendicular to contour lines
	*	_online_ : one at a time
		*	obs: gradient zig-zags arond steepest direction 
	*	_mini-batch_ : random subset 
		*	compromise

`l(w)` : _log-likelihood_ - `sum(l)(P(Y=y**l)|x**l,w) = sum(l)( y**l log(alpha**l) + (1-y**l) log(1-alpha**l) )`
*	`D[l(w)]/D[wi]` : **gradient** - `sum(l)(xi**l (y**l-alpha**l))`
	*	proof: ...
*	other results : ...
	*	see logistic regression training for the useful result

_regularizer_ (_prior_) : `mu lambda|wi|` 
*	pro: helps keep params `wi` close to `0`
*	pro: tends reduce overfitting


#### Naive Bayes

assume: `P(X1,..,Xn|Y) = prod(i)(P(Xi|Y))` : given `Y`, all `Xi` indep
*	proof: _chain rule_ and _conditional independence_
*	note: not always indep
	*	e.g.: image of pixels `pi={0,1}`, category `A` if `p1=p2`, else `B`
		*	`P(p1=1|A)` : `?`
		*	`P(p1=1|B)` : `?`

_naive bayes_ : 
*	need `n` params
*	note: sum of all possible outcomes should be `1`, but is often `<`; need to _normalize_ (by `P()`)

`P(Y=yi|X1,..,Xn) = ( P(Y=yi)prod((j)( P(Xj|Y=yi)) ) )/( P(X1,..,Xn) )` : _bayes rule_ for _naive bayes_, in general  

**classification** :
*	`Ynew = argmax(yi)( P(Y=yi)prod(j)(P(Xj=xj|Y=yi)) )` : **classification** of a **new sample** `xnew = <x1,..,xn>`  
	*	obs: outcome `yi` which makes max `P()`
*	`Ynew = argmax(k)( pi_k prod(i)(teta_ijk) )` : **classification** of `anew=<a1,..,an>`
	*	obs: outcome `yk` which makes max `P(Xi)`, i.e. compute argmax for each _var_, using only available values/data/samples `<xi..>` for such `Xi`
	*	`pi_k` : `P(Y=yk)`  
	*	`teta_ijk` : `P(Xi=xij|Y=yk)` - final outcome value estimate

**estimate** : estimate naive bayes own variables
*	_maximum likelihood etimates_ (_MLE_'s)
	*	`pi_k` : `(#D{Y=jk})/#D`
	*	`teta_ijk` : `( #D{Xi=xi,j&Y=yk} )/( #D{Y=yk} )`
	*	**bernoulli's distribution** : possible final outcomes `{0,1}`, probabilities `{alpha0=P(0),alpha1=P(1)}`
		*	`teta` : `alpha0/n` - `P(0)`
		*	proof:
			*	`teta_hat = argmax(teta)( P(X**n=alpha0|teta) )`
			*	`teta_hat = argmax(teta)( (teta**alpha0)(1-teta)**alpha1 )`
			*	equivalently, look for teta maximizing log : `ln( (teta**alpha0)(1-teta)**alpha1 )`
			*	`= alpha0 ln(teta) + alpha1 ln(1 - teta)`
			*	deriving with respect to `teta` : `alpha0/teta - alpha1/(1-teta) = ( alpha0 - alpha0 teta - alpha1 teta )/( teta(1-teta) )`
			*	so it's max iff derivate is 0, and that expression is 0 for : `teta = alpha0/(alpha0+alpha1) = alpha0/n`
	*	**multinomial distribution** : outcomes `{1,..,k}`, probabilities `teta_i`, `sum(i)(teta_i) = 1`
		*	`P(X**n=alpha_i|teta)` : `c__alpha_i prod(i)(teta_i**alpha_i)`
			*	`alpha_i` : number of `i` in the sequence
			*	`c__alpha_i` : combinatorial constant not epending on `teta`
		*	`teta_i = alpha_i/(sum(i)(alpha_i)) = alpha_i/n`

**learning**/**training** : 
*	steps:
	1.	_estimate_ `pi_k` for any possible value `yk` of `Y`
	2.	_estimate_ `teta_ijk` for any possible value `xij` of `Xi`

#### linear case

assume:
*	`x=<x1,..,xn>` : input to classify
*	`Y \in {0,1}` : bool outcome

`log( P(Y=1)/P(Y=0) ) + sum(i)(xi log(teta_i1/teta_i0)) + sum(i)(1-xi) log( (1-teta_i1)/(1-teta_i0) )` : _linear classification_, **boolean case** - `>=0` iff evaluated outcome is `Y=1`, not `Y=0`
*	proof:
	*	classify as `Y=1` iff `P(Y=1|X1..Xn=x)/P(Y=0|X1..Xn=x) >= 1` : val `1` more probable
	*	iff `(P(Y=1)prod(i)P(Xi=xi|Y=1) )/( P(Y=0)prod(i)P(Xi=xi|Y=0) ) >= 1` : naive, assume indep
	*	`log( P(Y=1)/P(Y=0) ) + sum(i)(log(P(Xi=xi|Y=1)/P(Xi=xi|Y=0)) ) >= 0` : pass to logs
	*	knowing that for a bool `f(x) = x f(1) + (1−x) f(0)`
	*	with `teta_ik=P(Xi=1|y=k)` (hence `P(Xi=0|y=k)=1−teta_ik`)
	* we conclude the above: `log( P(Y=1)/P(Y=0) ) + sum(i)(xi log(teta_i1/teta_i0)) + sum(i)(1-xi) log( (1-teta_i1)/(1-teta_i0) ) >= 0` iff `1` more probable
*	note: that's a linear expression in the set of features xi
	*	obs: thus evaluates each feature indep

#### continuous case

assume:
*	`x \in R` : continuous random var
	*	note: in continuous case `P(X=xi|Y)` is pointless (`1/infinite`)
1.	`N(x|mu_ik,sigma_ik) = 1/(sigma_ik sqrt(2pi)) e**( -(x-mu_ik)**2/2sigma_ik**2 )` : _inductive bias_ - for every val `yk` of `Y`, random var `P(Xi|Y=yk)` has a _gaussian distribution_

e.g.:
*	classify height or age of people

_decision boundary_ : 
*	idea: a vertical line, separating neatly classes classification
*	obs: if move right, _precision_`++`, _recall_`--` (assuming bool, 0 is left, 1 is right)

_gaussian distribution_ : assume input has gaussian distribution
*	`p(x|mu,sigma)` : _probability density_ - `1/(sigma sqrt(2pi)) e**( -(x-mu)**2/2sigma**2 )`
*	`E[X]=mu` : _mean value_
*	`Var[X]=simga**2` : _variance_
*	`sigma_X=sigma` : _standard deviation_
*	note: `integral(p()) = 1`

**classification** : of new `xnew=<a1,..,an>`
1.	`Ynew = argmax(k)( pi_k prod(i)(N(ai|mu_ik,sigma_ik)) )` : 
	*	proof: `Ynew = argmax(k)( P(Y=yk)prod(i)(P(Xi=ai|Y=yk)) )`, hence follows above
	*	idea: (boolean case) choose _decision boundary_ = `xk` (x axis)
		*	idea: on a graph, _decision boundary_ is a vertical line, classes are each a different _gaussian distribution_ (i.e. with own params) 
		*	classify `0` if sample to classify `xi<xk`, else `1`

**classification results** : (bool case)
*	_true positive_ (_TP_) : evaluated `1`, actually is `1`
*	_false positive_ (_FP_) : evaluated `1`, actually is `0`
*	_true negative_ (_TN_) : evaluated `0`, actually is `0`
*	_false negative_ (_FN_) : evaluated `0`, actually is `1`

**classification metrics** : measure "precision" (bool case)
*	`N` : total number of samples classified
*	`(TP+TN)/N` : _accuracy_ - number of correctly classified samples
*	`TP/(TP+FP)` : _precision_ - percentage of true positives over predicted ones
	*	obs: focus on target class to identify
*	`TP/(TP+FN)` : _recall_ - percentage of true positives over all positives
	*	obs: focus on target class guesses
*	`2(Precision Recal)/(Precision+Recall)` : _F1_ - armonic mean of _precision_ and _recall_

**learning** : estimate params
*	_MLE_ : 
	1.	`mu_ik` : `sum(j)(Xi**j delta(Y**j=yk)) )/sum(j)(delta(Y**j=yk))` - mean value of `Xi` for samples with label `Y=yk`; `j` ranges over samples in the _train set_
		*	`delta(Y**j=yk)` : `1` if `Y**j=yk`, else `0`
	2.	`sigma_ik**2` : `sum(j)( (Xi**j-mu_ij)**2 delta(Y**j=yk) )/sum(j)(delta(Y**j=yk))` - variance of `Xi` for samples with label `Y=yk`
