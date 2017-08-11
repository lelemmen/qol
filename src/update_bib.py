#!/usr/bin/env python3

# Script that, in a given directory, replaces all occurrences of bib-file references (in .tex files) to a new name

import argparse
import os
import glob
import shutil
import fileinput
import re


def inplace_replace(pattern, replace_with, filename):
    """
    Inplace replaces all occurrences of 'pattern' with 'replace_with' in the file that corresponds to 'filename'.
    Due to the nature of the used FileInput module, a back-up document will be made with name 'filename'.bak

    :param pattern: a compiled re pattern
    :param replace_with: string to replace the pattern with
    :param filename: name of the file you want all occurrences of pattern to be replaced in
    :return: None
    """

    with fileinput.FileInput(filename, inplace=True, backup='.bak') as f:  # creates a backup: filename.bak
        for line in f:
            line = pattern.sub(replace_with, line)
            print(line, end='')  # line already has a newline, so don't print another one!


def all_file_substitute(pattern, replace_with, file_extension, search_dir, backup_dir):
    """
    Substitutes all occurrences of 'pattern' with 'replace_with' of all files with extension 'file_extension' in the given 'search_directory'
    Due to the nature of the used FileInput module in the helper function 'inplace_replace()', this function also moves the made back-up files to a given back-up directory.

    :param pattern: a compiled re pattern
    :param replace_with: string to replace the pattern with
    :param file_extension: extension of the filename of the files trying to substitute
        There is a little hack you can use: it is coded in the way that file_extension actually behaves like the tail (think 'endswith') of the filename, so you can actually search for specific filenames as well
    :param search_dir: directory in which to search for files
    :param backup_dir: directory in which to move the back-up files created by the helper function 'inplace_replace()'
    :return: None
    """

    for filename in glob.iglob(search_dir + '/**/*' + file_extension, recursive=True):  # iglob returns an iterator
        inplace_replace(pattern, replace_with, filename)

        # move the created back-up file filename.bak to the back-up directory
        shutil.move(filename + '.bak', backup_dir + '/' + os.path.basename(filename) + '.bak')

# Parse the arguments
#   the first argument is the name of the new bib-file
#   the second argument is the directory in which should be searched

parser = argparse.ArgumentParser(description="Replace bib-file references to new ones.")
parser.add_argument('bib_name', type=str, help="the name of the new bib-file reference")
parser.add_argument('search_dir', type=str, help="the directory in which should be searched")
arguments = parser.parse_args()
bib_name = arguments.bib_name
search_dir = arguments.search_dir

# if bib_name ends with .bib, remove it
bib_name = bib_name.replace('.bib', '')


# First of all, create a back-up directory in the search directory
backup_dir = search_dir + '/replace_bib_script_backup'
if not os.path.isdir(backup_dir):
    os.mkdir(backup_dir)


# Specification of all patterns (list values) and replace_withs (single values) for all extensions (keys)
pattern_dict = {'.tex': [re.compile(r'\\bibliography{.*\.bib}.*'), re.compile(r'\\bibliography{.*_bib}.*')],
                'CMakeLists.txt': [re.compile(r'BIBFILES.*\.bib')]}
replace_with_dict = {'.tex': r'\\bibliography{{{}}}'.format(bib_name),
                     'CMakeLists.txt': r'BIBFILES {}'.format(bib_name + '.bib')}
# no extension (.bib) in the tex replacements, extension (.bib) in CMakeLists


print("Replacing bib-file occurrences with the newly provided bib-file name ...")

# Do the actual in-place substitutions for .tex-files
for file_extension in ['.tex', 'CMakeLists.txt']:
    for pattern in pattern_dict[file_extension]:
        all_file_substitute(pattern, replace_with_dict[file_extension], file_extension, search_dir, backup_dir)

print("Done.")
