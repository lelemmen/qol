#!/Users/laurentlemmens/miniconda/bin/python3


import os
import pathlib
import shutil



# Get the personal temporary directory from the environment
tmp_directory_path = "/Users/laurentlemmens/Software/tmp"
cpp_tmp_dir = os.path.join(tmp_directory_path, 'C++')
python_tmp_dir = os.path.join(tmp_directory_path, 'Python')


# Remove everything that's in it
shutil.rmtree(tmp_directory_path)


# Remake the Python and C++ directories
pathlib.Path(cpp_tmp_dir).mkdir(parents=True)
pathlib.Path(python_tmp_dir).mkdir(parents=True)
