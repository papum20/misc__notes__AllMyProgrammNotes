# BASICS


## block ciphers
Convert `m` to `c` block by block, independently.  

### AES
Block cipher, can become stream with modes.  
Key bits `128` (`AES-128`) or `256` (`AES-256`).  
Difficulty: best proved attempt reduces brute-force of `128b` to `126.1b`
*	it's still very infeasable, but suggest `AES-256`, also against quantum

Applies many invertible transformations
*	so decryption does the reverse

Steps:
1.	input as 4x4 matrix
2.	10 rounds of transformations

#### modes of operation
**modes of operation** : used to work on m longer than 1 block  

##### CBC
**CBC** : _cipher block chaining mode_
1.	`pt` is divided in blocks,
2.	each is xored with the previous encrypted block (or IV if first),
3.	then encrypted

##### CFB
**CFB** : _cipher feedback mode_
1.	`pt` is divided in segments (each of len in bits=`s`, `1<=s<=b`, `b` block size),
2.	(input) `i0=IV`, `i1 = (i0<<s) + c0)%2**b`, ...
2.	enc : `c0 = xor(p0, aes_ecb(i0))`, ...
*	code:
	```python
	ct_bytes = b''
	input = IV
	SEGMENT_SIZE = 8 # bits
	SEGMENT_SIZE_BYTES = 1
	BLOCK_SIZE = 16

	for ch in msg:
		cipher = AES.new(key, AES.MODE_ECB)
		e = cipher.encrypt(input)
		ct_bytes += xor(e[0], ch)
		input = input[SEGMENT_SIZE_BYTES:] + long_to_bytes(ct_bytes[-SEGMENT_SIZE_BYTES])
	```

##### CTR
**CTR** : _counter mode_  

##### EBC
**EBC** : _electronic codebook mode_
1.	`pt` is divided in blocks,
2.	each encrypted independently  

##### GCM
**GCM** : _galois/counter mode_
*	also grants authentication
*	input:
	*	`pt` : plaintext
	*	`aad` : _additional authenticated data_ - data to authenticate but not encrypt, so public to use for authentication
	*	`iv` : initialization vector (`96b`, otherwise it's hashed)
*	?? `ct` blocks in galois field `GF(2^128) = Z2[x]/(x^128+x^7+x^2+x+1)`
*	steps:
	1.	**ctr** mode, with `iv = iv + '0'*32` (`96b` iv + `32b` 0's)
		*	(`pyCryptoDome` seems to work like this) counter `0` and `1` used for `aad`, from `2` for all `pt`
	2.	calculate `128b` tag (mac, authenticator) with hash function `ghash`, and galois stuff

##### OFB
**OFB** : _output feedback mode_
1.	`pt` is divided in blocks,
2.	each xored with the output of the previous encryption (or encrypted IV if first)

note:	Doesn't need padding.  


## stream ciphers
