# Name: crypto.py
crypto.py - An interactive program that proposes solutions for cryptogram- or crosswords problems.

# Description:
crypto.py finds all the possible words that fit the known and unknown cryptogram- or crosswords characters given. Perequisite is presence on the system at the following locations of Dutch and British-English word lists in flat text format:

	/usr/share/dict/dutch
	/usr/share/dict/british-english

If wished, above paths may be modified or removed and references to other word lists may be added, by modifying the program code accordingly.

# How to use crypto.sh:
After starting the program by typing the following command on the command line:

	crypto.py

.. you are prompted to type the content of each cryptogram- or crosswords cell in the right order: a letter character if known, or otherwise a dot ('.') if a cell is still empty.

For instance, typing the query:

	p.p..r

... renders following possible solutions:

	papier
	pipser
	popper
	pepper
	poplar

To stop the program after a query result, type:

	q <Enter>

To continue for a new query, type:

    <Enter>

To abort while already in input mode, type:

	<Ctrl-C>

# Author:
Written by Rob Toscani (rob_toscani@yahoo.com).
