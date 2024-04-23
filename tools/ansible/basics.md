# BASICS

Tool for infrastructure as code.  

## Concepts

**control node** : must have access (ssh) to **managed nodes**    
**managed nodes** : nodes (hosts) to provision  

**provision** : install stuff on new pc  

## Files

Files in `yaml`.  

## Properties

**idempotency** : ansible (tries to )"check" if something has already been done and doesn't do it again  
*	obs: checks what it can, so should use its modules and avoid raw scripts, for which he doesn't know expected outputs/errors
