# BASICS

## Methods 

### Decision trees

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


### Random forest

_random forest_ : **ensemble** - of _decision trees_  
_ensemble technique_ : large number of _relatively uncorrelated_ models 
*	ensure differentiation
	1.	_bagging_ : feeding different, randomly choosen sets of input data
	2.	_feature randomness_ : building trees from random subsets of features

	