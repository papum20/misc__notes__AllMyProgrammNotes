# BASICS

## machine learning

machine learning :  
*	it's an optimization problem (see steps later)
*	uses iterative techniques

steps :
1.	**model** : define a model for the task to solve, depending on **parameters**
2.	`loss function` : `error function` - **performance metrics** - error measure to eval and choose best model
3.	**parameters** : tune to minimize error
*	e.g.: regression problem : 
	1.	fix parametric class of models, like `y=ax+b`, where params are `a`,`b`
	2.	fix a way to decide when a line is better
		*	e.g.: mean square error  
	3.	try to tune params

**_feature_** : **input** - any information relative to a datum, that describes some of its relevant properties  
*	note: learning is sensible to choice of features
*	note: choice hard, requires domain knowledge
*	e.g.: medical diagnosis : symptoms, patient condition, medical record... 

`<x^(i),y^(i)>` : `train set` - set of training examples  
*	`X` : set of inputs
*	`Y` : set of outputs
*	`x^(i) \in X` : 
*	`y^(i) \in Y` : 
*	`i` : instance of the training sample

### overfitting

_overfitting_ : `h` **overfits** train set `train`, on the full data domain set `D`, iff `\exist h' | error_train(h)<error_train(h') && error_D(h)>error_D(h')`  
_underfitting_ :  

estimate : we don't have `D`, so divide available data in _train set_ (to choose `h`) and _validation set_ (to validate `h`)
*	_early stopping_: terminate the construction of the tree as soon as the classification improvement is not statistically significative
	*	: `I()<threshold` :  
	*	_post-pruning_ : _reduce-error post-pruning_ - develop the full tree and then proceed to backward prune it
		1.	for any subtree, compute the impact of its removal on the classification accuracy on the validation set
		2.	greedily perform pruning of the subtree that optimizes accuracy

## types

### types of learning tasks 

**_supervised learning_** : inputs + outputs (labels)  
*	use: classification
*	use: regression

**_unsupervised learning_** : inputs  
*	use: clustering
*	use: component analysis
*	use: autoencoding

**_reinforcement learning_** : actions and rewards 
*	use: learning long-term gains
*	use: "model-free" planning

### learning approaches

old approach : you choose and compute good features, then use algo  
modern/**deep** approach : supply raw data to machine, which computes features  
*	impl: neural networks

## problems

### function approximation

**_function approximation_** : from `<x^i,y^i>`, learn function mapping `x^i` to `y^i`
**_classification problem_** : if `Y` discrete  
*	impl: _class prediction_

**regression problem** : if `Y` continue  
*	impl: _value prediction_

**_commitment_** : choice of a _function space_/_hypothesys space_ `H`, inside which to look for the best approx function for the _train set_  
**_model_** : a way to compute a function in `H`  

### document classification

...

## methods

### decision trees

_attribute_ : _feature_  

tree :  
*	_branch_ : corresponds to one possible discrete value of `X`
*	_leaf_ : predicts an answer `Y`, or _probability_ `P(Y|X)`
*	_node_ : each tests an _attribute_ `X`  

problem configuration :  
*	`x \in X` : input - vector of values for features
*	`y \in Y` : output - boolean (discrete)
*	`f:X->Y` : _target function_ - 
*	`H={h|h:X->Y}` :  

pro:
*	easy to understand: simple logical rules, trees can be
visualized
*	little or no data preprocessing is required
*	very low prediction cost
*	can be used with both discrete and continuous features
con:
*	high risk of overfitting
*	selection of attributes quite unstable
*	easy to build strongly unbalanced trees
	*	especially if a class is dominant
	*	note: can be useful to pre-balance the dataset

#### construction

tree construction : choice of order of evaluated attributes  
1.	assign to current node the _best attribute_ `Xi`
2.	create a child node for each possible value of `Xi`
3.	if `y^(i)=y` for each child node `x^(i)`, mark the _leaf_ with _label_ `y`, else iterate to 1.

`H(X)=-sum(i=1..n)(P(X=i)log2(P(X=i)) )` : _entropy_ - of a random variable `X`
*	`n` : nomber of possible values of `X`
*	measures degree of impurity of information
*	obs: max when `X` uniformly distributed over all values
*	obs: min when concentrated on single value
*	**information theory (shannon)** : entropy is average amount of information produced by a stochastic source of data
	*	`I(p)` : information of probability `p`
	*	obs: `I(1)=0` : no surprise
	*	obs: `I(p1p2)=I(p1)+I(p2)` : if `p1`,`p2` indep
	*	`I(p)=-log(p)` : works like log, info of product is sum of infos
*	**code theory (shannon)** : entropy measures average nmber of bits required to transmit outcomes produced by stochastic process `X`
	*	`log(n)` : bits to encode `n` possible outcomes (of an event), equiprobable
		*	`H(X) = -sum(i=1..n)( P(X=i)log2(P(X=i)) ) = -sum(i=1..n)( (1/n)log2(1/n) ) = log(n)` : 
	*	note: if not equiprobable, we can do better (see _codnitional entropy_)

`H(X|Y=v) = -sum(i=1..n)( P(X=i|Y=v)log2(P(X=i|Y=v)) )` : _conditional entropy_ : of `X` given a specific `Y=v`
`H(X|Y) = -sum(v=1..m)( P(Y=v)H(X|Y=v) )` : _conditional entropy_ : of `X` given `Y`
*	weighted average over all `m` possible values of `Y`

`I(X,Y) = H(X)-H(X|Y) = H(Y)-H(Y|X)` : _information gain_ : **between** `X` and `Y`

_best attribute_ : the one bringing more information gain  

_threshold_ : used for continuous attributes
*	compare thresholds, using info gain, to construct tree

### probabilistic approaches
(notes in [note.md](./notes.md))

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

**learning**/**training** : 
*	steps:
	1.	_estimate_ `pi_k` for any possible value `yk` of `Y`
	2.	_estimate_ `teta_ijk` for any possible value `xij` of `Xi`

**estimate** : 
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

### random forest

_random forest_ : **ensemble** - of _decision trees_  
_ensemble technique_ : large number of _relatively uncorrelated_ models 
*	ensure differentiation
	1.	_bagging_ : feeding different, randomly choosen sets of input data
	2.	_feature randomness_ : building trees from random subsets of features