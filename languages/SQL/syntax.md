# SYNTAX

## Statements

### initialization

`CREATE TABLE` : specifies new relation, creates its empty instance.  
*	specifies its attributes (with types) and initial constrains
*	e.g.:
	```
	Attr1 type1 constraints1,
	Attr2 type2 constraints2
	```
*	e.g.: `CHAR(6)` : domain, exactly 6 chars

`CREATE DATABASE db_name` :  
`CREATE SCHEMA schema_name` :  
*	also authorize another user 
	```
	CREATE SCHEMA schema_name
	AUTHORIZATION 'user_name'
	```

### schema change

`ALTER DOMAIN name operation params` :   
*	`operation` : 
	*	`SET/DROP DEFAULT/CONSTRAINT name` : 
		*	e.g.: `SET DEFAULT new_val` :  
		*	e.g.: `SET CONSTRAINT name CHECK expr` :  

`ALTER TABLE name operation params` :  
*	`operation` : 
	*	`ALTER/DROP COLUMN/CONSTRAINT name` : 
		*	e.g.: `ALTER COLUMN name SET NOT NULL` : 
		*	e.g.: `ADD COLUMN name params` : create empty col like in `CREATE TABLE`
	*	`DROP COLUMN name RESTRICT` : remove only if doesn't contain values
	*	`DROP COLUMN name CASCADE` : remove col and values contained

`DROP DOMAIN/TABLE` : delete  

## Table constraints
`CHECK` :   
`DEFAULT num` : where num is an int  
`NOT NULL` :  
`PRIMARY KEY` : just one, implies `NOT NULL`  
foreign key :   
*	```
	FOREIGN KEY(Attr1) REFERENCES
	Table2(Attr2)
	```
*	`Attr1 REFERENCES Table2(Attr2)` : with 1 attr, omit `FOREIGN KEY` (according to std iso)  
*	can be defined on more attrs

`UNIQUE` : unique val 
`UNIQUE(attr1,attr2)` : unique pair 
*	e.g.
	```
	Attr1 type1 constraints1,
	Attr2 type2 constraints2,
	UNIQUE(Attr1,Attr2)
	```

## Referential triggered action
Can be put after a referential constraint, to trigger action when operation rejected.  
```
ON < DELETE | UPDATE >
	< CASCADE | SET NULL | SET DEFAULT | NO ACTION >
```
`CASCADE` : delete/update referencing tuples  
`SET NULL` : value deleted/updated is replaced with `NULL`  
`SET DEFAULT` : value deleted/updated replaced with default  
`NO ACTION` : no removal/update allowed  

## Data types
Correspond to domains in relational calculi.  

### basic
`Boolean` :   
`Character-string` :  
*	fixed length
*	varying length

`Numeric` : int/float  
`DATE` :  
`TIME` :  
`INTERVAL` :  
`BLOB` : binary large object  
*	e.g.: used for large files (audio/video/text..)

`CLOB` : character large object  

### custom
```
CREATE DOMAIN domain_name
AS type constraints
CHECK ( boolean_expression ) 
```

### Operators
`AND` :  