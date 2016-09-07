#! /usr/bin/python3
# combinePdfs.py - Combines all the PDFs in the current working directory into a singel PDF

import PyPDF2, os

# Get all the PDF files.
pdfFiles = []
for filename in os.listdir('/home/jesse/Dropbox/computers/Automate the Boring Stuff with Python - Practical Programming for Total Beginners - 1st Edition (2015) (Pdf, Epub & Mobi) Gooner/automate_online-materials'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# TODO: Loop through all the PDF files.
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	# TODO: Loop through all the pages (except the first and add them.
	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# TODO: Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

