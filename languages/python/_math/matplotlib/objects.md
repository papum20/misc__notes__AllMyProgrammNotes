# OBJECTS  
  

  
matplotlib  
  
matplotlib.pyplot  
#functions of same dimensions as axes (vectors)  
#plots only with 2 vectors / matrix of 2 cols  
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
subplot(rows, cols, pos) : pos=index  
(e.g. graph made of r*c subgraphs, numbered 1..r*c, row by row)  
suptitle(string) :  
title(string, fontsize=<int>) : (accepts pseudo-latex text)  
	title(“[-$\pi$, pi]”) : pi  
xlabel(string) :  
ylabel(string) :  
  