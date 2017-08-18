#!/usr/bin/env python3

# If the 'share - AirDrop' option isn't available anymore, running this script will re-enable it.

import subprocess

subprocess.call(['/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister', '-kill', '-seed'])
