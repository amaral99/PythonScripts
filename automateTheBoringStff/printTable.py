tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


'''for li in tableData:
	for i in range(len(li)):
		print (tableData)'''
















'''#tableDataData = ['apples', 'oranges', 'cherries', 'banana']

def printtableData(tableData):
	
	print(tableData)


#print(str(tableDataData))
for a in range(len(tableDataData)):
	#for b in range(len(tableDataData[0])): 
		#print(' '.join(tableDataData[a]))
	print(tableDataData[a].rjust(7, '.'))'''



def printtableData(tableData):
# initialize the list "colWidths" with zeroes equal to the length of the input list
	colWidths = [0] * len(tableData)

# iterate over the input list to find the longest word in each inner list
# if its larger than the current value, set it as the new value
	for i in range(len(tableData)):
	    for j in range(len(tableData[i])):
	        if len(tableData[i][j]) > colWidths[i]:
	            colWidths[i] = len(tableData[i][j])

# assuming each inner list is the same length as the first, iterate over the input list
# printing the x value from each inner list, right justifed to its corresponding value
# in colWidths
	for x in range(len(tableData[0])):
		for y in range(len(tableData)):
			print(tableData[y][x].rjust(colWidths[y]), end = ' ')
			print('')


printtableData(tableData)
