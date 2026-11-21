#!/bin/bash
# Name: GETCRYPTO.command
# Author: R.J.Toscani
# Date: 21st November 2026
# Description: "Button"-program for starting a Terminal pop-up running 'crypto.py'
# on a MacOS-X computer. NOT TESTED YET.
# See also:
# https://superuser.com/questions/174576/opening-a-new-terminal-from-the-command-line-and-running-a-command-on-mac-os-x      
#
#################################################################################
#


osascript -e 'tell app "Terminal"
    do script "myloc="$( ( OLDPWD=- CDPATH= cd -P -- "$(dirname $0)" && pwd ) ); cd "$myloc"; ./crypto.py"
end tell'

# osascript -e 'tell app "Terminal" to activate' \
#           -e 'tell app "Terminal" to do script "myloc="$( ( OLDPWD=- CDPATH= cd -P -- "$(dirname $0)" && pwd ) ); cd "$myloc"; ./crypto.py"'