# BASICS  
  
READ COMMAND LINE PARAMETERS:  
main(int argc, char **argv) : argc = **argv size; **argv = list of strings containing commands  
  
void* : pointer to anything  
  
  
OPERATORS:  
^ : xor  
~ : binary not  
val << n : binary-shift val by n digits  
val >> n :   
|= : assign and do or  
^= : assign and do xor  
## README.md  
*	[README.md](./README.md)  

#string : string (without quotes) to string with quotes  
a##b : concatenate values (e.g.: a=3,b=0, a##b=30)  
instruction1, instruction2 : evaluates both, considers second  
line1 \ line2 : concatenates two rows (written in different rows)  
“str1” “str2” : concatenates two constant strings  
  
KEYWORDS:  
register <assignment> : performs assignment and saves in a register  
	oss. : useful if used often  
	es.: register type asm(“register_name”) = value;  
volatile <type> var : var can change (in execution, for external factors)  
(instruction for compiler)  
  
TYPES :  
**_t : t for type  
NUMBERS:  
0b010.. : number in machine language (b=binary, x=hexadecimal)  
uintptr_t : dimensions of pointers in local pc  
uint64_t, … : relative to local pc, not to language (c)  
STRUCT :  
struct punto {type x;};  
punto p;  
punto *ptrpunto = &p;  
ptrpunto -> x = 102;     ==     (*ptrpunto).x = 102;  
  
POINTERS :  
tipo “a qualcosa”  
* : operatore di indirezione/deriferimento  
type *p (= &var)  
type var, *p; : *p=&var  
  
FILE* :  
UNION :  
like struct, but allocates memory just for one parameter, and instantiates only the used parameter  
es.: union { type1 field1; type2 field2;} t;  
es.:  
	struct coso {		//only instantiates persona or auto (size=24)  
		enum {persona, auto} tipo;  
union {	struct{char *nome; char *cognome;} upersona;  
struct {char *marca; char *modello} wauto;  
};  
  
  
es.:   
union {  
		char *args[4];  
		struct { char *help; char *file;};	//oss.: struct has no name  
	} opts;  
	//if you call opts.args, instantiates argos; if help, inst. help  
ENUM :  
  
es.: enum {field1, field2} t;  
DIRECTIVES:  
  


## PREPROCESSOR DIRECTIVES

#include <> “” : includes external file; <> tells to search file in C directories, “” in your dir  
#define MACRO VALUE : defines a macro  
	#define MACRO(...) : any number of args  
#if <condition> :   
	es.: #if 0 :   
#ifdef MACRO …some code... : includes some code if macro is defined  
#ifndef MACRO …some code... :  
#endif :  
inline type function() {...} : in compiling, function gets copied, not called (with a reference)  
typedef type / struct (name) {..} new_name; :  
  
extern : access (global) variable declared in another source file  
static : make (global) variable only visible from own source file;  
	local static variable is like a global variable  
  
GENERAL :  
MACRO : in compiling, replaced with calling text  



