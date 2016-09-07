#! /usr/bin/python3
# countdown.py - a simple countdown script.

import time, subprocess

timeLeft = 10 
while timeLeft > 0:
	print(timeLeft)
	time.sleep(1)
	if timeLeft == 5:
		print('get ready')	
	timeLeft = timeLeft - 1

# TODO: at the end of the countdown, play a sound.  
subprocess.Popen(['see', 'Off The Record - My Morning Jacket-zGTpw_9o65w.m4a'])
