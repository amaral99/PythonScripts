'''print('enter the name of cat1:')
catName1 = input()
print('enter the name of cat2:')
catName2 = input()
print('enter the name of cat3:')
catName3 = input()
print('enter the name of cat4:')
catName4 = input()
print('enter the name of cat5:')
catName5 = input()
print('enter the name of cat6:')
catName6 = input()
print('the cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' +catName4 + ' ' + ' ' + catName5 + ' ' +catName6)'''

'''catNames = []
while True:
	print('enter the name of cat ' + str(len(catNames) + 1) + '(or enter nothing to stop.):')
	name = input()
	if name == '':
		break
	catNames = catNames + [name] #list concatenation

print('The cat names are:')
for name in catNames:
	print(' ' + name)
print(catNames)'''

myPets = ['zophie', 'pooka', 'fat-tail']
print('enter a pet name:')
name = input()
if name not in myPets:
	print('I do not have a pet named ' + name)
else:
	print(name + ' is my pet.')

