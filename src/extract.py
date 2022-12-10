#!/Users/laurentlemmens/miniconda/bin/python3

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
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tarf)
elif filename.endswith('.zip'):
    with zipfile.ZipFile(filename, 'r') as zipf:
        zipf.extractall()
else:
    raise IOError("Cannot extract the given file.")

print("Done.")
