#!/bin/bash

### Script that replaces the name of a bib file reference to
#	$1: bib_file
### in all .tex files, given the directory
#	$2: SEARCH_DIR .


## Extract the arguments
bib_file=$1
SEARCH_DIR=$2


## First of all, create a back-up directory for the sed backup if it doesn't exist yet
SED_BACKUP_DIR=${SEARCH_DIR}/sed-backup
if [ ! -d $SED_BACKUP_DIR ]; then
	mkdir ${SED_BACKUP_DIR} 
fi


echo "Replacing bib-file occurrences with ${bib_file} ..."
## Replace the current line in which the .bib-file is specified with the new name, for all files in SEARCH_DIR
# Only find files, only find .tex files, ignore any .bak files, ignore files in build directories
for TEX_FILE in $(find ${SEARCH_DIR} -type f -regex ".*\.tex" ! -regex ".*\.bak" ! -regex ".*/build/.*"); do 
	if [ -f ${TEX_FILE} ]; then
		# Do the actual replacing with % as delimiter (/ gives issues if a bib_file is given with /Users/... for example
		sed -i".bak" "s%\bibliography{.*_bib}%\bibliography{${bib_file}}%g" ${TEX_FILE}
	
		# sed -i"${SED_BACKUP_DIR}/*.bak" ---- doesn't work, so we will move the backup files to the designated folder ourselves
		# if an identically named file is already in the SED_BACKUP_DIR, we will overwrite it
		if [ -f ${SED_BACKUP_DIR}/"*{TEX_FILE}.bak" ]; then
			rm ${SED_BACKUP_DIR}/"*{TEX_FILE}.bak"
		fi
		mv "${TEX_FILE}.bak" ${SED_BACKUP_DIR}
	fi
done
echo "Done."