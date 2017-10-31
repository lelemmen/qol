#!/usr/bin/env python3

# Extracts any of the following files:
#   .tar, .tar.gz, tar.xz, .zip

import tarfile
import zipfile
import argparse


# Parse the argument
parser = argparse.ArgumentParser(description="Extracts a given file.")
parser.add_argument('filename', type=str, help="the path to the file you want to extract")
arguments = parser.parse_args()
filename = arguments.filename


print("Trying to extract the given file ...")

if filename.endswith('.tar.gz') or filename.endswith('.tar') or filename.endswith('tar.xz'):
    with tarfile.open(filename) as tarf:
        tarf.extractall()
elif filename.endswith('.zip'):
    with zipfile.ZipFile(filename, 'r') as zipf:
        zipf.extractall()
else:
    raise IOError("Cannot extract the given file.")

print("Done.")
