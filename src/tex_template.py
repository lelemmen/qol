#!/usr/bin/env python3

# This script makes a template LaTeX project.
#   the first argument parsed is the name you want your LaTeX project, so we end up with project_name.tex, which is based on the latex template (template.tex).
#   the second argument parsed is the (top-level, i.e. all files are put here) project directory you would like the project to be created in.
# Furthermore, the necessary files to be able to use cmake will be provided in the project directory as well.


import argparse
import os
import shutil


# Parse the arguments
#   the first argument is the project name
#   the second argument is the project directory

parser = argparse.ArgumentParser(description="Create a template LaTeX project.")
parser.add_argument('project_name', type=str, help="the name of the LaTeX project")
parser.add_argument('project_dir', type=str, help="the directory in which the template LaTeX project should be placed")
arguments = parser.parse_args()

project_name = arguments.project_name
project_dir = arguments.project_dir

# Find out the directory in which the QoL scripts are
this_script_dir = os.path.dirname(os.path.realpath(__file__))    # directory that contains this file, resolving any symlinks
qol_dir = '/'.join(this_script_dir.split('/')[:-1])


# CMake
# -----
# Copy the cmake directory (which contains UseLatex.cmake) to project_dir
print("Copying cmake files ...")
shutil.copytree(qol_dir + '/docs/cmake', project_dir + '/cmake')

# Copy and edit the CMakeLists template: replace 'project_name' with its actual value
print("Updating CMakeLists ...")
with open(qol_dir + '/docs/CMakeLists_template.txt', 'r') as f_in:
    with open(project_dir + '/CMakeLists.txt', 'wt') as f_out:
        for line in f_in:
            f_out.write(line.replace('project_name', project_name))


# LaTeX
# -----
print("Copying the LaTeX template ...")
shutil.copy2(qol_dir + '/docs/template.tex', project_dir + '/' + project_name + '.tex')


print("Done.")