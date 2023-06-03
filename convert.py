import sys
from string import ascii_letters, ascii_lowercase


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
		j = s[i+1:].find(r)
		if j != -1:
			j += i+1
			if all([c not in s[i+1:j] for c in exclude]):
				return (i, j)
	return (None, None)

def stripRight(s:str, chars:str=' \t\n\v') :
	i = len(s)
	while i > 0 and s[i-1] in chars:
		i -= 1
	return s[:i]

def readFile(path:str) -> list[str] : 
	doc = []
	with open(path, "r") as fr:
		doc = fr.read().split("\n")
	return doc





KEYWORDS = [
	'e.g.: ',
	'note: '
]
KEYWORDS_HALF = [i.strip(': \t') + ' ' for i in KEYWORDS]

HEADERS_EXCLUDED = [
	'README.md'
]



args = sys.argv
if len(args) == 1:
	getHelp()

PATH = args[1]

def convert(path:str):

	original = list(map(lambda l: l + "\n", readFile(path)))
	last_types = []
	current_header = ''

	with open(path, "w") as fw:
		for index, line in enumerate(original):


			if line.strip() == '```':
				last_types = ['CODE'] if 'CODE' in last_types else []

			elif not 'CODE' in last_types:

				# empty line
				if line.strip() == "":
					last_types = last_types[:1] + ['NEWLINE']

				# args from <arg> to ARG
				i, j = findSubStr(line, '<', '>', ' ')
				while i:
					# don't change in CODE
					i1, j1 = line[:i].find('`'), line[j+1:].find('`')
					if i1 != -1 and j1 != -1:
						break

					line = line[:i] + line[i+1:j].upper() + line[j+1:]
					i, j = findSubStr(line, '<', '>', ' ')

				# headers : remove :
				if line[0] == '#':
					last_types = ['HEADER']
					if line.strip()[-1] == ':':
						line = line.strip()[:-1] + '  \n'
					current_header = line.strip('# \t\n')

				# make heder
				elif line[0] in ascii_letters and not any([c in ascii_lowercase for c in line]) and (line.find(':') == -1 or line[line.find(':')+1:].strip() == ""):
					last_types = ['HEADER']
					if line.strip()[-1] == ':':
						line = line.strip()[:-1] + '  \n'
					current_header = line.strip('# \t\n')
					line = "## " + line


				elif line.startswith('// '):
					last_types = last_types[:1] + ['COMMENT']

				# command name
				elif (':' in line) and not (line[0] in ' \t#*'):
					ind = line.find(' :')
					if ind == -1:
						ind = line.find('\t:')
					if ind != -1:
						command = stripRight(line[:ind])
						command = command.strip('`')
						line = f"`{command}` :{line[(ind+2):]}"
						if not any([i in last_types for i in ['COMMAND', 'HEADER', 'NEWLINE']]):
							line = '\n' + line
						last_types = ['COMMAND']
						
				# command parameter / description / note
				elif (line[0] in '\t*') and current_header not in HEADERS_EXCLUDED:
					last_types = last_types[:1] + ['PARAMETER']
					if line[0] == '*':
						line = line[1:]
					if line.strip() == '':
						line = "\n"
					else:
						if line[0] == '\t' and not line.lstrip().startswith('*'):
							first = line.lstrip()[0]
							tabs = line.find(first)
							print(line, tabs)
							line = ('\t' * (tabs-1)) + '*\t' + line.lstrip()
						first = line[1:].strip()[0]
						# parameters / examples (code) ...
						j = line.find(' :')
						if j == -1: j = line.find('\t:')
						# keywords
						i = -1
						keyword = ""
						for w in KEYWORDS + KEYWORDS_HALF:
							if w in line:
								i = line.find(w) + len(w)
								keyword = w.strip(': \t') + ': '
								break
						if i == -1:
							i = line.find(first)
						if j == -1:
							j = line.rfind(line.strip()[-1]) + 1
						keyword = line[:i]
						command = line[i:j].strip('`')
						line = f"{keyword}`{command}`{line[j:]}"
				
				elif (line[0] in ascii_letters + '='):
					# make header (if all uppercase)
					# (already done above)
					if not any([c in ascii_lowercase for c in line]):
						last_types = ['HEADER']
						if line.strip()[-1] == ':':
							line = line.strip()[:-1] + '  \n'
						current_header = line.strip('# \t\n')
						line = "## " + line

					# make comment to header
					elif last_types[0] == 'HEADER':
						line = "// " + line
					
					# make comment to command
					elif len(last_types) > 0 and last_types[0] == 'COMMAND':
						line = "*\t" + line


			# don't add a new line
			if index == len(original) - 1:
				line = line.strip("\n")
			fw.write(line)
			#print(f"-{line}-")

				


args = sys.argv
if len(args) == 1:
	getHelp()

for path in args[1:]:
	convert(path)




## OLD, WITH PATH TMP


"""
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

				
				
"""