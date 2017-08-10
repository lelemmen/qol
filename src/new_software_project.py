#!/usr/bin/env python3

# Create a new software project template in the ${SOFTWARE_DIR}, with
#   $1: project_name
# The template looks as follows:
# 	project_name
#       |
#       |_____src
#       |
#       |_____docs
#       |
#       |_____tests
#       |
#       |_____build


import argparse
import os


# Parse the arguments
#   the first argument is the project name
parser = argparse.ArgumentParser(description="Create a new software project (directory tree).")
parser.add_argument('project_name', type=str, help='the name of the new project')
arguments = parser.parse_args()
project_name = arguments.project_name


# If the SOFTWARE_DIR variable is not set in the environment or it is empty, ignore the program
error_message = "The environment variable SOFTWARE_DIR is "

if 'SOFTWARE_DIR' not in os.environ:
    raise OSError(error_message + "not set.")
elif not os.environ['SOFTWARE_DIR']:
    raise OSError(error_message + "empty")
else:
    SOFTWARE_DIR = os.environ['SOFTWARE_DIR']


# Create the directory tree
print("Making a new software project: '{}'".format(project_name))

os.mkdir(SOFTWARE_DIR + '/' + project_name)
os.mkdir(SOFTWARE_DIR + '/' + project_name + '/' + 'src')
os.mkdir(SOFTWARE_DIR + '/' + project_name + '/' + 'docs')
os.mkdir(SOFTWARE_DIR + '/' + project_name + '/' + 'tests')
os.mkdir(SOFTWARE_DIR + '/' + project_name + '/' + 'build')

print("Done.")
