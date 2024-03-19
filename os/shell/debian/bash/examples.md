# EXAMPLES

## ARGUMENTS

arguments, arrays :
*	```bash
	./my_command a b "c d"
	# looping on $*, splits with spaces: a, b, c, d
	# looping on "$*", stringifies all: "a b c d"
	# looping on $@, splits with spaces, treats each elem as unquoted string: a, b, c, d
	# looping on "$@", splits quoted elements, treats each elem as quoted string: a, b, "c d"
	```
	*	ref: [unix.stackexchange][unix.stackexchange_args]

passing short arguments :  
*	```bash
	# userReg-flags.sh -f 'John Smith' -a 25 -u john
	while getopts u:a:f: flag
	do
		case "${flag}" in
			u) username=${OPTARG};;
			a) age=${OPTARG};;
			f) fullname=${OPTARG};;
		esac
	done
	```
	*	ref: [baeldung][baeldung_while]

`read` command :
*	```bash
	IFS='.' while read a b c
	do
		echo "a: $a, b: $b, c: $c"
	done
	```



## BOOL

check file extension:  
*	right part of `==` checks for linux pattern
	```bash
	if [[ $file == *.txt ]] ...
	```
*	right part of `=~` checks for regex
	```bash
	if [[ $file == ... ]] ...
	```


<!-- LINKS & REFS -->

[baeldung_while]: https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script
[unix.stackexchange_args]: https://unix.stackexchange.com/questions/129072/whats-the-difference-between-and