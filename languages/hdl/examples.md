# EXAMPLES  
  
CHIP And {  
	IN a, b;  
	OUT out;  
	Nand(a = a,  
	         b = b,  
	         out = x);  
	Not(in = x,  
	       out = out);  
}  
  
  
CHIP Add16 {  
	IN a[16], b[16];  
	out out[16];  
  
	PARTS:  
	...  
}  
  
  
  
CHIP Add3Way16 {  
IN first[16], second[16], third[16];  
	OUT out[16];  
  
	PARTS:  
  
	Add16(a=first, b=second, out=temp);  
	Add16(a=temp, b=temp, out=out);  
}  
