#! /usr/bin/python3
# stopwatch.py - a simple stopwatch program.

import time

# Display the program's instructions
print('Press ENTER to begin. then, press ENTER to click the stopwatch.  Press Ctrl-C to quit.')
input()		# press enter to begin
print('Started.')
startTime = time.time() 	# get the first lap start time
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() # reset the last lap time 
except KeyboardInterrupt:
	# handle the Ctl-C exc for err messgs
	print('\nDone.')

