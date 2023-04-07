# SORTING  
  
SELECTION-SORT  
per ogni indice i:  
trova l’elemento più piccolo nel sotto-array i...length  
scambia(array[i], min)  
  
void selection_sort(int a[], int length){  
int i, j, min ;  
for (i = 0 ; i < length-1 ; i = i+1){  
min = i ;  
for (j = i+1 ; j < length ; j = j+1)  
if (a[min] > a[j]) min = j ;  
scambia(a[i], a[min]) ;   
}  
}  
  
BUBBLE-SORT  
“fa galleggiare prima bolla più grande”  
scambia i valori a due a due se uno più piccolo dell’altro  
  
void bubble_sort(int a[], int length){  
int i, j ;  
for (i = 0 ; i < length ; i = i+1){  
for (j = 0 ; j < length-1-i ; j = j+1)  
if (a[j] > a[j+1]) scambia(a[j], a[j+1]) ;  
}  
}  
  
BINARY SEARCH  
int bin_search(int a[], int length, int k){  
bool found = false ;  
int l = 0 ; int r = length ;  
int m ;  
while (!found && (l < r)){  
m = (r + l)/2 ;  
if (a[m] == k) found = true;  
else if (a[m] > k) r = m ;  
else l = m+1 ;  
}  
if (found) return (m) ;  
else return(-1) ;  
}   
  
QUICKSORT  
.  
  
MERGESORT  
void mergesort(int A[], int l, int r) {  
	if(l < r) {  
int m = (l+r) / 2;  
	mergesort(A, l, m);  
mergesort(A, m, r);  
merge(A, l, m, r);  
}  
}  
  
  



