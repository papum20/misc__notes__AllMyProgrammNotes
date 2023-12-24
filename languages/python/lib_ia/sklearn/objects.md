# OBJECTS

## linear_model

### LogisticRegression

`coef_` : regression weights  

`LogisticRegression(C=0.01,multi_class='multinomial',penalty='l1',solver='saga', tol=0.1)` :  
*	`tolerance` : turn up for faster convergence

`fit(X,Y)` :  
`score(X_test,Y_test)` : test and get score (in `[0,1]`)  

## tree

Decision trees.  

`export_graphviz(Tree, out_file)` : export img of tree  

### DecisionTreeClassifier

`feature_importances_` : importance of each feature  

`DecisionTreeClassifier(criterion='entropy', random_state=0)` : get the tree  

`fit(X,Y)` :  
`predict(X)`:  
