# OBJECTS

## sklearn.datasets

`load_DATASET(as_frame=False)` : loader  
*	`as_frame=False` : values as `numpy.array`
*	`as_frame=True` : values as `pandas.DataFrame`

`make_DATASET(n_samples, n_features, centers, random_state, class_sep, weights, n_informative, n_redundant, flip_y, n_clusters_per_class)` : genration function  
*	`centers` : 
	*	e.g.: `centers=n_classes` 
*	`random_state` : rand seed

`lfw_DATASET(color: bool)` : fetcher  

`load_iris()` : iris flower  

`make_blobs()` :  
`make_moons()` :  
`make_s_crve()` :  
`make_circles()` :  

`fetch_lfw_people()` :  
`fetch_lfw_covtype()` :  

### loader object
`data` : x (input)  
`target` : y (label)  

### fetcher object
`images` : x (input)  
`target` : y (label)  

## preprocessing

### sklearn.model_selection

#### cross validation
`cross_val_score(estimator, X, y, cv:int)` : cross validation, return result for each fold  
*	`estimator` : a model
	*	e.g.: `LogisticRegression`

`StratifiedKFold(n_splits:int)` : cross validator obj  
*	`n_splits` : folds n

#### split
`train_test_split(X, y, test_size:float, stratify, random_state)` : split train and test 
*	`stratify` : label to use to stratify (`y`), if want to split with stratification

### sklearn.preprocessing

`METHODScaler()` : scaler, for _normalization_  

`StandardScaler()` : `z = (x - u) / s`  
`MinMaxScaler()` : range [0,1]  
`MaxAbsScaler()` : divide each col by its max val  

(log normalization scaler)  

#### scaler classes

`fit(X)` : use array `X` to compute the maximum absolute value to be used for later scaling  
`transform(X)` : scale data  

## learning

### sklearn.ensemble

`VotingClassifier(estimators:List, voting:str)` : ensemble model, with voting method
*	`estimators` : list of models
*	`voting='soft'` : weighted average of probabilities

### sklearn.linear_model

#### LogisticRegression

`coef_` : regression weights  

`LogisticRegression(C:float, multi_class='multinomial', penalty:str, solver='saga', tol:float, random_state)` :  
*	`C` : inverse of regularization strength
	*	e.g.: `0.01`, `1.0`
*	`penalty='l1'|'l2'` : regularization type
*	`tolerance` : turn up for faster convergence

`fit(X,Y)` :  
`score(X_test,Y_test)` : test and get score (in `[0,1]`)  

### sklearn.tree

Decision trees.  

`export_graphviz(Tree, out_file)` : export img of tree  

#### DecisionTreeClassifier

`feature_importances_` : importance of each feature  

`DecisionTreeClassifier(criterion='entropy', random_state=0)` : get the tree  

`fit(X,Y)` : train model, with train data  
`predict(X)`: predict classes for test data  
