#!/usr/bin/env python3
# Name   : crypto.py
# Author : Rob Toscani
# Date   : 08-04-2024
# Description: crypto.py is an interactive program that proposes solutions for
# cryptogram- or crosswords problems. It finds all the possible words that fit
# the known and unknown cryptogram- or crosswords characters given.
# Perequisite is presence on the system of Dutch and British-English word lists
# in flat text format.
#
##############################################################################
#
# Copyright (C) 2024 Rob Toscani <rob_toscani@yahoo.com>
#
# crypto.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# crypto.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#
import sys
import time
import getopt
import os
import re

dutch          = "/usr/share/dict/dutch"
english        = "/usr/share/dict/british-english"
language_files = [dutch, english ]

os.system('clear')

print("""
\n\n\n\n\n\n\n\n\n
######################################
#                                    #
#                                    #
#                                    #
#           CRYPTO SOLVER            #
#                                    #
#                                    #
#                           (c) 2024 #
######################################

Just a moment please, 
preparing database ...
""")

time.sleep(1)

# Regular expressions:
dot     = re.compile('\.')
ij_low  = re.compile('ij')
ij_upp  = re.compile('IJ')
undersc = re.compile('_')
equal   = re.compile('=')

wordlist = []
for language in language_files:
    with open(language,'r') as f:
        if language == dutch:
            wordlist += [ij_low.sub('_', ij_upp.sub('=', x)) for x in f.read().splitlines()]
        else:
            wordlist += [x for x in f.read().splitlines()]

instruction = """
Type content of each cell in the right order: a letter character if known,
or otherwise a \".\" if a cell is still empty (type <Ctrl-C> to abort)\n
"""

while True:
    os.system('clear')
    while True:
        word = input(instruction)   
        if word == "":
            os.system('clear')
            print ("\n\a\a\aPlease provide input...\a\a\a\n")
            continue
        break
    print("\nFor " + word + ", the following solutions are possible:\n")

    dotsub = dot.sub('[_=0-9a-zA-Z]', word)
    regex = re.compile('^' + dotsub + '$')

    matchlist = list(filter(regex.match, wordlist))
    results = [undersc.sub('ij', equal.sub('IJ', x)) for x in matchlist]
    for result in results:
        print(result)
    reply = input("\nQuit ('q<rtn>') or continue (any other input)? ")
    if reply == "q":
        break
    continue
