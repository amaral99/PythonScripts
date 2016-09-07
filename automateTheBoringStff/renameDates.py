#! /usr/bin/python3
# renameDates.py - Renames filenaes with American MM-DD-YY form
# to Eur DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the Amer format
datePattern = re.compile(r"""^(.*?)  # ALL TEXT BEFORE DATE 
	((0|1)?\d)- 					 # 1 OR 2 DIG FOR MONTH	
	((0|1|2|3)?\d)-					 # 1 OR 2 DIG FOR DAY
	((19|20)\d\d)					 # FOUR DIG FOR YEAR
	(.*?)$							 # ALL TEXT AFTER DATE
	""", re.VERBOSE) 

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)

	# TODO: Skip files without a date.
	if mo == None:
		continue

	# TODO: Get the different parts of the file name.
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# TODO: Form the European-style filename.
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	# TODO: Get the full, absolute file paths.
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)

	# TODO: Rename the files.  
	print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
	shutil.move(amerFilename, euroFilename) # Uncomment after testing
