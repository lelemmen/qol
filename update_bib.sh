#!/bin/bash

### Script that replaces the location of
#	$1: bib_file
### in all .tex files, given the directory
#	$2: SEARCH_DIR .

### Flags:
#	-r:	search recursively in SEARCH DIR

bib_file=$1
SEARCH_DIR=$2

echo ${bib_file}

