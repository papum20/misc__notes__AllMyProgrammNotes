# BASICS  
  
## README.md  
*	[README.md](./README.md)  

#!/usr/bin/env python : rende file eseguibile da shell senza comando python  
  
SYMBOLS:  
  
# comments (ignored by compiler) (octothorpe/hash symbol)  
__ dunder : double underscore  
“””  
multiline string, also used as multiline comment (read by compiler but ignored)  
“””  
  
OPERATORS:  
  
* = wildcard notation  
*data_structure : returns elements in data_structure, not only the data_structure as only one element  
*args : gets a list of arguments of any length  
	e.g. def foo(*args)	: any args  
**kwargs : gets a dictionary of args of any length (identifier: value)  
(args, kwargs, kwds are conventions)  
_ : last result  
  
ARITHMETIC OPERATORS:  
>= / <=		### EVEN FOR EXPRESSIONS AS a <= b <= c  
// integer division  
% remainder  
**: power  
es.: “%.2f”%var : prints n with 2 decimal digits  
  
CONCATENAMENTO, RIPETIZIONE (str):  
+ (es. 'ca'+'sa' >>> 'casa')  
* (es. 'ca'*2 >>>'caca')  
  
COMPARISON:  
!= diverso  
  
BOOLEAN:  
and: TRUE se entrambi veri  
or: TRUE se almeno uno falso  
not: TRUE se entrambi falsi  
in : contained  
is : if variables refer to the same object (not only they have the same value)  
  
BINARY:  
>> Bitwise right operator (sposta cifre in binario, trasformando numer)  
<< Bitwise left operator (//)  
  
STATEMENTS:  
if-elif-else :  
for :  
try - except-…-except - finally :  
e.g.:  
try :  
	...  
	raise Error  
	raise Error(string)  
except :  
	…  
	raise	# RE-RAISES SAME ERROR WHICH OCCURRED  
except <error> :  
	...  
else :  
	# IF NO ERROR  
except(Error1, Error2):	### () FOR MORE EXCEPTIONS  
finally :  
	# EXECUTED ANYWAY  
  
while :  
with <value> as <identifier>	: create var <identifier> only valid in indented block;  
				“inverse” operations (“deallocation”) at the end;  
	e.g. with open(“file”,”r”) as f:	use file, without need to close it at the end  
  
KEYWORDS:  
assert bool : if false returns AssertionError  
assert bool, “string” : prints string, then returns AssertionError  
break :  
continue :  
pass : empty command (do nothing)  
raise <Error>  
raise <Error>(string) : also prints string  
  
  
TYPES:  
  
VARIABLES:  
int: intero  
float: reale  
complex:   
	es.: n=1+2j  
bool: booleano (True/False)  
complex: complesso  
str: stringa (testo)  
byte: byte  
None : "empty" value (returned by functions without return value)  
  
STRINGHE:  
usare ' o "  
\ è escape character : prima di segni che non puoi mettere in stringhe  
a capo: \n oppure """.."""  
  
DATA STRUCTURES:  
dictionary = {key:value} : (only immutable objects as keys)  
  
FUNCTIONS:  
functions=objects  
def f():...  
g=f  
	def(fun,x):  
		return fun(x)  
  
def f(*args):		### GETS A LIST OF ARGUMENTS OF ANY LENGTH  
def f(**kwargs):  
### GETS A DICTIONARY OF ARGS OF ANY LENGTH (IDENTIFIER: VALUE)  
  
LAMBDA FUNCTIONS:  
lambda some_function  parameter1...parameter_n: some_output  
  
LIBRARIES:  
3 kinds:  
the Standard Library (pre-installed)  
from external sources (many in Python Package Index PyPI, sometimes pre-installed)  
written by you  
MODULES:  
import module_name  
from module_name import var1, var2, var3  
from module_name import * : imports all objects  
import module_name as new_module_name  
  


## DATA STRUCTURES
  
INDEXING E SLICING  
s[indice] : elemento in posizione indice (n) (anche negativo, così parte dalla fine)   
(s=lista, tupla... qualsiasi cosa)  
sequenza[inizio:fine] (incluso:escluso)  
(anche solo inizio, fine o nessuno)  
partendo da zero  
l=[8,0,4,6,1]  
del(l[1::3])  
>>l=[8,4,6]  
a=[1,2,3]  
a[::-1] = 3,2,1  (sarebbe ogni quanto)  
a[::-2] = 3,1  
a[::-3(o piu)] = 3  
  
s='sequenza(/parola)'     ??????  
  
sum(list) : somma elementi  
  
  
TUPLE:  
sequenza immutabile di oggetti eterogenei  
es. t = (a, b, c)   
elementi tra ( ) separati da ,  
tupla da 1: serve ,  
tupla da 0: ( )  
faster than lists  
OPERAZIONI:  
can be created without () : t = a,b,c  
assegnamento: >>t=('Ciccio','Caputo',30,11)  
>>(nome,cognome,età,numero)=t  
>>a,b,*c=('Ciccio','Caputo',30,11)  
output: b=30 11)  
  
LISTA:  
sequenza mutabile di oggetti omogenei  
elementi tra [ ] separati da ,  
lista da 0: [ ]  
  
OPERAZIONI:  
lista.append(elem): aggiunge elem alla fine della lista;  
lista.extend(seq): estende la lista aggiungendo alla fine gli elementi di seq;  
lista.insert(indice, elem): aggiunge elem alla lista in posizione indice;  
lista.pop(): rimuove e restituisce l’ultimo elemento della lista;  
lista.remove(elem): trova e rimuove elem dalla lista;  
lista.sort(): ordina gli elementi della lista dal più piccolo al più grande;  
lista.reverse(): inverte l’ordine degli elementi della lista;  
lista.copy(): crea e restituisce una copia della lista;  
lista.clear(): rimuove tutti gli elementi della lista;  
del rimuove 'elem'  
lista.max()  
lista.min()  
lista.count(obj)  
  
( combinazione tuple-lista: lista di tuple )  
  
DIZIONARI:  
sequenza mutabile di elementi formati da chiave(univoca) e valore  
dic = {key:value} : (only immutable objects as keys)  
  
d={'firs':1,'second',2}   
è uguale a  
d = dict(first=1,second=2)  
  
OPERAZIONI:  
dizionario[key] = value aggiunge item  
 del dizionario[chiave] rimuove item  
key in dic = bool  
  
d.items() Restituisce gli elementi di d come un insieme di tuple  
d.keys() Restituisce le chiavi di d  
d.values() Restituisce i valori di d  
d.get(chiave, default)	Restituisce il valore corrispondente a chiave se presente, altrimenti il valore di default  
d.pop(chiave, default)	Rimuove e restituisce il valore corrispondente a chiave se presente, altrimenti il valore di default  
d.popitem() Rimuove e restituisce un elemento arbitrario da d  
d.update(d2) Aggiunge gli elementi del dizionario d2 a quelli di d (se presenti elem con stessa chiave, li andranno a sostituire)  
d.copy() Crea e restituisce una copia di d  
d.clear() Rimuove tutti gli elementi di d  
  
SET E FROZENSET:  
insieme non ordinato di oggetti unici (se alcuni uguali, vengono rimossi automaticamente) (set mutabile, frozenset immutabile)  
elementi tra {} separati da ,  
set vuoto: set()  
  
METODI:  
set.add(elem): aggiunge elem al set;  
set.remove(elem): rimuove elem dal set (dà KeyError se non presente);  
set.discard(elem): rimuove elem dal set se presente;  
set.pop(): rimuove e restituisce un elemento arbitrario del set;  
set.copy(): crea e restituisce una copia del set;(unico compatibile con frozenset)  
set.clear(): rimuove tutti gli elementi del set;  
s1.isdisjoint(s2) 	Restituisce True se i due set non hanno elementi in comune  
s1 <= s2 	s1.issubset(s2) 	Restituisce True se s1 è un sottoinsieme di s2  
s1 < s2 		Restituisce True se s1 è un sottoinsieme proprio di s2  
s1 >= s2 	s1.issuperset(s2) 	Restituisce True se s2 è un sottoinsieme di s1  
s1 > s2 		Restituisce True se s2 è un sottoinsieme proprio di s1  
s1 | s2 | ... 	s1.union(s2, ...) 	Restituisce l’unione degli insiemi (tutti gli elementi)  
s1 & s2 & ... 	s1.intersection(s2, ...) 	Restituisce l’intersezione degli insiemi (elementi in comune a tutti i set)  
s1 - s2 - ... 	s1.difference(s2, ...) 	Restituisce la differenza tra gli insiemi (elementi di s1 che non sono negli altri set)  
s1 ^ s2 	s1.symmetric_difference(s2) 	Restituisce gli elementi dei due set senza quelli comuni a entrambi  
s1 |= s2 | ... 	s1.update(s2, ...) 	Aggiunge a s1 gli elementi degli altri insiemi  
s1 &= s2 & ... 	s1.intersection_update(s2, ...) 	Aggiorna s1 in modo che contenga solo gli elementi comuni a tutti gli insiemi  
s1 -= s2 | ... 	s1.difference_update(s2, ...) 	Rimuove da s1 tutti gli elementi degli altri insiemi  
s1 ^= s2 	s1.symmetric_difference_update(s2) 	Aggiorna s1 in modo che contenga solo gli elementi non comuni ai due insiemi  

## CLASSES

CLASS:  
class class_parent:  
###function called when new object instantiated  
	def __init__(self, parameter1):  
		###define attribute  
		self.parameter1 = parameter1  
  
  
INHERITED (CHILD) CLASS:  
class child_class(class_parent):  
	def __init__(self, parameter1):  
		###super() makes child inherit methods and properties  
		super().__init__(parameter1)  
  
  
STATIC METHOD:  
doesn’t need a class object to be instantiated in order to be called  
class some_class:  
	@staticmethod  
	def some_method():  
		pass  
  
call: some_class.some_method()  
  
2. some_class.newMethod = staticmethod(some_class.some_method)  


