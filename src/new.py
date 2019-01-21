#!/Users/laurentlemmens/miniconda/bin/python3

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
project_dir = os.getenv('SOFTWARE_DIR') + '/' + project_name  # project_dir includes the project name


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


# Filenames starting with a dot are special cases that are not matched, so we'll have to add them manually
hidden_filenames = glob.glob(qol_dir + '/docs/c++_library_template/.*')
for hidden_filename in hidden_filenames:
    all_template_filenames.append(hidden_filename)


# Copy the contents of every input file into the output file, but replace every occurrence of &PROJECT_NAME&
for filename in all_template_filenames:
    if '.' not in filename:  # this is a check if we're working with files, not directories
        continue

    if filename == 'wrapper_header.hpp':  # don't copy-paste the wrapper header template
        continue

    # We want to copy all files inside c++_library_template into the project_dir, so we have to figure out what the new filename (inside project_dir)
    filename_out = project_dir + '/' + os.path.relpath(filename, qol_dir + '/docs/c++_library_template/')
    print(filename_out)
    with open(filename, 'r') as f_in:
        os.makedirs(os.path.dirname(filename_out), exist_ok=True)  # make sure that intermediary directories exist
        with open(filename_out, 'w') as f_out:
            for line in f_in:
                f_out.write(line.replace('&PROJECT_NAME&', project_name))


# We'll do something special for the wrapper header
# Create a file with the name 'project_name' in the previously created library include directory
wrapper_header_filename = project_dir + '/include/' + project_name + '.hpp'
template_wrapper_header_filename = qol_dir + '/docs/c++_library_template/include/wrapper_header.hpp'
print(wrapper_header_filename)
with open(wrapper_header_filename, 'w') as f_out:
    with open(template_wrapper_header_filename, 'r') as f_in:
        for line in f_in:
            f_out.write(line.replace('&PROJECT_NAME&', project_name.upper()))

print("Done.")
