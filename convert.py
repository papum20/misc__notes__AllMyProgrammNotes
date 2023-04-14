import sys


def getHelp():
	print("""
	actions:
	headers:
		pattern:
		-	lines starting with '#`
		actions:
		-	remove last ':'
	commands:
		pattern:
		-	lines not starting with \\t, *, #
		-	contain ':'
		-	don't contain '`' (backtick)
		actions:
		-	add backticks in first part before ':', without first and last whitespaces
		-	add newline before, if previous line was not a command (can contain *)
	parameters:
		pattern:
		-	start with \\t, or *
		actions:
		-	if doesn't start with *: add *
		-	if contains ' :', add backticks around left part of ':'
		-	don't add backticks to 'note: ', 'e.g.: '
		-	add backticks to what follows e.g./note and preceedes ':'
	any:
		new, consistent argument convetion:
			if contains <text>
			(<, then some text, without whitespaces before and after, but can have inside, then >)

			replace with TEXT (uppercase)
	""")
	raise Exception("missing input file")

def findSubStr(s:str, l:str, r:str, exclude:str=' '):
	i = s.find(l)
	if i != -1:
		j = s[i+1:].find(r) + i+1
		if (j != -1) and (c not in s[i+1:j] for c in exclude):
			return (i, j)
	return (None, None)

def stripRight(s:str, chars:str=' \t\n\v') :
	i = len(s)
	while i > 0 and s[i-1] in chars:
		i -= 1
	return s[:i]





NO_CODE = [
	'e.g.: ',
	'note: '
]

args = sys.argv
if len(args) == 1:
	getHelp()

PATH = args[1]
PATH_TMP = PATH + ".tmp"
last_type = 'NONE'
with open(PATH, "r") as fr:
	with open(PATH_TMP, "w") as fw:
		line = fr.readline()
		while line != "":
			# headers : remove :
			if line[0] == '#':
				last_type = 'HEADER'
				if line.strip()[-1] == ':':
					line = line.strip()[:-1] + '  \n'
			# command name
			elif (':' in line) and not (line[0] in ' \t#*') and ('`' not in line):
				ind = line.find(' :')
				if ind == -1:
					ind = line.find('\t:')
				if ind != -1:
					line = f"`{stripRight(line[:ind])}` :{line[(ind+2):]}"
					if last_type != 'COMMAND':
						line = '\n' + line
					last_type = 'COMMAND'
			# command parameter / description / note
			elif (line[0] in '\t*'):
				last_type = 'PARAMETER'
				if line[0] == '\t':
					line = '*' + line
				first = line[1:].strip()[0]
				# parameters / examples (code) ...
				j = line.find(' :')
				i = line.find(first)
				if j != -1:
					for w in NO_CODE:
						if w in line[:j]:
							i = line.find(w) + len(w)
				else:
					for w in NO_CODE:
						if w in line:
							i = line.find(w) + len(w)
							j = line.rfind(line.strip()[-1]) + 1
				line = f"{line[:i]}`{line[i:j]}`{line[j:]}"
			fw.write(line)
			line = fr.readline()
			print(f"-{line}-")

				
PATH = PATH_TMP
PATH_NEW = PATH + ".md"
with open(PATH, "r") as fr:
	with open(PATH_NEW, "w") as fw:
		line = fr.readline()
		while line != "":
			# args from <arg> to ARG
			i, j = findSubStr(line, '<', '>', ' ')
			print(f"-{line}-")
			while i:
				line = line[:i] + line[i+1:j].upper() + line[j+1:]
				i, j = findSubStr(line, '<', '>', ' ')
			fw.write(line)
			print(f"-{line}-")
			line = fr.readline()
			print(f"-{line}-")

				
				