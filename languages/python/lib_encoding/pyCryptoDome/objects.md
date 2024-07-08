# OBJECTS  
  
  
## Crypto.Cipher
  
### AES
`cipher=AES.new(key, mode, iv=)` : create new AES cipher
*	`MODE_*` : modes names

#### GCM
`update(aad)` : add **aad** to cipher  


  
## old
  
## import 
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

## Crypto.Hash.\*  
\*.new(...)->\* : return object hashed with * method  
<hashed>.hexdigest()	: in hex  
  
## Crypto.PublicKey  
DSA.import_key(key)->DSA.DsaKey	:   
  
DSA.DsaKey: 	// key object  
.x  
.domain()	: p, q, g  
  
## Crypto.Util.number  
// stuff with numbers, e.g. primes  
bytes_to_long(b) :   
getPrime(bits) : random prime of n bits  
isPrimeNumber(int) : bool if prime  
long_to_bytes(l) :   

## README.md  
*	[README.md](./README.md)  

