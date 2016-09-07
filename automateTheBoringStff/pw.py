#! /usr/bin/python3 
# pw.py - an nsecure password locker program

PASSWORDS = {'email': 'thisismypassword', 'blog': 'password2', 'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('usage: python pw.py [account] - copy account passowrd')
	sys.exit() 
	
account = sys.argv[1] #first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('password for ' + account + ' copied to clipboard.')
else:
	print('there is no acount named ' + account)	
