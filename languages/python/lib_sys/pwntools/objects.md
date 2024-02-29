# OBJECTS  

## IMPORT  
import pwn  
// pwn only works with bytes strings  

## FUNCTIONS
`bytes pack(hex number, int word_size=32)` : from hex number to bytes  
`bytes p32(hex number)` : =pack(number, 32)  
`bytes p64(hex number)` : =pack(number, 64)  
  
## ELF
`ELF(“ELF”)` :   

`elf.sym.SYM` : address of function SYM in elf  
`elf.sym[“SYM”]` : same  

## process
`.process(“EXE”)` : start process of file EXE, and return as variable"  
*	`shell=bool` : if True, give the arguments to the shell as given, not as argv  

`.process(“CMD”, shell=True)` : give CMD to the shell, as if you were typing it in  
`.process([“EXE”, “ARG1”, …])` : same as above (?)  
`.process(executable=”EXE”, argv=”ARGS”, shell=False)` :  
*	pass ARGS as argv to launched EXE  

`process.close()` : close connection; raise EOFError  
`process.recv(SIZE, timeout=N)` : receive as soon as something is available, up to SIZE;  
				`*	if N seconds reached, return “”`  
`process.recvall()` : receive until EOF, then return  
`process.recvuntil(str)` : receive output until received str, then return  
`process.send(str)` : send str  
`process.sendline(str)` : send + newline  

## remote
`.remote(HOST, PORT)` : create remote, return as variable  

## shellcraft
`.shellcraft` : create shellcode on-the-fly  
`.shellcraft.amd64.linux.sh()` : assembly code to open shell /bin/sh  
*	note: can be assembled with asm(asm_code, arch=”x86_64)  

`.interactive()` : open interactive i/o  
  
## pwnlib.util.packing  
`pack(int, size, endianness, sign)` : pack a n-bit integer  
  
## README.md  
*	[README.md](./README.md)  

