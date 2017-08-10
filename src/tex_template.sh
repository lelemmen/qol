#!/bin/bash

### This script makes a template LaTeX project.
###	$1: project_name
### is the name you want your LaTeX project, so we end up with project_name.tex, which is based on the latex template (template.tex).
###	$2: project_dir
### is the (top-level, i.e. all files are put here) directory you would like the project to be created in.
### Furthermore, the necessary files to be able to use cmake will be provided in the project_dir as well.

## Variable extraction
project_name=$1
project_dir=$2
MY_DIR=$(dirname $(readlink ${0}))

## CMake
# Copy the cmake dir to project_dir (this directory contains UseLatex.cmake)
echo "Copying cmake files ..."
cp -R ${MY_DIR}/cmake ${project_dir}

# Copy and edit (no backup, replace 'project_name' by its actual value) the CMakeLists template
cp ${MY_DIR}/CMakeLists_template.txt ${project_dir}/CMakeLists.txt
echo "Updating CMakeLists ..."
sed -i ""  "s/project_name/${project_name}/g" ${project_dir}/CMakeLists.txt


## LaTeX
# Copy the LaTeX template
echo "Copying the LaTeX template ..."
cp ${MY_DIR}/template.tex ${project_dir}/${project_name}.tex
