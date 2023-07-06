#!/bin/bash

help () {
	echo \
"Usage: docentry ENTRY FILE
"
}

if (($# < 2))
then
	help
	exit 1
elif ! [ -e $2 ] || ! [ -r $2 ]
then
	echo "file doesn't exist, or can't be read."
	help
	exit 1
else
	entry=$1
	file=$2
fi


echo "/(\`(<?)${entry})[[:space:]\`\(>]/,/^\s*$/p" $file
sed -nE "/(\`(<?)${entry})[[:space:]\`\(>]/,/^\s*$/p" $file
