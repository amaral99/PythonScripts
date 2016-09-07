import random

messages = ['it is certain', 'it is decidedly so', 'yes definitely', 'reply hazy try again', 'ask again later', 'concentrate and ask again', 'my reply is no', 'outlook not so good', 'very doubtful']

print (messages[random.randint(0, len(messages) -1)])

def eggs(someParameter):
	someParameter.append('hello')

spam = [1,2,3]
eggs(spam)
print (spam)
print()

spam = ['apples', 'bananas', 'tofu', 'cats']

'''def list(spam):
	spam[-1] = 'and ' + spam[-1]
	str(spam)
	print (spam)
list(spam)'''

print()

def comma(aList):
	count=0
	a_string=''
	while count < len(aList) -1:
		a_string += aList[count] + ','
		#string = spam - 1
		count += 1
	print(a_string)
	print (aList[count])
	return a_string + 'and ' + aList[count]
print (comma(spam))
