# BASICS  
  
//COMMENT  
  
A-INSTRUCTION  
@var : A = var  
  
C-INSTRUCTION  
dest=comp;JMP  
  
dest = register where to memorize  
comp = ALU operation  
JMP = JGT, GLT, GEQ, JGE, JLE, JNE : conditioned jump to ROM[A] (comp compared to 0)  
	JMP : unconditioned jump to ROM[A]  
  
  
  
LABEL DECLARATION :  
(do while)  
(LOOP)  
…  
@LOOP : goto LOOP if condition  
(condition)  
  
  
//ENDLESS LOOP (AT THE END OF A PROGRAM SO OS DOESNT STOP  
(END)  
@END  
0;JMP  
  
VARIABLES :  
  
PRE-DEFINED:  
SCREEN (RAM[16384...])  
KBD (RAM[24576]) : pressed key on keyboard  
R0..R15 = RAM[0]...RAM[15]  
  
DEFINED BY USER:  
@xxx : if not defined by user as label; value assigned automatically (except 0..15)  
