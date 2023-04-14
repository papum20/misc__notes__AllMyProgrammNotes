# EXAMPLES

check if path is a directory:  
## README.md  
*	[README.md](./README.md)  

#include <sys/stat.h>  
bool isDir(const char *path) {  
	struct stat path_stat;  
	if(stat(path, &path_stat) != 0) return false;  
	return S_ISDIR(path_stat.st_mode);  
}  


## GRAPHS
  
ALBERO BINARIO:  
3 modi di visita (oltre a quello linea x linea):  
  
prefissa:  
void anticipata(vector <int> A, int pos){  
if (pos >= A.size()) return;  
cout << A[pos]<<" ";  
int lg = (int)(log(pos+1)/log(2));  
anticipata(A, pow(2,lg+1)+2*(pos+1-pow(2,lg))-1);  
anticipata(A, pow(2,lg+1)+2*(pos+1-pow(2,lg)));  
}  
  
infissa:  
void simmetrica(vector <int> A, int pos){  
if (pos >= A.size()) return;  
int lg = (int)(log(pos+1)/log(2));  
simmetrica(A, pow(2,lg+1)+2*(pos+1-pow(2,lg))-1);  
cout << A[pos] << " ";  
simmetrica(A, pow(2,lg+1)+2*(pos+1-pow(2,lg)));  
}  
  
postfissa:  
void posticipata(vector <int> A, int pos){  
if (pos >= A.size()) return;  
int lg = (int)(log(pos+1)/log(2));  
posticipata(A, pow(2,lg+1)+2*(pos+1-pow(2,lg))-1);  
posticipata(A, pow(2,lg+1)+2*(pos+1-pow(2,lg)));  
cout << A[pos] << " ";  
}  
  
  
  
ALBERO (BINARIO) DI RICERCA:  
valore nodo >= tutti valori sotto-albero sx, valore nodo <= tutti valori sott-albero dx  
  
ALBERO BINARIO COMPLETAMENTE BILANCIATO:  
ogni nodo ha 2 rami  


