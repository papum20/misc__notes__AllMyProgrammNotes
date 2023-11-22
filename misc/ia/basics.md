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

