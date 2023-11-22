# EXAMPLES

`grep '"size":' ${CONDA_PREFIX}/conda-meta/*.json |sort -k3rn |  sed 's/.*conda-meta\///g' |  column -t` : packages by size  
*	src: https://stackoverflow.com/a/67976448/20607105  
