# BASICS

A type of machine learning.  
*	"deep" :
	*	_deep_ _neural networks_ (with many layers)
	*	deep features (extracted from other features)

use: all machine learning problems
*	better for many features
	*	e.g.: img, speech, text processing

## Methods

### neural network

cyclic : 
*	_recurrent_ : nn if cyclic
*	_feed-forward_ : nn if acyclic

_layer_ : set of _neuron_ s
*	layers :
	*	input
	*	hidden : many
	*	output
*	_dense_ : in layer `k`, each neuron is connected to all neurons in layer `k-1`
*	_convolutional_ : in layer `k-1`, each neuron is connected to a subset of neurons in layer `k`
	*	thru a _kernel_ (a matrix of weights) (of fixed size), which is convolved over whole prev layer
		1.	move kernel `K` on portion `M` of input, of equal size, with step `b` (__stride__)
		2.	`M K + b`
		3.	move `K` and repeat
		*	output dimension depends on n times `K` applied
			*	input _structured_, and structure reflected in out
*	_deep_ : nn if has >1 hidden layer
*	_shallow_ : else
	
_neuron_ : `I^n W^n + B^1 = O^1` - compute a weighted sum of its inputs, then apply _activation function_
*	weighted sum : `sigma (w x + b)` - implements a logistic regressor
*	_activation function_ : non-linear function on result of weighted sum
*	`w` : weights vector, made of `w1, w2, ..., wn`
*	`x` : input vector, made of `x1, x2, ..., xn`
	*	_flat_ / _unstructured_ : order of elements irrelevant
		*	note: usual for _dense_ layers
	*	_structured_ : 
		*	note: usual for _convolutional_ layers
*	`b` : bias (constant)
*	`I^n W^n*m + B^m = O^m` : vectorized operation on `m` neurons, to produce `m` outputs in parallel

## Misc

**logit** : probability of a certain output
*	e.g.: probability of different predictions at a certain step, useful to understand why one was chosen
