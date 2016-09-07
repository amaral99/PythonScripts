birthdays = {'alice': 'apr 1', 'bob': 'dec 12', 'carol': 'mar 4'}

while True:
	print('enter a name: (blank to quit)')
	name = input()
	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('i do not have birthday info for ' + name)
		print('what is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('birthday database updated')
		print (birthdays)
