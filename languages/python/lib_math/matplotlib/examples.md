# EXAMPLES

Plot histogram:
```py
def plot_hist(a,bins=10,title=None):
	plt.figure(tight_layout=True)
	plt.hist(a,bins=bins)
	if title:
		plt.title(title)
	plt.show()
```