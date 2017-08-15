# qol
A repo with Quality of Life improving scripts. Install the scripts by running

    ./install.py ${INSTALL_DIR}

and adding INSTALL_DIR to your PATH (in your .bash_profile or .bashrc):

    export PATH=${INSTALL_DIR}:${PATH}

You can then call the scripts from anywhere.


extract
-------
Given a compressed file COMPRESSED_FILE, tries to extract it:

    extract COMPRESSED_FILE



new_software_project
----------------------
If you have ${SOFTWARE_DIR} exported, then you can call

    new_software_project PROJECT_NAME

to create a software project folder template in SOFTWARE_DIR.


tex_template
------------

    tex_template PROJECT_NAME PROJECT_DIR

creates a template LaTeX project PROJECT_NAME in the specified PROJECT_DIR, with cmake files also set to be used.


update_bib
-----------
First, let's give some context. Let's say you have many .tex-files in some directory (or subdirectories thereof) DIR, and you decide to move or rename (or use another) bibliography (.bib) file. In that case, this script will locate any instances of

    \bibliography{absolute/path/to/yourbibfile.bib}

in all .tex-files in DIR, and change them with

    \bibliography{BIB_PATH}

which is the absolute path (BIB_PATH) you have provided. Furthermore, it detects if you are using cmake and will replace any occurrences of

    BIB_FILES relative/path/to/yourbibfile.bib

in the corresponding CMakeLists.txt files by

    BIB_FILES relative/path/to/{BIB_PATH}


update_updmap
-------------
After a MacPorts update of texlive, the installation of the font MinionPro is broken. Running

    update_updmap

updates the updmap.cfg file so that MinionPro works again.



update_uselatex_symlinks
------------------------
Given the absolute path to a UseLATEX.cmake file (USELATEX_PATH),

    update_uselatex_symlinks USELATEX_PATH SEARCH_DIR

creates (if UseLATEX.cmake files were already there) or force (i.e. overwrites) replaces present symlinks to a (previous location to) a UseLATEX.cmake file to USELATEX_PATH.