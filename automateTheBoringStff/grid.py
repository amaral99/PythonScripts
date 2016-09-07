grid = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']] 

'''def flip(grid):
	string = ''
	for i in range(len(grid[0])):
		for j in range(len(grid)):
			#string += i
			print (str(grid[i]))
			
	
flip(grid)

print()

print(len(grid))'''

for j in range(len(grid[0])):
	
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print('')
