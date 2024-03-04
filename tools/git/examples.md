# EXAMPLES

Remove files from remote, after adding them to `.gitignore` :  
```bash
git rm -r --cached DIR
git commit -m 'Remove the now ignored directory "DIR"'
git push origin master
```

Remove file from all commits (e.g. sensitive data) :
```bash
git filter-repo --invert-paths --path PATH
# then add,commit, force push
git push origin --force --all
```
