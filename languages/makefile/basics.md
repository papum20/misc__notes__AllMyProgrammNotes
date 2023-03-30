# BASICS  
  
MISC:  
# : comment  
  
VARIABLES:  
<var>	=	<val> : simple assignment  
<var>	:=	<val> : evaluates assignment  
<var>	::=	<val> : similar to :=  
<var>	:::=	<val> : -  
<var>	!=	<val> : evaluates shell script value  
	e.g.: foo != printf “bar”  
<var>	+=	<val> : append  
  
SYMBOLS:  
% : any  
$@ : left side of : , that is, rule/target name  
$^ : right side of : , that is, dependencies  
$< : evals to first prerequisite of first rule for this target  
rule: dependencies  
	… $< …  
  
COMMAND LINE:  
make <var>=<val> <target> : passing command line arguments =  
	assigning values to variables  
$(<var>) : to use argument, like normal variables  
  
FUNCTIONS:  
//function use : $(function arg1, arg2, …)  
// $=eval  
(dir <text>) :   
(notdir <text>) :   
(patsubst pattern, replacement, text) :  
replaces all pattern occurrences in text with replacement  
(warning <text>) : prints text (debug)  
echo <text> :   
@echo <text> : don't print echo  
  
“KEYWORDS”:  
.PHONY : target  
	//phony targets are “false” targets, i.e. never interpreted as files,  
but just as special targets, or commands  
  
  
----OLD----  
  
file_name = Makefile  
  
  
target: dependencies  
	code  
when executed target, if dependencies modified after last modification of target, executes code  
  
clean:  
	rm (-f) *.o main  
removes files other files could generate  
-f to avoid error when removing not existing file  
  
  
es.  
main: main.o sum.o  
	gcc -o main main.o sum.o  
main.o: main.c sum.h  
	gcc -c main.c  
sum.o: sum.c sum.h  
	gcc .c sum.c  
clean:  
	rm *.o main  
