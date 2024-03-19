# OBJECTS  
  

## numpy  
`arange(int n)` : array={0..n-1}  
`atleast_2d(array)` :  
*	`for 1d array, adds empty dimension (useful for transpose)`  
`array copy(array)` :  
`clip(array, min, max)` : return the `array` with values clipped in range  
`diag(1-D_array, k=0)` : matrix with 1-D_array on diagonal, k=which diagonal  
*	`diag(2-D_array)` : vector with matrix’s diagonal  
`dot()` :   
`array eye(int n, <int m>,)` : identity matrix (ones on diagonal); n=cols, m=rows  
`linspace(int start, int end, num=n)` : returns n number at same distance between each other  
`matmul(array1, array2)` : product row by column  
`max(array, axis=)` :  
`mean(array, axis=)` : average  
`min(array, axis=)` :  
`multiply(a1, a2)` : mul one by one  
`array ones()` :   
`outer()` :   
`prod()` : product over axis  
`range(max)` : array of ints < max  
`reshape(array)` : keeps elements, changes shape  
`std(matrix)` : standard deviation  
`sum(matrix, axis=)` : sums, along axis  
`transpose(matrix)` :  
*	`for a 1d array, doesn't do anything;`
*	`do instead `np.atleast_2d(A).T`  
`tril(matrix)` :   
`triu(marix)` : upper diagonal  
`array zeros(lunghezza(int)/dimensioni(tupla), tipo(default:float), qualcosa di memoria('C'/'F', default) )` : array full of zeroes  

### functions

`cos(array:Array)` : (like `sin`)  
`sin(array:Array)` : compute sin for each point in `array`  

## TYPES  
// float32  
class array:  

## ATTRIBUTES  
`object` : n-dimensional array (list/list of lists… or tuple for 1-dimension);  
`int size` : number of elements (total)  
`tuple shape` : dimensions  
`dtype` : type of elements  
`int ndim` : number of dimensions  
`T` : transposed  

## METHODS  
`array(object, DTYPE=TYPE)` : constructor  
  
## numpy.random  
`normal(loc=, scale=, size=)` : random numbers with gauss distribution  
`rand(int n, int m)` : random array, shape = n*m  
`randint(low, high=, size=, dtype=)` : rand with ints, in range  
`seed(s:int)` : set seed `s`  

## numpy.linalg (linear algebra)  
`cond()` :  
`inv()` : inverse  
`matrix_rank(matrix)` :   
`norm()` :  

## README.md  
*	[README.md](./README.md)  

