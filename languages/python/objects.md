# OBJECTS  
  
## FUNCTIONS
  
CONVERSION :   
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
  
  
STRINGS:  
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
  
  
NUMBERS:  
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
  
  
LISTS  
list(elements) : convert to list  
	es.: list(range(..))  
sum(list, start=0) : sum of elements in list, starting from start parameter+first element,  
and using the result for the next summation  
  
list.extend(insieme) : aggiunge elem di insieme a list  
list.index(elem) : indice dell'elemento  
list.insert(index, elem) :  
list.pop([index]) : removes and returns element in index (last item if not specified)  
  
DICTIONARIES  
dic.get(index, exc=None) : returns value, or exc if not found (instead of error) (=None by default)  
.pop(key) : removes key (if present) and returns it  
  
.keys() : list of keys  
.items() : list of pairs <key,val>  
.values() : list of values  
  
I/O :   
input()		:   
print(object(s), sep=separator, end=end, file=file, flush=flush)  
[ print(“qualcosa”, end = “,”) : aggiunge end alla fine ]  
  
MISC :   
  
del(var)	: delete variable  
type()		:   
zip()		: empty iterator  
zip(arg)	: return an iterator to tuples, each with one element (from arg),  
		where arg is an iterable element  
zip(args…)	: (2+ args) return an iterator to tuples,  
where tuple i contains the i-th element of each arg (in order);  
args are iterable;  
if args of different length, the shortest one is used  
  
  
CLASSES:  
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
  
  
LIBRARIES  
  
base64  
import base64  
  
.b64decode(str)	: decode str in base 64  
  
BeautifulSoup  
import bs4  
  
OBJECTS:  
.BeautifulSoup :   
BeautifulSoup(DOC, PARSER)	: init object with DOC containing html document  
	PARSER=”html.parser”	: (default)  
.extract()	: (?)  
.find(...)	: (works like find_all)  
.find_all([ELEM], [class_=CLASS], [ATTRS={...}], [recursive=BOOL])	:  
return array of all html elements of type ELEM, class CLASS, attributes specified, recursive if also search descendants  
.find_all([string=STR])	: match STR (text)  
	e.g. str=”p” for p elements  
prettify()	: return pretty doc  
  
tag :   
.get(ATTR)	: ATTR value  
.string	: text in element  
  
datetime  
date(year, month, day) : allows operations between dates  
today()  
  
hashlib  
// hashing  
.md5(encoded_str) : return the md5 of an encoded string  
md5 object:  
.digest() : equivalent byte value  
.hexdigest() : equivalent hexadecimal value  
  
json  
dump(obj, file) : saves object as json string in file  
dumps(obj) : serializes object as json string  
	e.g. json.dumps(dict)  
load(file) : returns deserialized object from file  
loads(s) : deserializes a json string and returns a python object  
  
kivy  
self.ids.idname : access to widget in kv file with id:”idname”  
  
math  
ceil(int) : arrotonda per eccesso  
floor(int) : arrotonda per difetto  
sqrt(int) : square root  
  
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
  
numpy  
array[row, col] : access  
vect1*vect2 : element by element  
matrix1 @ vect2 : product row by column  
  
arange(int n) : array={0..n-1}  
array copy(array) :  
diag(1-D_array, k=0) : matrix with 1-D_array on diagonal, k=which diagonal  
	diag(2-D_array) : vector with matrix’s diagonal  
dot() :   
array eye(int n, <int m>,) : identity matrix (ones on diagonal); n=cols, m=rows  
linspace(int start, int end, num=n) : returns n number at same distance between each other  
matmul(array1, array2) : product row by column  
max(array, axis=) :  
mean(array, axis=) : average  
min(array, axis=) :  
array ones() :   
outer() :   
prod() : product over axis  
range(max) : array of ints < max  
reshape(array) : keeps elements, changes shape  
std(matrix) : standard deviation  
sum(matrix, axis=) : sums, along axis  
transpose(matrix) :  
tril(matrix) :   
triu(marix) : upper diagonal  
array zeros(lunghezza(int)/dimensioni(tupla), tipo(default:float), qualcosa di memoria('C'/'F', default) ) : array full of zeroes  
  
  
TYPES:  
float32  
class array:  
ATTRIBUTES:  
object : n-dimensional array (list/list of lists… or tuple for 1-dimension);  
int size : number of elements (total)  
tuple shape : dimensions  
dtype : type of elements  
int ndim : number of dimensions  
T : transposed  
METHODS:  
array(object, <dtype=type>) : constructor  
  
numpy.random  
normal(loc=, scale=, size=) : random numbers with gauss distribution  
rand(int n, int m) : random array, shape = n*m  
randint(low, high=, size=, dtype=) : rand with ints, in range  
numpy.linalg (linear algebra)  
cond() :  
inv() : inverse  
matrix_rank(matrix) :   
norm() :  
  
os  
chdir(“path”) : cd  
getcwd() : get current working dir  
  
os.path  
exists(string) : bool if string (path) exists  
  
pickle  
dump(obj, file) : saves object in file (any extension) (must be in wb mode)  
load(file) : returns content of file (any extension) (must be in rb mode)  
  
random  
choice(list) : dà elem random  
randint(min, max) : returns random int in [min; max] (included)  
randrange(start, stop, step) : random.choice in range()  
shuffle(list) : mischia lista..  
  
pwntools  
import pwn  
// pwn only works with bytes strings  
  
.ELF(“ELF”)		:   
.process(“EXE”)	: start process of file EXE, and return as variable"  
	shell=bool	: if True, give the arguments to the shell as given, not as argv  
.process(“CMD”, shell=True)	: give CMD to the shell, as if you were typing it in  
.process([“EXE”, “ARG1”, …])	: same as above (?)  
.process(executable=”EXE”, argv=”ARGS”, shell=False)	:  
pass ARGS as argv to launched EXE  
.remote(HOST, PORT)	: create remote, return as variable  
.shellcraft		: create shellcode on-the-fly  
.shellcraft.amd64.linux.sh() : assembly code to open shell /bin/sh  
	note : can be assembled with asm(asm_code, arch=”x86_64)  
process.close()	: close connection; raise EOFError  
process.recv(SIZE, timeout=N)	: receive as soon as something is available, up to SIZE;  
					if N seconds reached, return “”  
process.recvall()	: receive until EOF, then return  
process.recvuntil(str)	: receive output until received str, then return  
process.send(str)	: send str  
process.sendline(str)	: send + newline  
elf.sym.<SYM>	: address of function SYM in elf  
elf.sym[“SYM”]	: same  
  
pwnlib.util.packing  
.pack(int, size, endianness, sign)	: pack a n-bit integer  
  
pycryptodome  
import Crypto  
from Crypto.Util.Padding import pad, unpad  
from Crypto.Cipher import AES, DES  
  
pad(“text”, size, style=”...”)	: pad text, to size bytes, with style (prefixed strings)  
// AES / DES methods are the same  
AES.new(“key”, AES.MODE_…, “iv”)	:  
create single-use cypher, with iv (random if not specified ?);  
			i.e. can only crypt or decrypt once (?)  
AES.decrypt(“text”)	: decrypt text  
AES.encrypt(“text”)	: encrypt (padded) text  
  
// encryption  
// required input of fixed length, otherwise should pad  
with initialization vector (equal for AES/DES) :  
plaintext = b“text”  
iv = “iv”  
padded = pad(plaintext, size)  
cipher = AES.new(...)  
encrypted = AES.encrypt(...)  
decrypted = AES.decrypt(...)		# using new cipherw  
  
Crypto.Hash.*  
*.new(...)->* : return object hashed with * method  
<hashed>.hexdigest()	: in hex  
  
Crypto.PublicKey  
DSA.import_key(key)->DSA.DsaKey	:   
  
DSA.DsaKey: 	// key object  
.x  
.domain()	: p, q, g  
  
Crypto.Util.number  
// stuff with numbers, e.g. primes  
.getPrime(bits)	: random prime of n bits  
.isPrimeNumber(int)	: bool if prime  
  
scipy  
  
scipy.linalg  
cholesky() : cholesky factorization  
hilbert() : hilbert matrix  
lu_solve() : LU factorization  
solve(coefficients, known_term) :  
svd() :   
  
sys  
List argv()	: cmd args  
List path : libraries paths (as list)  
	sys.path.append : you can change the path, as a list  
version :  
version_info : version info/number  
  
time  
time() :   


## CONSTANTS
  
__name__ = “__main__” if file is being run, else name of the file  
__main__ = name of the file being run  
