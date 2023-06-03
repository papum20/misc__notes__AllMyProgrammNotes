# COMMANDS  
  
## ELF
readelf ELF :   
	-h	: header  
	-l	: segments  
	-S	: sections  
  
## SECTIONS
.bss : uninitialized global vars  
	e.g. static int x  
.data : read and writable data  
	e.g. static int x=0x41  
.dynamic : linking info  
.interp : interpreter* path  
.rodata : read-only data  
	e.g. strings like in printf(“ciao”)  
.symtab : symbol table  
.text : exe instructions (code) of program  
  
## REGISTERS  
x86-32 :   
// 32b registers  
general purpose :   
EAX : (called accumulator, as was used by arithmetic operations)  
	subsections:  
	AX : least significant 2B  
	AL : least significant B  
	AH : most significant B  
ECX : (called counter, as was used to hold a loop index)  
reserved for special purposes :   
EBP : (extended) base pointer / frame pointer :  
starting point for local vars, in current block’s stack  
ESP : stack pointer : start of unused stack  
  
x86-64 :   
// 64b registers  
general purpose :   
*ax, *bx, *cx, *dx, *sx, *di :  
*sp, *bp :  
r8-r15 :    
accessed with :   
rax : full register (64b)  
eax : half register (lowest 32b)  
ax : 1/4 register (lowest 16b)  
al : 1/8 register (lowest 8b)  
special registers :   
// used by CPU automatically  
rbp : (not used automatically, but) normally used to calculate offset from memory locations  
rflags : status of current run (last instruction)  
rip : points to instruction executed at next step  
rsp : keep pointer to stack frame with push and pop  
xmm0-15 : enable use of SIMD instructions;  
	usually 126b or 256b;  
	can be used to accelerate crypto operations or vector graphics  
// parameters for functions get passed in :   
rdi, rsi, rdx, rcx, r8, r9, xmm0-7  
  
## x86 INSTRUCTIONS  
data movement :   
lea  op1,  op2 :  load  the  memory  address  indicated  by  op2 into the register specified by op1  
mov op1, op2 : copy the data item referred to by op1 into the location referred to by op2  
push op1 : place its operand onto the top of the stack  
pop op1 : remove the 4B data element from the top of the stack  
Arithmetic and Logic Instructions :  
add op1, op2 : stores in op1 the result of op2+op1  
sub op1, op2 : stores in op1 the result of op2-op1  
// The following instructions perform the specified logical operation on the operands, storing the result in the first operand location  
and op1, op2  
or op1, op2  
xor op1, op2  
Control Flow Instructions :   
jmp  op :  jump  to  the  instruction  at  the  memory  location specified by the operand op.  
cmp  op1, op2 :  compares  the  values  of  the  two  specified operands and stores the result in the machine status word.  
j<condition>  op :  depending  on  the <condition>  and  on the context of machine status word, jumps to instruction at the memory location indicated by the operand.  
other :   
syscall : syscall;  
	syscall number loaded in rax (64b) / eax (32b);  
	parameters in eax, ebx, exc, edx, esi, edi, ebp;  
	return code in rax (64b) eax(32b);  
	paramters in rdi, rsi, rdx, r8, r9, r10 for 64b;  
  
DEFS :  
interpreter : program that allows ELF to load shared object dynamically at run-time  

## COMMANDS
`checksec` : check security (mitigations) on  

## SECTIONS
`.bss` : non-initialized global vars  
`.text` : executable code  

## README.md  
*	[README.md](./README.md)  

