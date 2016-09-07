#! /user/bin/python3
# mcb.pyw - saves and loads pieces of text to the clipboard.
# Usage: save <keyword - saves clipboard to keyword.
#	 <keyword> - Loads keyword to clipboard.
#	 list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#  TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	# TOD: list keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

#  TODO: List keywords and load content.

mcbShelf.close()
