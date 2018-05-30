#!/opt/local/bin/python3

# This script automatically adds, commits, and pushes any changes to the given directory

import argparse
import datetime
import subprocess


# Parse the git_dir argument and check if it is an absolute path
parser = argparse.ArgumentParser(description="Add, commit, push any changes to the given directory.")
parser.add_argument('git_dir', type=str, help="the git directory in which changes should be pushed")
arguments = parser.parse_args()

git_dir = arguments.git_dir

if git_dir[0] != '/':
    raise ValueError("The given directory is not an absolute path.")



# Do the git commands
# source: a comment on the answer (https://superuser.com/a/905246)
subprocess.call(['git', '-C', git_dir, 'add', '.'])  # git add
subprocess.call(['git', '-C', git_dir, 'commit', '-m', '"autocommit changes to {} on {}"'.format(git_dir, datetime.datetime.now())])
subprocess.call(['git', '-C', git_dir, 'push'])
