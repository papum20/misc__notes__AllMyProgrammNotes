# SYNTAX

## Statements

### initialization

`CREATE ASSERTION name CHECK(condition)` : named constraint  
`CREATE TABLE` : specifies new relation, creates its empty instance.  
*	specifies its attributes (with types) and initial constrains
*	e.g.:
	```
	Attr1 type1 constraints1,
	Attr2 type2 constraints2
	```
*	e.g.: `CHAR(6)` : domain, exactly 6 chars

`CREATE DATABASE db_name` :  
`CREATE INDEX name ON table (attr)` :  
`CREATE SCHEMA schema_name` :  
*	also authorize another user 
	```
	CREATE SCHEMA schema_name
	AUTHORIZATION 'user_name'
	```
`CREATE VIEW name [attrs] AS query [WITH [LOCAL|CASCADED] CHECK OPTION]` : create view  
*	`WITH CHECK OPTION` : allow update to view (same operations as tables), only if the update belongs to the view
*	`LOCAL` : only update view
*	`CASCADE` : cascade update

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

`CHECK (condition)` :   
*	note: `condition` can be a query, depending on sql type

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

## Data operations

`SELECT attrs+exprs FROM tables+joins [WHERE cond] [GROUP BY attrs2] [HAVING aggr-cond] [ORDER BY ASC|DESC]` : query  

`query1 EXCEPT query2` :   
`FROM table` :  
*	obs: tuple calculus: attrs=range list

`query1 INTERSECT query2` :   
`ORDER BY attr ASC|DESC` : (default=`ASC`)  

`SELECT attrs` :  
*	obs: tuple calculus: attrs=target list

`query1 UNION query2` :   
`query1 UNION ALL query2` : keep duplicates  

`WHERE condition` : (optional in a query)
*	obs: tuple calculus: attrs=formula
*	obs: omitting equals `WHERE true`

### attributes
`attr1,attr2` : list  
`*` : all  
`table1.attr1` : (needed when ambiguity: if attr in common between tables)  
`attr1 AS new1, attr2` : **alias** - 
*	obs: renaming operation

### conditions
`attr op ALL (query)` : operator `attr op x` is true foreach `x` in `query`  
`attr op ANY (query)` : operator `attr op x` is true for any `x` in `query`  
`EXISTS (query)` : true if >0 tuples  
`attr LIKE 'pattern'` : true if value matches  
*	`pattern` :
	*	`_` : any single char
	*	`%` : any

`attr IN (query)` : if in  
`attr IS NULL` :  
`DISTINCT attrs` : remove duplicates for `attrs`  
*	e.g.: `SELECT DISTINCT attrs` :  
*	obs: sql doesn't remove duplicates by dflt

`attr op (SELECT ...)` : nested query  
*	note: visibility : 
	*	can't access inner vars from outside, unless returned
	*	can access outer vars from inside
	*	implicitly refers to closest `FROM`  

### aggregate functions
`aggr([DISTINCT] *)` :  
`aggr([DISTINCT] attr)` :  
*	`aggr=AVG|COUNT|MAX|MIN|SUM` :  
	*	`COUNT` : doesn't count `NULL` val
*	e.g.: `SELECT count(*) ...` :  
*	e.g.: `aggr() AS ...` : alias  

`SELECT attrs, aggr() ... GROUP BY attrs` : perform query without aggr, then grouping and apply aggr over each group  
`SELECT ... GROUP BY ... HAVING cond` : select groups having condition (applied on aggr)
*	note: can't nest queries here (language choice)


### tables

`table [AS] alias` : **alias** - 
*	note: `AS` can be omitted

`table1 JOIN table2 ON table1.attr1=table2.attr2` : **natural join** -   
*	obs: `FROM table1, table2 WHERE table1.attr1=table2.attr2` : equivalent

`(t1 JOIN t2 ...) JOIN ...` : concatenated joins  
`LEFT/RIGHT/FULL OUTER JOIN` : **outer join** - 
*	note: with `LEFT`,`RIGHT` : `OUTER` can be omitted


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

### operators
`AND` :  

## Updating operations

`DELETE FROM table [WHERE cond]` :  
*	note: removing a tuple could dremove others (if `CASCADE` constraint)
*	note: no `WHERE` means `WHERE TRUE`

`INSERT INTO table [(attrs)] VALUES(vals)` :  
`INSERT INTO table [(attrs)] query` :  
*	note: can omit `attrs`, but need to put `vals` in correct position
*	note: can insert incomplete tuples for table if no constraint on `NULL`, and assigned `NULL`/`default`
*	note: beware of inserting incomplete tuples with attrs of same type: would give error or asign by default to first attr in positions, despite attrs specified in `table(attr1,attr2)`

`UPDATE table SET attr = <expr|query|deafult|null> [WHERE cond]` :  