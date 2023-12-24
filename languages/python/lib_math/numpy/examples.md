# EXAMPLES

Bool expression in indexing:
```py
mean_digits = np.zeros((10,784))
for i in range(0,10):
	mean_digits[i]= np.mean(x_train[y_train==i], axis=0)
show_samples(mean_digits)
```

Convert a matrix of floats to one of bools, with the given condition:
```py
x_discr = x >.5
```
