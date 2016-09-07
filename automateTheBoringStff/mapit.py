#! /usr/bin/python3
# mapit.py - launches a map in the browser through ComLine

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])

#TODO: Get address form clipboard. 
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

