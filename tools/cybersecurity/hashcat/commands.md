# COMMANDS

`hashcat [OPTIONS] HASH_FILE DICTIONARY_FILE` : crack hash contained in `HASH_FILE` using words in `DICTIONARY_FILE`  
*	`-a ATTACK_TYPE` : use attack type
	*	e.g.: `-a 0` : dictionary attack
*	`-j RULE` : use rule on `DICIONARY_FILE`
*	`-m HASH_ALGO` : hash type
	*	e.g.: `-m 0` : MD5
*	`-r RULE_FILE` : use rules in `RULE_FILE` for dictionary attack
	*	if use more `-r`, do a combination
*	`--stdout` : print to stdout `DICTIONARY_FILE` with rules applied
