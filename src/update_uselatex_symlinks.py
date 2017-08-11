#!/usr/bin/env python3

# In a given directory, replace all UseLATEX.cmake symlinks with the given filename (absolute path to UseLATEX.cmake)


import argparse
import glob
import os


# Parse the arguments
#   the first argument is the name of the new bib-file
#   the second argument is the directory in which should be searched

parser = argparse.ArgumentParser(description="Replace UseLATEX.cmake symlinks to new ones.")
parser.add_argument('uselatex_path', type=str, help="the path to the UseLATEX file")
parser.add_argument('search_dir', type=str, help="the directory in which should be searched")
arguments = parser.parse_args()
uselatex_path = arguments.uselatex_path     # absolute path to the .bib-file (as given by the user)
search_dir = arguments.search_dir


# Search for all UseLATEX.cmake files in the search_dir
for file_path in glob.iglob(search_dir + '/**/UseLATEX.cmake', recursive=True):  # iglob returns an iterator
    # Force create symlinks, overwriting previous ones
    print("{target} -> {source}".format(source=uselatex_path, target=file_path))
    try:
        os.symlink(uselatex_path, file_path)
    except FileExistsError:
        os.remove(file_path)
        os.symlink(uselatex_path, file_path)
