#!/opt/local/bin/python3

# Clean my ~/Documents/ folder from League of Legends and Mathematica folders


import os
import shutil


home = os.path.expanduser("~")
league_path = home + "/Documents/League of Legends"
mathematica_path = home + "/Documents/Wolfram Mathematica"

def remove_if_exists(path_to_dir):

    try:
        shutil.rmtree(path_to_dir)  # remove a directory recursively
    except FileNotFoundError:
        pass



print("Removing the League of Legends folder ...")
remove_if_exists(league_path)

print("Removing the Mathematica folder ...")
remove_if_exists(mathematica_path)

print("Done")
