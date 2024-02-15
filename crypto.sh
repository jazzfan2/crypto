#!/bin/bash
# Name   : crypto.sh
# Author : Rob Toscani
# Date   : aug 2014
# Description: This script finds all the possible cryptogram- or crosswords words possible that fit the known or unknown characters given.
# Perequisite is presence on the system of Dutch and British-English word lists in flat text format.
#
##############################################################################
#
# Copyright (C) 2024 Rob Toscani <rob_toscani@yahoo.com>
#
# crypto.sh is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# crypto.sh is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#
dutch="/usr/share/dict/dutch"
british_english="/usr/share/dict/british-english"
clear
echo -e "\n\n\n\n\n\n\n\n\n\n\n\n"
echo "                ####################################################"
echo "                #                                                  #"
echo "                #                                                  #"
echo "                #                                                  #"
echo "                #                   CRYPTO SOLVER                  #"
echo "                #                                                  #"
echo "                #                                                  #"
echo "                #                                                  #"
echo "                ####################################################"
sleep 1
while true; do
    clear
    while true; do
    	echo -e "Type content of each cell in the right order: a letter character if known,\nor otherwise a \".\" if a cell is still empty (type <Ctrl-C> to abort)"   
	    read "word"
	    [ -z $word ] && clear && echo -e "\n\a\a\aPlease provide input...\a\a\a\n" &&
        continue
	    break
    done
    echo "For "$word", the following solutions are possible:"
    sleep 2
    grep "^${word//./[0-9a-zA-Z]}$" $dutch $british_english | awk 'BEGIN { FS = ":" }{ print $2 }' | less
done
#
#
################################################################################################################
#
