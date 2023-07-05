# EXAMPLES

Remove files from remote, after adding them to `.gitignore`:  
```bash
git rm -r --cached DIR
git commit -m 'Remove the now ignored directory "DIR"'
git push origin master
```