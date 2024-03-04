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
1.	`pt` is divided in blocks,
2.	each is xored with the previous encrypted block (or IV if first),
3.	then encrypted

##### CTR


##### EBC
1.	`pt` is divided in blocks,
2.	each encrypted independently  

##### OFB
1.	`pt` is divided in blocks,
2.	each xored with the output of the previous encryption (or encrypted IV if first)

note:	Doesn't need padding.  


## stream ciphers
