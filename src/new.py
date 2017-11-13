#!/usr/bin/env python3

import argparse
import os
import glob


# Create new projects by running this command. The project will be placed inside the ${SOFTWARE_DIR}
#   Example usage:
#       new library


# Parse the arguments
parser = argparse.ArgumentParser(description="Create a new project.")
parser.add_argument('type', type=str, help="For now, the only supported type is 'library'.")
parser.add_argument('name', type=str, help="The project name")
arguments = parser.parse_args()
project_type = arguments.type
project_name = arguments.name

# Since we know what the project's name is going to be, we can figure out the installation path
project_dir = os.getenv('SOFTWARE_DIR') + '/' + project_name


# Make sure that the user knows that we only support 'library' for now
if project_type != 'library':
    raise ValueError("For now, the only supported type is 'library'")


# Find out the directory in which the QoL scripts are, in order to locate qol/docs/c++_library_template
this_script_dir = os.path.dirname(os.path.realpath(__file__))  # directory that contains this file, resolving any symlinks
qol_dir = '/'.join(this_script_dir.split('/')[:-1])


# Copy the contents of qol/docs/c++_library_template into the new project name
# Replace all occurrences of &PROJECT_NAME& with the actual project_name
print("Copying files from {} into {} ...".format(qol_dir + '/docs/c++_library_template', project_dir))
print("Customizing the preset template ...")
all_template_filenames = glob.glob(qol_dir + '/docs/c++_library_template/**', recursive=True)  # the pattern “**” will match any files and zero or more directories and subdirectories

for filename in all_template_filenames:
    if '.' not in filename:  # this is a check if we're working with files, not directories
        continue

    # We want to copy all files inside c++_library_template into the project_dir, so we have to figure out what the new filename (inside project_dir)
    filename_out = project_dir + '/' + os.path.relpath(filename, qol_dir + '/docs/c++_library_template/')
    print(filename_out)
    with open(filename, 'r') as f_in:
        os.makedirs(os.path.dirname(filename_out), exist_ok=True)  # make sure that intermediary directories exist
        with open(filename_out, 'wt') as f_out:
            for line in f_in:
                f_out.write(line.replace('&PROJECT_NAME&', project_name))

print("Done.")
