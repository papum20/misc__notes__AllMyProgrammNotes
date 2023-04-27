import os
import sys


def getHelp():
	print("""\
	mklib BASEPATH [-L SUBDIR] NAME [-D|-d] [-f FILENAMES...]

	Create BASEPATH/[lib_SUBDIR/]NAME/, containing, optionally, default and/or files.

	Arguments:
	BASEPATH		library's language path
	-L SUBDIR		create library (NAME) in subdir (lib_SUBDIR) of language (BASEPATH)
	-d				don't create default files
	-D				(default) create default files
	-f FILENAMES...	create specified files in library dir

	""")
	raise Exception("wrong parameters")


def removeExtension(f:str):
	return f[:f.rfind('.')] if '.' in f else f





SUBDIR_START = "lib_"
BASEPATH, SUBDIR, NAME = [""] * 3
FILENAMES = [
	'basics.md',
	'objects.md',
	'README.md'
]
args = sys.argv

try:
	i = 1
	BASEPATH = args[i]
	i += 1
	if args[i] == '-L':
		SUBDIR = SUBDIR_START + args[i+1]
		i += 2
	if args[i][0] == '-':
		getHelp()
	NAME = args[i]
	i += 1
	if i < len(args):
		if args[i] == '-d':
			FILENAMES.clear()
			i += 1
		elif args[i] == '-D':
			i += 1
	if i < len(args) and args[i] == '-f':
		FILENAMES.extend(args[i+1:])
		
except:
	getHelp()


PATH = BASEPATH

# create SUBDIR
if len(SUBDIR) > 0:
	PATH += '/' + SUBDIR
	if not os.path.exists(PATH):
		os.mkdir(PATH)

# create NAME
PATH += '/' + NAME
if not os.path.exists(PATH):
	os.mkdir(PATH)


for filename in FILENAMES:
	p = PATH + '/' + filename
	if not os.path.exists(p):
		f = open(p, 'w')
		if filename == 'README.md':
			f.write(f"# {PATH.upper()}\n")
		else:
			f.write(f"# {removeExtension(filename).upper()}\n")
		f.close()