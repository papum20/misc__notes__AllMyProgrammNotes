# OBJECTS

## Data structures

### pandas.DataFrame

`DataFrame(dataset: dict[str,np.array])` : a collection of `Series`, each as a column of a table with a name (header)  
*	`dataset` : dict with key string (`series` name), value (1-dimension) np array (`series` values array)

`copy()` : return copy  
`corr(method)` : get correlation matrix  
*	`method='pearson'` : use Pearson coefficient  

`describe()` : print some statistics on data  
`head(n: int)` : print first `n` rows  

#### convert
`to_csv(path, index: bool)` :  
`to_excel(path, index: bool)` :  

#### edit
`drop_duplicates()` : remove duplicate rows   
`dropna()` : remove rows with missing values (NaN)  

`group_by(name: str)` : group table by `name`  


### pandas.Series

`Series()` : a named collection (1-dimension array and a name for the series)  

## Files
`read_csv(path)` :  
`read_excel(path)` :  

