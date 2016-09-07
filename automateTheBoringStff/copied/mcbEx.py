#! /usr/bin/python3
# mcbEx.pyw - saves and loads pieces of text to the clipboard.
# Usage: save <keyword - saves clipboard to keyword.
#	 <keyword> - Loads keyword to clipboard.
#	 list - Loads all keywords to clipboard.
#	 DEL <keyword> - deletes keyword.
#	 DELALL -deletes all keywords and clears clipboard.

import shelve, pyperclip, sys

mcbExShelf = shelve.open('mcbEx')

#  TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbExShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1] == 'DEL' and sys.argv[2] in mcbExShelf.keys():
	del mcbExShelf[sys.argv[2]]

# Extended; delete all
# copy '' to clipboard to clear it

elif sys.argv[1] == 'DELALL':
	for i in list(mcbExShelf.keys()):
		del mcbExShelf[i]
		pyperclip.copy('')
	
elif len(sys.argv) == 2:
	# TODO: list keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbExShelf.keys())))
	elif sys.argv[1] in mcbExShelf:
		pyperclip.copy(mcbExShelf[sys.argv[1]])




mcbExShelf.close()  
	






