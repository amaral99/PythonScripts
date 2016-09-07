#! /usr/bin/python3
#bulletPoint.py - adds wiki bullet point to the start
#of each line

import pyperclip
text = pyperclip.paste()

#Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  #loop  all indx in lines
	lines[i]= '* ' + lines[i] # adds star
text = '\n'.join(lines)

pyperclip.copy(text)

