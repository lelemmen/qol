#!/usr/bin/env python3

import argparse
import glob
import os



# Parse the arguments
#   the first argument is the direction in which the symlinks will be placed
parser = argparse.ArgumentParser(description="Install the QoL scripts.")
parser.add_argument('install_dir', type=str, help="directory in which the symlinks have to be placed")
arguments = parser.parse_args()

install_dir = arguments.install_dir


# Find out the directory in which the QoL scripts are
qol_dir = os.path.dirname(os.path.realpath(__file__))    # directory that contains this file, resolving any symlinks


for script_py in glob.iglob(qol_dir + '/src/*.py', recursive=True):
    script_without_extension = os.path.basename(script_py.replace('.py', ''))

    # Create symlinks for every script, overwriting previous ones
    print("{target} -> {source}".format(source=script_py, target=install_dir + '/' + script_without_extension))
    try:
        os.symlink(script_py, install_dir + '/' + script_without_extension)
    except FileExistsError:
        os.remove(install_dir + '/' + script_without_extension)
        os.symlink(script_py, install_dir + '/' + script_without_extension)


if install_dir not in os.environ['PATH'].split(':'):
    print("WARNING: The directory provided for installation ({install_dir}) is not present in your PATH. If you want full functionality, please add that directory to your PATH".format(install_dir=install_dir))
