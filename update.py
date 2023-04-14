import os
import sys
from typing import Callable



EXCLUDE = [".git", ".vscode", "_template"]
PREFIX_LIB = "lib_"




def getHelp():
	print("""\
	update [-l LEVELS=0] [PATH=.]

	Update structure.
	Recursively, for l levels, create references in each PATH/*/README.md/## CONTENTS for each subdir;
	create references in README.md to files in same dir;
	create references in */libraries.md for each lib_*;
	also creates needed files if not present.

	PARAMETERS:
	PATH=.			path where to start recursion
	-l LEVELS=0		levels to apply recursion;
					0 means witout limits
	
	Replaces each ## CONTENTS content.
	Doesn't create ## CONTENTS if no subdirs.
	Doesn't consider lib_* as subdirs.

	""")
	raise Exception("wrong parameters")



def toOverwrite(doc:list[str]):
	return len(doc) <= 1

def readFile(path:str) -> list[str] : 
	doc = []
	with open(path, "r") as fr:
		doc = fr.read().split("\n")
	return doc

"""
 create if not present;
"""
def createFile(path:str, filename:str, text:str) -> None :
	fullname = os.path.join(path, filename)
	if os.path.exists(fullname):
		doc = readFile(fullname)
		# if exists and long enough
		if not toOverwrite(doc):
			return

	# overwrite	
	with open(fullname, "w") as f:
		f.write(text)
			
				
def createReadme(path:str) -> None :
	createFile(path, "README.md", f"# {path.upper()}  \n\n")

def createLibraries(path:str) -> None :
	createFile(path, "libraries.md", "# LIBRARIES  \n\n")
				


def checkExcluded(f:str):
	return os.path.basename(f) not in EXCLUDE
def checkLibraries(path:str, f:str):
	return os.path.isdir(os.path.join(path, f)) and f.startswith(PREFIX_LIB)
def filterFile(f:str):
	return not os.path.isdir(f) and f != 'README.md' and f.endswith('.md')
def removeExtension(f:str):
	return f[:f.rfind('.')] if '.' in f else f
def addReadme(d:str):
	return os.path.join(d, 'README.md')
def addLib(d:str):
	return os.path.join(d, 'libraries.md')


def isHeader(line:str) -> bool:
	return line.startswith("#")

def nextHeader(doc:list[str], i:int=0) -> int:
	if i >= len(doc): return i
	elif isHeader(doc[i]): return i
	else: return nextHeader(doc, i+1)

def addHeader(
		path:str,
	    headers:list[str],
		contents:list[list[str]],
		links:list[list[str]],
		create:Callable[[], None]=None,
		n:int=1,
		create_new:bool=False
		) -> None :
	"""
	

	---
		@n : headers after which to add own headers
		@create_new : if True, create even if file not existing, but headers not empty
	"""
	if not os.path.exists(path):
		if not create_new or all([len(c) == 0 for c in contents]):
			return
		else:
			create()

	original = list(map(lambda l: l + "\n", readFile(path)))
	with open(path, "w") as fw:
		#write first n headers
		i = 0
		found_headers = 0
		while i < len(original) and found_headers < n:
			line = original[i]
			j = nextHeader(original, i+1)
			#skip headers to rewrite
			if not isHeader(line) or not any(map(lambda h: h in line, headers)):
				if isHeader(line):
					found_headers += 1
				#write (copy)
				fw.writelines(original[i:j])
			i = j

		#create custom headers
		for h, cont, lnk in zip(headers, contents, links):
			if len(cont) > 0:
				#write header name
				fw.write(f"{h}  \n")
				for c, l in zip (cont, lnk):
					fw.write(f"*\t[{c}]({l})  \n")
				fw.write('\n')

		#if contents was already present, skip it
		while i < len(original):
			line = original[i]
			j = nextHeader(original, i+1)
			#skip headers to rewrite
			if not isHeader(line) or not any(map(lambda h: h in line, headers)):
				#write (copy)
				fw.writelines(original[i:j])
			i = j

			

def updateReadme(path:str, parent:str, subdirs:list[str], files:list[str]) :
	parent = [] if not parent else [os.path.basename(parent)] if parent != '.' else ['root']
	parent_lnk = [] if not parent else ['../README.md']
	headers = ['## PARENT', "## CONTENTS", "## TOPICS"]
	contents = [parent, list(map(removeExtension, files)), subdirs]
	links = [parent_lnk, files, list(map(addReadme, subdirs))]
	addHeader(addReadme(path), headers, contents, links, lambda : createReadme(path), n=1, create_new=True) 

def updateLibraries(path:str, libraries:list[str]) : 
	headers = ["## CATEGORIES"]
	contents = [libraries]
	links = [list(map(addReadme, libraries))]
	addHeader(addLib(path), headers, contents, links, lambda : createLibraries(path), n=1, create_new=True) 

def updateContents(path:str) : 
	headers = ['## README.md', "## CATEGORIES"]
	contents = [['README.md']]
	links = [['./README.md']]
	addHeader(path, headers, contents, links, None, n=1, create_new=False) 


def recursive(path, levels, parent=None) :
	print(path)
	# create readme
	createReadme(path)
	
	# don't continue recursion
	if levels == 0:
		return

	# find subdirs
	ALLOWED = sorted(list(filter(checkExcluded, os.listdir(f"{path}"))))
	FILES = list(filter(filterFile, ALLOWED))
	LIBRARIES = list(filter(lambda f: checkLibraries(path, f), ALLOWED))
	SUBDIRS = list(filter(lambda f: os.path.isdir(os.path.join(path, f)) and f not in LIBRARIES, ALLOWED))
	
	print(f"path: {path}, level={levels}")
	print(f"subdirs: {SUBDIRS}")
	print(f"libraries: {LIBRARIES}")
	print(f"files: {FILES}")
	
	# go recursive
	for s in SUBDIRS+LIBRARIES:
		recursive(os.path.join(path, s), levels-1, path)

	#overwrite
	updateReadme(path, parent, SUBDIRS, FILES)
	updateLibraries(path, LIBRARIES)
	for f in FILES:
		updateContents(os.path.join(path, f))





args = sys.argv
PATH = "."
LEVELS = 0


if len(args) > 1:
	if "--help" in args:
		getHelp()
	if args[1] == "-l" and len(args >= 3):
		LEVELS = args[2]
		if len(args) == 4:
			PATH = args[3]
		elif len(args) > 4:
			getHelp()
	elif len(args) == 2:
		PATH = args[1]
	else:
		getHelp()
if LEVELS == 0:
	LEVELS = 100



recursive(PATH, LEVELS)