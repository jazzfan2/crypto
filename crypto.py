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

wordlist = []
for language in [dutch, english]:
    with open(language,'r') as f:
        if language == dutch:
            wordlist += [x.replace('ij', '_').replace('IJ', '=') for x in f.read().splitlines()]
        else:
            wordlist += [x for x in f.read().splitlines()]

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

    dotword = word.replace('.', '[_=0-9a-zA-Z]')
    regex = re.compile('^' + dotword + '$')

    matchlist = list(filter(regex.match, wordlist))
    results = [x.replace('_', 'ij').replace('=', 'IJ') for x in matchlist]
    for result in results:
        print(result)
    try:
        reply = input("\nQuit ('q<rtn>') or continue (any other input)? ")
    except:
        os.system('clear')
        sys.exit()
    if reply == "q":
        break
    continue
