#!/Users/laurentlemmens/miniconda/bin/python3

# This script will update the updmap.cfg-file, in order to let the font type MinionPro work again after a texlive update.

import subprocess


# For a MacPorts installation, updmap.cfg can be found here

print("Updating updmap ... ")
subprocess.call(['updmap-sys', '--enable', 'Map=MinionPro.map'])


print("Updating the texlive-tree ... ")
subprocess.call(['sudo', 'mktexlsr', '$(kpsewhich -var TEXMFLOCAL)'])


print("Done.")
