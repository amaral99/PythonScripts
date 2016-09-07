#! /usr/bin/python3

# walk the folders; locate file type, move all file type to new folder

import os, shutil

def selectiveCopy(folder, fileType):
	folder = os.path.abspath(folder)
	desFolder = os.path.abspath('/home/jesse/Dropbox/copied')
	
	for foldername, subfolder, filenames in os.walk(folder):
		#print('Looking in folders %s...' % (foldername))
		for filename in filenames:
			if filename.endswith(fileType):
				#print (foldername + '/' + filename)
				
				shutil.copy(filename, desFolder)

selectiveCopy('/home/jesse/Dropbox', '.epub')


