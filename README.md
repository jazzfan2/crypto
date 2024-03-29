# Name: crypto.sh
crypto.sh - An interactive program that proposes solutions for cryptogram- or crosswords problems.

# Description:
crypto.sh finds all the possible words that fit the known and unknown cryptogram- or crosswords characters given. Perequisite is presence on the system at the following locations of Dutch and British-English word lists in flat text format:

	/usr/share/dict/dutch
	/usr/share/dict/british-english

If wished, above paths may be modified or removed and references to other word lists may be added, by modifying the program code accordingly.

# How to use crypto.sh:
After starting the program by typing the following command on the command line:

	crypto.sh

.. you are prompted to type the content of each cryptogram- or crosswords cell in the right order: a letter character if known, or otherwise a dot ('.') if a cell is still empty.

For instance, typing the query:

	p.p..r

... renders following possible solutions:

	papier
	pipser
	popper
	pepper
	poplar

To start a new query, type:

	q

To abort inputting a query and stop the program, type:

	<Ctrl-C>

# Author:
Written by Rob Toscani (rob_toscani@yahoo.com).
