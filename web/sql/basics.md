# BASICS  
  
WHAT IS SQL  
interact with database;  
represented as scheme(s)/ table(s) (rows x cols);  
scheme = collection of tables;  
you can access elements by row/col;  
outputs must have same number of cols as database (e.g. union)  
  
SYNTAX :  
“-- “	: comment (with space!)  
‘	: single quotes for names  
// non case-sensitive? (select… or…)  
  
OPERATORS :   
and	:   
or 	:   
=	: logic equal  
.	: access.schema.table.col …  
l  
KEYWORDS :   
from		: (select … from …) from parent (table for col, schema for table…)  
like PATTERN	: (in where) match PATTERN;  
		PATTERN = any sequence to match, plus special signs:  
		%	: anything (0+ chars)  
		_	: exactly one char  
ORDER BY: ...
select	COL1,COL2,...	:  
access columns by names COL1,...  
union		: concatenate commands (must return same number of columns)  
where		: “environment”, assign values  
  
KNOWN SCHEMES/TABLES/COLS… :   
VERSION   
version()		: MySQL, PostgreSQL  
@@VERSION		: MIcrosoft SQL Server  
sqlite_version()	: SQlite  
  
MySQL :   
information_schema		: a schema  
  
tables		: list of tables accessible by current MySQL user  
cols :   
table_name		:   
table_schema	:   
  
columns	: list of all cols of all tables accessible by current user  
cols :  
column_name	:   
table_name		:   
table_schema	:   
  
FUNCTIONS :   
DATABASE()	: current schema  
HEX(‘string’)	: encode string to hex  
SLEEP(seconds) : sleep  
		in select : only executed when where = true  

STRINGS : 
CONCAT() : 
  
EXAMPLES :   
SELECT table_name FROM information_schema.tables WHERE table_schema = DATABASE()  
// select column named table_name, from table tables, from schema information_schema, filtering rows with table_schema=DATABASE()  
  

TYPES: 
NULL : any type
## README.md  
*	[README.md](./README.md)  

