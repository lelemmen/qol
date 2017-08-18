#!/usr/bin/env python3

# This script will update the updmap.cfg-file, in order to let the font types MinionPro work again after a texlive update.

import subprocess

# For a MacPorts installation, updmap.cfg can be found here
updmap_path = '/opt/local/var/db/texmf/web2c/updmap.cfg'


print("Updating updmap ... ")
subprocess.call(['updmap-sys', '--enable', 'Map=MinionPro.map'])


print("Updating the texlive-tree ... ")
subprocess.call(['sudo', 'mktexlsr', '$(kpsewhich -var TEXMFLOCAL)'])


print("Done.")
