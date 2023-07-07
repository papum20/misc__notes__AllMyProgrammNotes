# All My Programm Notes
The external hard-drive of my programming-and-computer-related knowledge.
Here you can find tons of commands, shortcuts, tips and all that stuff which I either forget repeatedly, or can't remember because I only use them once in a while.

## TOPICS  
*	[algorithms](algorithms/README.md)  
*	[apps](apps/README.md)  
*	[languages](languages/README.md)  
*	[markup](markup/README.md)  
*	[misc](misc/README.md)  
*	[os](os/README.md)  
*	[shortcuts](shortcuts/README.md)  
*	[tools](tools/README.md)  
*	[web](web/README.md)  
*	[web-development](web-development/README.md)  

## STRUCTURE
In each folder, named as the topic, you can find a list of markdown notes.
Folders can be grouped by topic.

-	`root` 
	-	`subdir1`  
		-	`[sub-subdir/topic1]`
		-	`topic1`  
			-	`lib_library1`
			-	`lib_library2`
			-	`file1.md`  
			-	`file2.md`  
			-	`README.md`  

## GENERAL SYNTAX
*	command format:  
	`command ARGUMENT(S)` : notes  
	*	command  
	*	parameters names: uppercase
	*	colon (`:`) separates command from notes  
*	language function format:  
	*	usually follows own language syntax (e.g. for types)  


## GENERAL FILES
*	`lib_LIBRARY` : folder for a category of libraries/modules/submodules  
*	`basics.md` : generical info  
*	`buttons.md` : (app/site) buttons, fields, etc.  
*	`commands.md` : commands (usually from command-line)  
*	`examples.md` : examples of code/...  
*	`files.md` : standard/relevant files/directories  
*	`functions.md` : language functions/objects/...  
*	`guide.md` : plain text guide  
*	`libraries.md` : list of libraries/modules (divided by category), with links to them (in case)  
*	`notes.md` : generical notes  
*	`shortcuts.md` : (app/site) shortcuts  
*	`syntax.md` : language syntax  
*	`README.md` : folder content and meta-info (about notes structure/folder...)  

## COMMANDS
`.bash_aliases` : (not a real command) to copy in ~/.bash_aliases in order to use these commands more easily  
*	(at the moment) the commands are intended to only be used in the repo folder  

`cd $allMyProgrammNotes_DIR` : move to your repo folder (installed in your user dir)  

`docentry ENTRY FILE` : print ENTRY found in FILE  
`mkentry PATH` : create new entry in PATH, copying files in __template_
`mklib BASEPATH [-L SUBDIR] NAME [-d] [-f FILENAMES...]` : create BASEPATH/[lib_SUBDIR/]NAME/, containing, optionally, default and/or files.  
`mklib-list BASEPATH [-L|-l]` : create BASEPATH/libraries.md, containing list and links of libraries in subdirectories.  
`update [-l LEVELS=0] [PATH=.]` : update structure.




---
### note:
some notes are still in italian, some (many) are quite messy/to tide up







































