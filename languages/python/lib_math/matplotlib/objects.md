# OBJECTS  
  
## matplotlib.pyplot  
// functions of same dimensions as axes (vectors)  
// plots only with 2 vectors / matrix of 2 cols  

`show()` :  
`subplot(rows, cols, pos)` : subplot at pos  
*	`pos=index (1,2..)`  
*	`pos=(i,j)` : (tuple) use from index i to j  
*	e.g.: graph made of `r*c` subgraphs, numbered `1..r*c`, row by row  

### plot

`loglog()` : graph with logarithmic scale  
`plot(x, y, color=”string”, linewidth=INT, marker=’char’)` :  
*	`plot(x, y, “b*”)` : color+marker  

`imshow(IMG, str cmap=, int vmin=, int vmax=)` :  
*	add image to axis  
*	`cmap` : color  
*	`cmap='gray'` : grey mask
*	`vmin, vmax` : values range

`scatter()` : graph as scatter points  
`semilogx()` : graph with logarithmic scale (on x)  
`semilogy()` : //  

### configure plot properties

`axis(val)` : set axises
*	`val="on"` : show
*	`val="off"` : don't show

`figure(figsize=)` : dimensions/size  
`grid()` : configure stuff like grid lines  
`legend([list])` :  
`suptitle(string)` :  
`title(string, fontsize=INT)` : (accepts pseudo-latex text)  
*	`title(“[-$\pi$, pi]”)` : pi  

`xlabel(string)` :  
`ylabel(string)` :  

### misc

`rc()` : global configurations  
*	`rc(“font”, size=INT)` : font size  
  
### matplotlib.pyplot.axis
// returned by subplot


