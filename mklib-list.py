#!/usr/bin/env python3

import os
import sys


def getHelp():
	print("""\
	mklib-list BASEPATH [-L|-l]

	Create BASEPATH/libraries.md, containing list and links of libraries in subdirectories.

	Arguments:
	BASEPATH		path containing libraries, where libraries.md will be created
	-L				search libraries directories in any BASEPATH/lib_SUBDIR/LIBDIR,
					where libraries dirs are divided in subdirectories of BASEPATH
	-l				search libraries directories in BASEPATH;
					-L, -l are alternatives, -L is default

	""")
	raise Exception("wrong parameters")

def hasReadme(prnt, dr):
	return os.path.exists(prnt + '/' + dr + '/README.md')

def addLibs(f, base, libs, subdir=False):
	path = base + '/' + libs
	for lb in os.listdir(path):
			if hasReadme(path, lb):
				if subdir:
					f.write(f"*	[{lb}]({libspath}/{lb}/README.md)  \n")
				else:
					f.write(f"*	[{lb}]({lb}/README.md)  \n")
				



LIBS_SUBDIR_START = "lib_"
args = sys.argv

if len(args) == 1:
	getHelp()
basepath = args[1]

if len(args) == 2:
	args.append('-L')


# create libraries.md

print(basepath + '/' + 'libraries.md')
with open(basepath + '/' + 'libraries.md', "w") as md:

	md.write("# LIBRARIES\n\n")
	
	libspath = basepath
	# with subdirs categories
	if args[2] == '-L':
		libsdirs = list(filter(lambda s: s.startswith(LIBS_SUBDIR_START), os.listdir(basepath)))
		libsdirs.sort()
		for libspath in libsdirs:
			md.write(f"## {libspath[len(LIBS_SUBDIR_START):]}  \n")
			addLibs(md, basepath, libspath, subdir=True)

	# without subdirs categories
	else:
		addLibs(md, libspath, libspath)