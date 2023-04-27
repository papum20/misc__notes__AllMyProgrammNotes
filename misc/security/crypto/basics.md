# BASICS.MD

rsa: 2048 bit  


## RSA
### NOTATION
`m` : plain text msg  
`c` : encrypted msg  
`p, q` : prime numbers (keys)  
`n=p*q` :   
`totient(n)=(p-1)*(q-1)` : totient function  
`d=` :   
`e=` :   
### FORMULAS
d=e\**-1 mod tot  
de mod tot = 1  
totient = (p-1) * (q-1)  
m\**e mod n = c  
c\**d mod n = decrypted  

### HACKS
#### find n:  
1.	encrypt/decrypt -1  
2.	guess (doesn't work with values < n)  
