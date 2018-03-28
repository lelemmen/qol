#!/usr/bin/env python3



import argparse
import glob
import os
from os.path import expanduser
from sys import platform
import subprocess



#
### HELPER FUNCTIONS
#
def overwrite_symlink(source, target):
    """Create a symlink or overwrite one."""
    try:
        os.symlink(source, target)
    except FileExistsError:
        os.remove(target)
        os.symlink(source, target)




#
### MAIN PROGRAM
#

# Parse the arguments
#   the first argument is the direction in which the symlinks will be placed
parser = argparse.ArgumentParser(description="Install the QoL scripts.")
parser.add_argument('install_dir', type=str, help="directory in which the symlinks have to be "
                                                  "placed")
arguments = parser.parse_args()

install_dir = arguments.install_dir


# Find out the directory in which the QoL scripts are, resolving any symlinks
qol_dir = os.path.dirname(os.path.realpath(__file__))


# Install python scripts
for script_py in glob.iglob(qol_dir + '/src/*.py', recursive=True):
    script_without_extension = os.path.basename(script_py.replace('.py', ''))

    # Create symlinks for every script, overwriting previous ones
    overwrite_symlink(script_py, install_dir + '/' + script_without_extension)

    print("{target} -> {source}".format(source=script_py, target=install_dir + '/' +
                                                                 script_without_extension))


if install_dir not in os.environ['PATH'].split(':'):
    print("WARNING: The directory provided for installation ({install_dir}) is "
          "not present in your PATH. If you want full functionality, please add "
          "that directory to your PATH".format(install_dir=install_dir))


# If on macOS, create symlinks for the Daemons and activate them
if platform == 'darwin':
    home = expanduser('~')
    daemon_directory = home + "/Library/LaunchAgents"

    for daemon_file_name in glob.iglob(qol_dir + '/src/daemons/*.plist', recursive=True):
        base_daemon_file_name = os.path.basename(daemon_file_name)

        # Create symlinks for the Daemons
        overwrite_symlink(daemon_file_name, daemon_directory + '/' + base_daemon_file_name)

        print("{target} -> {source}".format(source=daemon_file_name,
                                            target=daemon_directory + '/' + base_daemon_file_name))


        # Activate the Daemons
        subprocess.run(["launchctl", "load", daemon_directory + '/' + base_daemon_file_name])
