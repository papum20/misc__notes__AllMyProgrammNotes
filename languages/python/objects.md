# OBJECTS  
  
## README.md  
*	[README.md](./README.md)  

## FUNCTIONS
  
### CONVERSION 
chr(int)		: int code to char  
hex(int)		: int to hex  
hexlify(bytes)		: bytes to hex  
ord(char)		: char to int code  
bytes.fromhex(str)	: return bytes obj from hex string  
byte 	s.hex()		: bytes to hex  
int(str, base=10)	: str to int, in base  
int.from_bytes(b, endianness)	: bytes to int, with endianness  
		endianness=”big”|”little”  
int.to_bytes(n, endianness)		: int to bytes;  
		n=number of bytes to use for conversion (at least equal to result)  
		endianness=”big”|”little”  
str.decode(charset=”utf-16”)	: bytes to char  
str.encode()			: char to bytes  
  
  
#### STRINGS:  
FORMAT:  
b”string” : encoded  
  
OLD:  
eval(string) : valuta stringa come espressione matematica  
sorted(lista...) : ordina  
  
str.endswith(carattere) : bool finisce con  
str.join([strings]) :  
str.len()  
str.lower() : dà tutto lowercase  
str.partition('c') = 'abcd' -> ['ab','c','d']  
str.replace(e1,e2) :   
str.rfind(substr) : trova substr e dà l'indice più alto (-1 se non trovato)  
string.split() : "Hello World" ->  ["Hello","World"  
str.swapcase() : swappa  
str.upper() : dà tutto uppercase  
str.zfill(int n) : prints zeroes before str such that there are at least n characters  
  
  
#### NUMBERS:  
complex() :  
float() :  
int() :  
  
abs(-n) = n (absolute)  
max()  
min()  
round(obj) : arrotonda  
  
complex.real() :  
complex.imag() :   
  
DATA STRUCTURES  
insieme.count(elem) : conta elem in insieme  
len(x) : length  
insieme.sort() : bool, se è ordinata  
  
  
#### LISTS  
list(elements) : convert to list  
	es.: list(range(..))  
sum(list, start=0) : sum of elements in list, starting from start parameter+first element,  
and using the result for the next summation  
  
list.extend(insieme) : aggiunge elem di insieme a list  
list.index(elem) : indice dell'elemento  
list.insert(index, elem) :  
list.pop([index]) : removes and returns element in index (last item if not specified)  
  
#### DICTIONARIES  
dic.get(index, exc=None) : returns value, or exc if not found (instead of error) (=None by default)  
.pop(key) : removes key (if present) and returns it  
  
.keys() : list of keys  
.items() : list of pairs <key,val>  
.values() : list of values  
  
### I/O :   
input()		:   
print(object(s), sep=separator, end=end, file=file, flush=flush)  
[ print(“qualcosa”, end = “,”) : aggiunge end alla fine ]  
  
### MISC :   
  
del(var)	: delete variable  
enumerate(iterable) : return iterator of pairs (number=0,1,.. element[number] of iterable)  
type()		:   
zip()		: empty iterator  
zip(arg)	: return an iterator to tuples, each with one element (from arg),  
		where arg is an iterable element  
zip(args…)	: (2+ args) return an iterator to tuples,  
where tuple i contains the i-th element of each arg (in order);  
args are iterable;  
if args of different length, the shortest one is used  
  
  
### CLASSES:  
super() : refers to base (parent) class (indirection)  
  
obj.__mro__ : Method Resolution Order : order in which methods are inherited  
  
FILE  
OPENING:  
var = open('nome_file', 'mode') : mode = 'r' (default): read, 'w': rewrite (deletes content);  
		file can be accessed/iterated as “list” of rows;  
		(creates a new file if not existing), 'a': append, ‘b’: binary mode				(for not-text files, as images, sound) (you can combine modes: es. “wb”)  
var.close() : close  
var.readlines() : var=list of lines  
var.read(int n) : var = string made of n bytes of file (default: all file)  
x = var.write('str') : writes str in the file; returns in x number of bytes written  
  
  



## CONSTANTS
  
__name__ = “__main__” if file is being run, else name of the file  
__main__ = name of the file being run  





