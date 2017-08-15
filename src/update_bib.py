#!/usr/bin/env python3

# Script that, in a given directory, replaces all occurrences of bib-file references (in .tex files and CMakeList.txt) to a given new name (that is an !!! absolute !!! path to the file)

import argparse
import os
import glob
import shutil
import fileinput
import re


class Extension:
    """
    Specifies substitution rules for patterns for a given file name extension
    """
    def __init__(self, extension, patterns, replace_with, absolute=True):
        """
        :param extension:       string that represents the extension of the files trying to substitute
                                    There is a little hack you can use: it is coded in the way that file_extension actually behaves like the tail (think 'endswith') of the filename, so you can actually search for specific filenames as well
        :param patterns:        a list of compiled re pattern
                                    Order matters!
        :param replace_with:    string to replace the pattern with if it were an absolute substitution (see :param absolute)
        :param absolute:        bool:   True represents a filename extension in which the substitution has to be done absolutely (i.e. bib_name stays absolute)
                                        False represents a filename extension in which the substitution has to be done relatively (i.e. bib_name needs to become relative)
        """
        self.extension = extension
        self.patterns = patterns
        self.replace_with = replace_with    # if absolute:      represents the full string that a pattern will be replaced with
                                            # if not absolute:  represents a string that still has to be .format()

        self.absolute = absolute


def inplace_pattern_replace(extension_instance, filename):
    """
    Inplace replaces all occurrences of 'pattern' with 'replace_with' in the file that corresponds to 'filename'.
    Due to the nature of the used FileInput module, a back-up document will be made with name 'filename'.bak

    :param extension_instance:  instance of the class Extension
    :param filename:            name of the file you want all occurrences of pattern to be replaced in
    :return: None
    """

    with fileinput.FileInput(filename, inplace=True, backup='.bak') as f:  # creates a backup: filename.bak
        for line in f:
            for pattern in extension_instance.patterns:
                if extension_instance.absolute:
                    line = pattern.sub(extension_instance.replace_with, line)
                else:   # we have to figure out the relative bib_name and put it in replace_with
                    relative_path_to_bib_file = os.path.relpath(bib_path, filename)
                    line = pattern.sub(extension_instance.replace_with.format(relative_path_to_bib_file), line)     # we can use .format() here because there is a {} in replace_with instances that have absolute=False
                                                                                                                    # unfortunately, this is still manually coded
            print(line, end='')  # line already has a newline, so don't print another one!


def all_file_substitute(extension_instance, search_dir, backup_dir):
    """
    Based on the specifications in the Extension instance, substitutes all occurrences of its 'patterns' with 'replace_with' in the given 'search_directory'
    Due to the nature of the used FileInput module in the helper function 'inplace_replace()', this function also moves the made back-up files to a given back-up directory.

    :param extension_instance:  instance of the class Extension
    :param search_dir:          directory in which to search for files
    :param backup_dir:          directory in which to move the back-up files created by the helper function 'inplace_replace()'

    :return:                    None
    """

    for filename in glob.iglob(search_dir + '/**/*' + extension_instance.extension, recursive=True):  # iglob returns an iterator
        inplace_pattern_replace(extension_instance, filename)

        # move the created back-up file filename.bak to the back-up directory
        shutil.move(filename + '.bak', backup_dir + '/' + os.path.basename(filename) + '.bak')


# Parse the arguments
#   the first argument is the name of the new bib-file
#   the second argument is the directory in which should be searched

parser = argparse.ArgumentParser(description="Replace bib-file references to new ones.")
parser.add_argument('bib_name', type=str, help="the name of the new bib-file reference")
parser.add_argument('search_dir', type=str, help="the directory in which should be searched")
arguments = parser.parse_args()
bib_path = arguments.bib_name       # absolute path to the .bib-file (as given by the user)
search_dir = arguments.search_dir


# First of all, create a back-up directory in the search directory
backup_dir = search_dir + '/replace_bib_script_backup'
if not os.path.isdir(backup_dir):
    os.mkdir(backup_dir)


# Specification of patterns and replace_withs for .tex-files and CMakeList.txt files
tex = Extension('.tex', patterns=[re.compile(r'\\bibliography{.*_bib}.*'), re.compile(r'\\bibliography{.*\.bib}.*')],
                replace_with=r'\\bibliography{{{}}}'.format(bib_path), absolute=True)  # for the .tex-files, the absolute path is OK to use FIXME: I think

cmakelists = Extension('CMakeLists.txt', patterns=[re.compile(r'BIBFILES.*_bib'), re.compile(r'BIBFILES.*\.bib')], replace_with=r'BIBFILES {}',
                       absolute=False)  # for any CMakeLists.txt files, a relative path is needed


print("Replacing bib-file occurrences with the newly provided bib-file name ...")

for extension in [tex, cmakelists]:
    all_file_substitute(extension, search_dir, backup_dir)

print("Done.")








