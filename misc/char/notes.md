# NOTES  
  
Characters encoding : mapping real language characters to numerical (byte) codes.  
  
Rules :  
Order : values follow alphabetical order (if present);  
Contiguity : every value (in range min-max) is associated (with a char);  
Grouping : logical grouping;  
		e.g. ASCII: uppercase=10xx xxxx, lowercase=11xx xxxx,  
control chars=00xx xxxx;  
  
Definition :   
shift : reserved code, changes mapping;  
free codes : not associated to characters, so (could) indicate an error;  
control codes : associated to transmission;  
  
HISTORY :   
1) 1870 - Baudot - teletype (telescrivente)  
32 codes, with shift 64:  
50 for letters, numbers, punctuation mark   
9 control chars  
2 shift  
3 free codes  
- no contiguity, order  
2) ? - punched cards (scheda perforata)  
when made mistake in punching holes for a char:  
mark card as not-valid = punch all = 1111 1111  
3) 1968 - ASCII   
128 chars (7bit, 1 parity bit, necessary at the time)  
0-31 + 127 : control (with repetitions):  
0x08=backspace (moves cartridge (testina) back, in teletype)  
0x7F=127=Delete (deletes all holes in punched card, i.e. 1111 1111=127)  
32-126 : latin (english) alphabet, upper+lower, numbers, marks  
contiguity, order  
no free codes  
4) 1965 - EBCDIC (IBM)  
proprietary  
8 bit  
no order  
5) 1991 - ISO646-1991  
european charachters  
12 free codes, for different languages needs  
6) ASCII code pages  
extended to 8bit=255 (no more need for parity bit)  
you can add your extension (hard to know which extension used)  
7) CJK :   
China, Japan, Korea: share several letters  
8bit not enough, use 16bit (56k) or more  
too many characters  
8) ISO 8859/1 (ISO Latin 1)  
8bit=255,  
only std ASCII extension  
compatible with ASCII  
adds some european characters  
9) Unicode and ISO/IEC 10646  
work separately, then remain separate but compatible  
chars for:  
modern scripts  
ancient scripts  
special marks  
principles :   
universal : for all languages  
efficiency : min memory use, max parsing speed: groupings, no shift…  
characters, not glyphs : no fonts, bold… just a char  
semantics : each char has its own meaning (same character divided if different meanings in different languages, e.g. double S in german and greek)  
order  
unification : characters common to different languages (e.g. latin)  
dynamic composition : (for some languages, chinese…)  
stability : assigned codes remain  
convertibility : easy conversion unicode - other (e.g. ASCII)  
  
chars :  
variable length codes : UTF-8 UTF-16 UTF-32 (n of bits)  
ISO 10646 -> fixed length codes : UCS-2, UCS-4 (n of bytes)  
[block (gruppo)]	[plan]		[row]		[cell]  
00000000		00000000	00000000	00000000  
  
[- = not used)  
ASCII  
  
  
  
  
  
  
-1010000  
ISO Latin 1  
  
  
  
  
  
  
01010000  
UCS-2  
  
  
  
  
00000000  
01010000  
UCS-4  
00000000  
00000000  
00000000  
01010000  
  
  
10) UTF (Unicode/UCS Transformation Format)  
each language usually only needs few bis  
varying number of bits  
UTF-8 :  
1byte : 0-127 : ASCII  
2byte : latin  
3byte : oriental  
4byte : other  
  
ASCII (UTF-8)  
  
  
  
  
  
  
0xxxxxxx  
ASCII (UCS-4)  
-0000000  
00000000  
00000000  
0xxxxxxx  
ISO Latin 1 (UTF-8)  
  
  
  
  
110yyyyx  
10xxxxxx  
ISO Latin 1 (UCS-4)  
-0000000  
00000000  
00000yyy  
yxxxxxxx  
idiographic alphabet (UTF-8)  
  
  
1110zzzz  
10zyyyyx  
10xxxxxx  
idiographic alphabet (UCS-4)  
-0000000  
00000000  
zzzzzyyy  
yxxxxxxx  
other (UTF-8)  
11111uuuu  
00000000  
00000000  
01010000  
other (UCS-4)  
000000ww  
wwzzzzzy  
110111yy  
yxxxxxxx  
  
  
UTF-8:  
first byte: number of bytes, in unary (i.e. number of 1s)  
others: start with 10  
note: needed as check, e.g. in transmission, for identifying errors (if a 10 arrives without a starting byte)  
  
Little Endian, Big Endian :   
FFFE char reserved to tell if own system is litte/big (if different, other receives FEFF, so can switch all chars)  
