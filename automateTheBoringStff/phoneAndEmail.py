#!/usr/bin/python3
# phoneAndEmail.py - finds phone numbers and email addr on clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?					#area code
	(\s|-|\.)?							#separator
	(\d{3})								#first 3 num
	(\s|-|\.)							#separator
	(\d{4})								#last 4 num
	(\s*(ext|x|ext.)\s*(\d{2,5}))?		#ext
	)''', re.VERBOSE)

# TODO: Create email regex.
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+		#username
	@						# at sym
	[a-zA-z0-9.-]+			#domain name
	(\.[a-zA-Z]{2,4})		#dot-something
	)''', re.VERBOSE)

# TODO: find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])
	

# TODO: copy restults to the clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to Clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')


