# OBJECTS  
  

  
matplotlib  
  
## matplotlib.pyplot  
// functions of same dimensions as axes (vectors)  
// plots only with 2 vectors / matrix of 2 cols  
figure(figsize=) : dimensions/size  
grid() :  
legend([list]) :  
loglog() : graph with logarithmic scale  
plot(x, y, color=”string”, linewidth=<int>, marker=’char’) :  
	plot(x, y, “b*”) : color+marker  
rc() : global configurations  
	rc(“font”, size=<int>) : font size  
semilogx() : graph with logarithmic scale (on x)  
semilogy() : //  
show() :  
subplot(rows, cols, pos) : subplot at pos  
*	pos=index (1,2..)  
*	pos=(i,j) : (tuple) use from index i to j  
(e.g. graph made of r*c subgraphs, numbered 1..r*c, row by row)  
suptitle(string) :  
title(string, fontsize=<int>) : (accepts pseudo-latex text)  
	title(“[-$\pi$, pi]”) : pi  
xlabel(string) :  
ylabel(string) :  
  
### axis
// returned by subplot
`.imshow(IMG, str cmap=, int vmin=, int vmax=)` :  
*	add image to axis  
*	cmap : color  
	='gray'
*	vmin, vmax : values range