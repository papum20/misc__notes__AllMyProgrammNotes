# BASICS  
  
stile imperativo : assegnamenti (lungo : )  
stile funzionale : funzioni di funzioni (corto)  
aliasing (tra variabili e/o puntatori) : variabili diverse puntano a stesso oggetto  
  
  
  
OPERATORI  
  
PRECEDENZA:  
.  
parametro  
! + - & *  
per puntatori  
* / %  
  
  
+ -  
  
  
<< >>  
stream  
< <= >= >  
  
  
== !=  
  
  
&&  
  
  
||  
  
  
  
  
DEFINIZIONI:  
operatori overloaded: fanno più cose (es. + usato da int e float); usati in base al contesto  
type safety: ogni var deve essere usata con operatori e funzioni del suo tipo --> sicuro		         niente errori  
  
OPERATORI:  
A == B	: (assegnamento) A considerato come indirizzo, B come valore  
++var	: aumenta di uno var e restituisce var  
var++	: restituisce var e aumenta di uno var  
&& 	: AND  
||	: OR  
!	: NOT  
&	: BITWISE AND (n & (n-1) dà 0 se n è potenza di 2) : compara tutti i bit n / n-1 di		 numero binario e return false se tutti opposti (1000 & 0111 = false)  
|	: BITWISE OR  
^	: BITWISE XOR  
  
(x==y)? (a:b)    : se x==y, allora è a, altrimenti b  
  
  
  
  
SEQUENZE DI ESCAPE  
  
x stampare caratteri speciali:  
\n 	: newline  
\t	: tab  
\\ 	: x stampare \  
  
  
BASI  
  
## README.md  
*	[README.md](./README.md)  

#direttiva al preprocessore (eseguito non nel programma ma nella fase preliminare)  
(es.: #include <iostream>) include libreria (insieme di definizioni, funzioni…)  
using namespace:definisce tipo di namespace, ovvero come interpretare alcune parole (tipo cin e cout)  
  
  
typedef tipo nome_tipo;	//rinomina un tipo  
  
VARIABILI GLOBALI: valide in tutto il codice  
#define var value;	//costante  
const type var (= value);	//costante  
  
  
//funzione x inizio e fine programma:  
int main(){  
return: ritorna (a fine main: return 0; significa fine (è messo automaticamente) )  
}  
  
  
commento: /* commento (più righe) */ ; // commento (una riga)  
  
  
  
  
  
  
STATEMENTS AND LOOPS  
  
do {	}  
while(condition);  
//fa almeno una volta  
  
val =value  
switch (val) {  
    case value:  
        ...  
        (break; oppure usa le graffe {} nel case)  
    default:  
        è come else;  
}  
  
try{  
(opzionale) throw("type" "var")  
}  
catch(**){	}  
** : error, var (con throw), (...) per tutto  
  
  
identifier:  
	...  
goto identifier //goes to indentifier instruction  
  
  
  
OUTPUT  
cifre decimali:  
#include <iomanip>  
cout << fixed(/scientific) << num;  
// fixed: num not in scientific notation  
  
cout << setioflags(ios::fixed) << setprecision(cifre d.) << x;  
cout << setioflags(ios::floatfield) << setprecision(cifre tot (d. e non)) << x  
  
STRUCT:  
  
campi  
  
FUNZIONI:  
scope : portata dell funzione, blocco in cui è valida  
catena statica : non annidamento funzioni (catena max 1)  
formal-parameter : parameter when function declared (declaration)  
actual-parameter : parameter when called (expression)  
/*	(function declaration) type f(type (name),type (name),…);	//name not mandatory  
	//comment (precondition (input) and postcondition (output))  
main()...  
(function definition)	*/  
procedural abstraction : using a function without knowing how it works, but just what it does (information hiding)  
  
parameter passed as value by default (without &) : types, structs  
parameter passed as reference by default (without &) : array  
  
HEADER:  
//library.h  
function declaration;  
//library.cpp  
#include “library.h”  
function definition  
//source.cpp  
#include “library.h”  
…  
  
  
#include “path” : (es. ../../folder…)  
	../ to go in the “parent” folder  
  
from external folder (for ECLIPSE):  
properties/”C/C++ General”/”Paths and symbols”: add folder in “Includes”/”Gnu C++” and 							 "Source Location"/"Add Folder"  
#include “library.h”  
  
  
NAMESPACE:  
// scope with an identifier  
one {  
function()..  
}  
two {  
	function()..  
}  
main()  
one::function()	  
two::function()  
  
using one::function; / using namespace one;  
main()  
	function()  
  
FUNZIONE LAMBDA:  
auto foo = [] (parametri) {	//tipo auto, perché non ha tipo  
return...;  
};  
  
  
  
MEMORIA :  
heap	: dove allocati nuovi blocchi di memoria (permanente) (es. new, return di funzioni)  
stack	:   
//entrambe dimensioni dinamiche  
  
CLASSI:  
  
Definizione classe:  
class class_name {  
	public:  
		parameter;  
		method(){...};  
		class_name() {...};	//CONSTRUCTOR  
	protected:	//default  
		parameter;  
		method(){...}  
};  
  
COSTRUTTORI:  
chiamata: 	class_name x();  
		class_name x = class_name();  
  
definire metodo fuori da classe:  
type class_name::method_name() {...};  
  
this : puntatore a oggetto stesso  
  
EREDITARIETÀ:  
class sub_class : public parent_class { … }  
  
sottoclasse ha della superclasse (classe padre):  
 - stessi parametri (non modificabili)  
 - stessi metodi (tranne costruttore) (modificabili)  
 - eventuali parametri e metodi aggiuntivi  
  
overriding: modifica metodi padre  
costruttore: all’inizializzazione invocato prima costruttore di padre e poi di sottoclasse  
		-> costruttore padre deve avere valori di default  
sub_class(sub par…) : parent_class(parent par…) {	//parent constructor  
… }  
sottotipaggio: oggetto superclasse può essere sostituito da sottoclasse in variabili,			 puntatori, parametri, valori di ritorno  
 (non contrario)  
static dispatch: oggetto di superclasse = oggetto di sottoclasse : a quale					 dichiarazione fanno riferimento i metodi dell’oggetto superclasse quando			 invocati (risposta: del padre (static) )  
ridefinire funzione partendo da definizione di parent:  
parent_class {  
	some_method() {...}  
};  
sub_class : parent_class {  
	some_method() {  
		parent_class::some_method();  
		…  
	}  
};  
  
STREAM:  
  
FILE *stdin : standard input stream  
FILE *stdout : standard output stream  


## TYPES
VARIABILI:  
type (es. int) (definisce) variable (identifier)  
type variable = value  
type variabileA, variabileB  
  
variabili dinamiche 	: (new) create e distrutte mentre programma in esecuzione  
altre variabili 		: create a invocazione funzione/programma, distrutte a fine/uscita funz  
  
auto:  
	automatico (necessario per funzioni lambda)  
  
int :  
signed: positivi e negativi  
unsigned: positivi  
long: doppio della lunghezza default  
short: metà della lunghezza default  
float:  
float: 4 byte  
double: 8 byte  
long double: 8/16 byte  
  
string:  
""  
va inclusa (#include <string>;/<iostream>)  
  
char = character:  
' .. '  
singolo carattere  
  
VAR :  
pascal case: BackColor  
camel case: backColor  
  
Array :  
type arr[len] = {elem,elem...}  
elem dello stesso tipo  
n elem <= len  
indici  
arr[] = {1,2,3} : len è 3  
multidimensional : arr[seize1][seize2]..[N]  
2-dim. : arr[rows][columns]= {{..},{...},...}  
  
Void :  
funzione senza return  
  
String :  
char s[length] = “string”;  
// ’\0’ added automatically  
// (if shorter than length, else out of bound Error)  
char s[ ] = “string”;  
// length determined automatically  
must contain the ‘\0’ char, meaning null char = end of string  
length = length - 1 (because of ‘\0’)  
input ends with space ‘ ‘  
  
POINTER :  
type *p, n;	//p type pointer, n type  
  
NULL (costante) 	: puntatore vuote, “a niente"  
(type *p=) new type	: puntatore a nuovo blocco di memoria (alloca) (variabili dinamiche)  
* 			: dereferenziazione (*p=valore di oggetto puntato da p)  
&var (ampersand)	: indirizzo di var  
delete	p		: delocalizzazione blocco di memoria: rende disponibile per altro				  pointer, non cancella (delete NULL non fa niente)  
  
aliasing (tra puntatori) 	: puntatori puntano stesso indirizzo  
dangling pointer (pendente)	: dopo delete, valore indefinito  
buona regola:  
delete p;  
p = NULL;  
  
LISTS :  
struct list {  
	int val;  
	list *next;  
};  
  
//head non list, ma puntatore a list  
list* head = new list;  
head -> val = some_int;  
head -> next = NULL (es) ;  


## PREPROCESSOR DIRECTIVES

  
#endif	: ends code starting at ifdef / ifndef  
#ifdef MACRO : executes following code (until endif) if MACRO defined  
#ifndef MACRO : //  
#include<...> : include (librerie standard)  
#include"..." : include (librerie create, nella stessa directory)  
#define const_name const_value  
#define const_name(var) (changed_const) : when called const_name(x) replaces with						 	changed_const  
#typedef known_type new_type;  
  
  
  
how to avoid multiple includes of same file:  
#ifndef FILE_H  
#define FILE_H  
code  
#endif  


## STREAMS
  
cin>> = computer input  
cout<< = computer output  
<< = insertion operator  
  
cout:  
a capo:  
cout << … << endl;  
cout << … ;  
  
= \n  
  
  
------  
  
  
string a = "123";  
stringstream bo(a);   //(sstream), stringa in num  
int x; bo>>x; //x=123  


