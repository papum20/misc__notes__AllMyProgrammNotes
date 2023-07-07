# EXAMPLES

## ARGUMENTS
passing short arguments :  
```bash
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
ref: [baeldung][BAELDUNG]


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

[BAELDUNG]: https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script