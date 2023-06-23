#!/usr/bin/env python3

import os


def foo(path:str):
	files = os.listdir(path)
	print(path, files)
	if "libraries.md" in files:
		os.remove(os.path.join(path, "libraries.md"))
	print(path, files)
	for f in files:
			if os.path.isdir(os.path.join(path, f)):
				foo(os.path.join(path, f))


foo(".")