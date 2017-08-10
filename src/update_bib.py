#!/usr/bin/env python3

# Script that, in a given directory, replaces all instances of bib-file references to a new name

import argparse
import os
import glob
import shutil
import fileinput
import re



# Parse the arguments
#   the first argument is the name of the new bib-file
#   the second argument is the directory in which should be searched

parser = argparse.ArgumentParser(description="Replace bib-file references to new ones.")
parser.add_argument('bib_name', type=str, help="the name of the new bib-file reference")
parser.add_argument('search_dir', type=str, help="the directory in which should be searched")
arguments = parser.parse_args()
bib_name = arguments.bib_name
search_dir = arguments.search_dir

# if bib_name ends with .bib, remove it (as it shouldn't be included in the .tex file
bib_name = bib_name.replace('.bib', '')


# First of all, create a back-up directory in the search directory
backup_dir = search_dir + '/replace_bib_script_backup'
if not os.path.isdir(backup_dir):
    os.mkdir(backup_dir)


print("Replacing bib-file occurrences with the newly provided bib-file name ...")
dotbib_pattern = re.compile(r'\\bibliography{.*\.bib}.*')
underscorebib_pattern = re.compile(r'\\bibliography{.*_bib}.*')
replace_with = r'\\bibliography{{{}}}'.format(bib_name)
for filename in glob.iglob(search_dir + '/**/*.tex', recursive=True):  # iglob returns an iterator
    # do the actual inplace replacement
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as f:  # creates a backup: filename.bak
        for line in f:
            line = underscorebib_pattern.sub(replace_with, line)
            line = dotbib_pattern.sub(replace_with, line)
            print(line, end='')  # line already has a newline, so don't print another one!

    # move the created filename.bak to the back-up directory
    shutil.move(filename + '.bak', backup_dir + '/' + os.path.basename(filename) + '.bak')

print("Done.")
