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

### types of methods

_discriminative_ : (primarily) used for classification tasks

_generative_ : can model underlying data distribution, generate new data samples
*	use: _classification_
*	use: data generation
*	use: data augmentation (with cautions)
*	use: anomaly detection

### types of probles

_classification_ : learn the _decision boundary_, separating classes in data  

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

*	Decision trees
*	Probabilistic approaches
	*	Joint distribution
	*	Logistic regression
		*	Gradient technique
	*	Naive Bayes
*	Random forest
