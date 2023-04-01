# SYNTAX


## STRUCTURE ELEMENTS
---
### HEADERS
// 6 levels of headers;  
`# TEXT` : 1-6 \# to indicate level of header
### COMMENT
`<!-- TEXT -->` :  
### INLINE CODE
`` `TEXT` `` : (single backtick) not formatted  
``` `` `TEXT` `` ``` : use one more backtick (for each side) to escape backticks
### BLOCK
// triple backticks  
` ``` `  
`TEXT`  
` ``` `
### BLOCKQUOTES
`> TEXT` : text in block for quotes  
// to group multiple lines in same block, > before each line (including empty ones)
### LINE BREAKS
// how to separate lines
#### hard break:
// insert empty line: inserts it in preview too
#### soft break:
// insert 2 spaces at end of line


## ELEMENTS
---
### LINKS
#### inline links:
// URLs
`[LINK_TEXT](LINK)` : link to LINK, displayed with text LINK_TEXT  
`[LINK_TEXT](#HEADER)` : reference to any header in same document  
#### reference links:
// links to other places of document,  
// or to declared URLs: behave like variables  
`[LINK_TEXT][REFERENCE_NAME]` : reference link  
`[REFERENCE_NAME]: LINK` : reference declaration  

### IMAGES
//work like links, preceeded by !, where text is used as alt text
#### inline image link:
`![ALT_TEXT](LINK)` : 
#### reference image:
`![ALT_TEXT][REFERENCE_NAME]` :  
`[REFERENCE_NAME]: LINK` :  
### FOOTNOTES
`[^N]` : footnote link  
`[^N]: FOOTNOTE` : footnote declaration

### LISTS
// sub-lists made with indentation;  
// also blocks made with indentation/single-space, i.e. a block in same list element
#### unordered
`* TEXT` : (with bullet points)  
`- TEXT` : (with bullet points)
#### ordered
`1. TEXT` : (with numbers)

### LINE SEPARATORS
// insert 3+ chars to make a line;  
// some types have a different result if upper row not empty..
// not side-effects if empty line above
`***` :  
`---` : side-effect: make line above like header, and line disappers  
`___` :  
`===` : side-effect: make line above like header, but also inserts one line (equivalent to 2 ---)  


## TEXT
---
### SPECIAL CHARS
`\` : escape char
### FONT STYLES
`**TEXT**` : bold  
`_TEXT_` : italic  
`~~TEXT~~` : lined out  
##### notes : 
- text can include spaces
- can combine bold and italic in whatever order
