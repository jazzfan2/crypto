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
import os
import re

dutch          = "/usr/share/dict/dutch"
english        = "/usr/share/dict/british-english"

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

wordlist = [ [], [] ]
for language in (dutch, english):
    with open(language,'r') as f:
        if language == dutch:
            wordlist[0] = [x.replace('ij', '_').replace('IJ', '=') for x in f.read().splitlines()]
        else:
            wordlist[1] = [x for x in f.read().splitlines()]
for i in (0,1):
    wordlist[i] = [x.replace('.', '').replace('-', '').replace(' ', '').replace('\'', '') \
                   for x in wordlist[i]]

instruction = """
Type content of each cell in the right order: a letter character if known,
or otherwise a \".\" if a cell is still empty (type <Ctrl-C> to abort)\n
"""

while True:
    os.system('clear')
    while True:
        try:
            word = input(instruction)
        except:
            os.system('clear')
            sys.exit()
        if word == "":
            os.system('clear')
            print ("\n\a\a\aPlease provide input...\a\a\a\n")
            continue
        break
    print("\nFor " + word + ", the following solutions are possible:\n")


    # Dutch:
    # dotword = word.replace('.', '[_=0-9a-zA-ZáàäâåÁÀÄÂéèëêÉÈËÊïíìÏÍÌóòöôøÓÒÖÔüûÜÛñÑçÇ]')
    dotword = word.replace('.', '(_|=|\w)')
    dotword = dotword.replace('ij', '_')
    dotword = dotword.replace('IJ', '=')
    regex_nl = re.compile('^' + dotword + '$')

    # English:
    dotword = word.replace('.', '\w')
    regex_en = re.compile('^' + dotword + '$')

    for language in [dutch, english]:
        if language == dutch:
            matchlist = [x.replace('_', 'ij').replace('=', 'IJ') \
                        for x in list(filter(regex_nl.match, wordlist[0]))]
        else:
            matchlist = list(filter(regex_en.match, wordlist[1]))

        for result in matchlist:
            print(result)
        print()

    try:
        reply = input("\nQuit ('q<rtn>') or continue (any other input)? ")
    except:
        os.system('clear')
        sys.exit()
    if reply == "q":
        break
    continue
