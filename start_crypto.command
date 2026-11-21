#!/bin/bash
# Name: start_crypto.command
# Author: R.J.Toscani
# Date: 21st November 2026
# Description: Start a Terminal pop-up running 'crypto.py' on a MacOS-X computer
# NOT TESTED YET
#
###############################################################################
#

# https://superuser.com/questions/174576/opening-a-new-terminal-from-the-command-line-and-running-a-command-on-mac-os-x
# Substitute <full_path_to_crypto.py> string by actual path to the program:
osascript -e 'tell app "Terminal"
    do script "<full_path_to_crypto.py>"
end tell'

# osascript -e 'tell app "Terminal" to activate' -e 'tell app "Terminal" to do script "<full_path_to_crypto.py>"'