# OBJECTS  
  
## FUNCTIONS  
  
TYPES:  
  
(Template) swap(a, b) :  
  
TYPE CONVERSION  
atoi(char) : int di char(/str) (stdlib.h)  
stoi(str) : str in int (stdlib.h) (stoi(str,index,base)  
atof(str) : str in double  
to_string(int) : (string/iostream)  
  
char* str="123";  
int x; sscanf(s, "%d", &x); (stdlib.h)  
  
char *:  
sizeof(String) = int length  
  
<cstring>/<string.h>:  
strcat(String1, String2) : String1 = String1+String2  
strcmp(String1, String2) = int String1[i] - String2[i]  
strlen(String) = length String  
strncat(String1, String2, int) : String1 = String1+String2[0:n] (first n chars)  
strcpy(String1, string, int size) : String1 = string if size < max_length(String1)  
  
String:  
str.at(index) = s[]  
str.cpy(arr, obj) : copia obj (char, forse str) in arr  
str.c_char() : str in char  
str.empty() : true se vuoto  
str.erase(index, n)  
str.find(obj) : trova obj in str  
str.insert(index, str2) : inserisce str2 in str in ind  
str.length() : len  
str.substr(index, length) : sottostringa da index  
str.replace(index, n, str2)  
  
<cstdlib>:  
atoi(String) : to int (reads from start until it finds a non-num char)  
atol(String) : to long int (//)  
atof(String) : to float (//)  
<bits/stdc++.h>:  
reverse(str.begin(), str.end() ) : capovolge  
  
Float/Double:  
abs() :  
ceil() : arrotonda per eccesso  
cos() : coseno  
log() : logaritmo naturale	<math.h>  
log10() : logaritmo base 10	<math.h>  
log(a)/log(b) : logaritmo di a base b	<math.h>  
pow() :  
sin() : seno  
sqrt() :  
  
CLASSES:  
VECTOR:  
vect.assign(elem, quante volte) : aggiunge “quante volte” volte elem al vector  
vect.push_back(elem) : come .append  
vect.resize(n,val) : dà lunghezza n a vettore, assegnando val se specificato (fa usare cin)  
  
STREAM:  
<iomanip>:  
cout << setprecision(int) << num : total number of digits displayed  
cout << setw(int) : number of char printed  
  
FILE:  
#include <cstdio>  
freopen(char *filename, char mode, FILE *stream) : redirects stream from current to  
filename (if NULL, only changes mode), using mode (‘r’=read, ‘w’=(over)write,  
‘a’=append, ‘r+’,’w+’,’a+’=with update)  
  
INPUT:  
getline(stream(cin), str, char limite(default:\n)) : prendi input riga fino a limite(escluso)  
  
cin.clear() :   
cin.getline(String, int m+1) : String = first m char of input (+1 for ‘\0’)  
cin.ignore(int max, char delim) : ignora input fino a là (utile con getline)  
  
RANDOM:   
(#include <ctime><cstdlib>)  
srand(time(NULL));  
cout << rand()%10 +1;  
(rand=pseudo-random; srand=seed x rand; time=time da 1/1/1970)  
  
  
  
  
<ctime>/<time.h>:  
CLOCKS_PER_SEC : processor’s clock ticks per second  
  
clock() : clock ticks consumed by processor  
time() : seconds  
	time(NULL) : current time  
  
<sys/stat.h>  
struct stat {  
	st_mode : file mode (type, i.e. directory…)  
	}  
MACRO S_ISDIR(stat_object.st_mode) : 0 if not dir, else non-zero  
stat(const char *path, struct stat *buf) : fills buf with information about pat;  
					return 0 upon completion, -1 otherwise  
  
ios_base::  
void sync_with_stdio(bool sync  = true) : true: syncs i/o streams with std C streams  
(false can be faster)  

FUNZIONI:  
freopen(“file”,”r”/”w”,stdin/stdout)  
  
  
METODI:  
stream.eof() : bool, se lo stream (come cin) è arrivato alla fine del file  

## DATA STRUCTURES

  
SET	//elementi unici ordinati in modo crescente  
#include<set>  
auto set_name = set<type>();  
auto set_name = set<type, decltype(ordine)> (ordine);	//segue l’ordine scelto  
  
//WITH PAIRS  
struct comp{  
	bool operator()(pair<int,int> a, pair<int,int> b){  
…  
set<pair<int,int>,comp> set_name  
  
//WITH STRUCT  
struct{...}  
bool operator<...  
set <struct> set_name;  
  
METODI:  
s.begin() : puntatore del primo elem  
s.end() : puntatore ultimo elem  
s.erase(elem) : rimuove elem  
s.find(elem) : trova puntatore di elem  
  
x accedere elementi:  
next(s.begin() / end(), indice) : sola lettura  
std::set<type…>::iterator it_name = s.begin() / s.end();	poi ++/-- ....  
  
MULTISET	//come set, ma ammette duplicati  
  
  
QUEUE	//(FIFO) vettore dove si può solo aggiungere e togliere all’inizio  
  
STACK	//(FIFO) vettore dove si può solo aggiungere e togliere in fondo  
  
PRIORITY_QUEUE	//queue con priorità  
priority_queue <type, vector<type>(del sottoinsieme), class comparator> nome_queue;  
class comparator: classe con comparatore (funzione bool) x ordinare  
class comparator{  
public:  
bool operator() (type a, type b){  
return …qualcosa;	}  
};  
  
  
UNORDERED_MAP	//dizionario (key-value, niente ordine)  
unordered_map<key type, value type> nome_dizionario;  
  
  
VECTOR  
#include<bits/stdc++.h> o <vector>  
vector<type> vector_name(opzionale: lunghezza, valore default);  
  
for(auto x : V){		//le graffe sono opzionali  
cout << x;  
}  
  
METODI:  
v.push_back(elem) : aggiunge alla fine  
  
  
  
ALGORITHM  
sort(v.begin(), v.end(), funzione lambda (opzionale)) : ordina secondo lambda  
e.g.: sort(v.begin()+2, v.end()-1, funzione lambda (opzionale))  
