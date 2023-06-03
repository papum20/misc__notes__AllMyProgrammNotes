# BASICS

## vi(m)  
  
## SHELL USE  
`vimtutor` : tutorial  
  
  
## MODES  
`normal mode` : commands  
`insert mode` : typing  
  
## OPTIONS  
`ruler` :  
  
  
## COMMANDS  
format:  
// operator+motion  
operator:   
motion: what the operator will operate on  
es.: de  
(operator+)count+motion / count+operator  
count: number: apply motion count times  
es.: 2w: moves 2 words forward  
es.: d3w: deletes 3 words  
  
  
## MODES  
`Esc` : normal mode (from insert)  
`:term` : open new shell window  
  
## FILE  
`:COMMAND!` : after command: override / don’t make ask for confirmation  
`Ctrl+d` : command completion  
`<TAB>` : choose command completion  
`:h` : (or :help)  
*		`:h vimrc-intro` : vim features tutorial  

`:q` : quit  
*		`:q!` : quit and discard changes  

`:qw(!)` : save, quit  
`:qa(!)` : quit all (quit vi)  
`:w` : save  
*		`:w FILENAME` : save as filename  

`Ctrl+w, (then) w` : jump from one window to another  
`Ctrl+w, (then) v` : open new window (split screen vertical)  
`Ctrl+w, (then) n` : open new window (split screen horizontall)  
`<command>` : execute external (shell) command, and print in editor (without writing)  
`!COMMAND` : execute external (shell) command, and switch to shell view  
  
## EDIT  
`a` : append: add text after the cursor (character at the right)  
`A` : append at end of line  
`c` : change (deletes and goes in insert mode)  
*		`ce` : deletes until end of line and goes in insert mode  
*		`cw` :  
*		`c$` :  

`d` : (operator) delete (cut: deletes and saves)  
*		`dd` : delete line  
*		`de` : (motion) to the end of word (including last character)  
*		`dw` : until the next word (excluding its first character)  
*		`d$` : to the end of line (including the last character)  

`i` : insert: add text at cursor  
`o` : open a line below (adds a line and goes in insert mode)  
`O` : open a line above  
`p` : put (paste), below the cursor  
*		`if copied a whole line (dd)` : puts in the line below  

`rCHARACTER` : replace character below cursor with character  
`RSTRING` : start replacing (overriding) text below cursor  
`:r FILENAME` : retrieves filename, and puts its text below the cursor  
*		`:r !COMMAND` : retrieves output of command  
	`*			es.:` :r !ls  

`Ctrl+r` : redo (last command)  
`:#,#s/old/new/flag` : substitute, between lines, old with new, with option flag  
`:s/OLD/NEW` : substitute (first occurrence in the line) of old with new  
*		`:s/OLD/NEW/g` : (flag) substitute globally: all occurrences in the line  
*		`:N1,N2s/OLD/NEW/g` : substitute all occurrences  
*	between lines n1-n2 (included)  
*		`:%s/OLD/NEW/g` : all occurrences in file  
*		`:%s/OLD/NEW/gc` : find all occurrences in file,  
*	with a prompt whether to substitute or not for each one  

`u` : undo (last command)  
`U` : fix a whole line (undo all changes on the line)  
`x` : remove character under cursor  
`y` : yank (copy selected text)  
  
## DIGRAPHS  
//a way to write special characters, e.g. tilde ~  
`:digraphs` : shows table  
`Ctrl+K (followed by) <digraph sequence>` : types special character  
*		`e.g. Ctrl+K ‘ ?` : writes tilde  
  
## NAVIGATION  
`h` : left  
`j` : down  
`k` : up  
`l` : right  
  
`0` : start of line  
`$` : end of line  
`e` : end of current word (last character) /  
*	next word if already on last character of current word  
`w` : start of next word  
`G` : last line  
`gg` : first line  
`<number>G` : go to line number  
`Ctrl+g` : filename and line number  
  
`/STRING (and press ENTER)` : find string; move forward through results  
`/STRING\c` : search, ignoring case (just for this search)  
`?STRING (and press ENTER)` : find string; move backwards through results  
`n` : (next result)  
`N` : (previous result)  
`Ctrl+o` : go back to where you came from  
`Ctrl+i` : go forward  
`:set OPTION` : set search option…  
*		(you can either use short or long commands, e.g. ic=ignorecase)  

`noOPTION` : remove option  
`ic` : (ignorecase) ignore case (no case sensitive)  
*		`hls` : (hlsearch) highlight search results  
*		`is` : (incsearch) in sentence: show partial matches for a search phrase  

`%` : move to matching parentheses  
*		when on a parentheses character: move to matching parentheses  
*		when on another character: move to previous opening parentheses (if present)  
  
`v` : highlight (you can save highlighted lines in a file with :’,’w FILENAME)  
  
## EDITOR  
`:set number` : rows numbers  
`:set tabstop=N` : set tab to N spaces  
`:set shiftwidth=N` : spaces when newline  
`:syntax on` : syntax highlighting  
  
## FILES  
`/etc/vim/vimrc` : default configuration  
`$HOME/.vimrc` : user config (linux)  
`$HOME/_vimrc` : user config (windows)  

## README.md  
*		[README.md](./README.md)  

