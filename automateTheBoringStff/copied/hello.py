'''def hello():
    print('howdy')
    print('no fuck off')
    print('cunt!')

hello()
hello()
hello()'''

def hello(name):
    print('hello ' + name)

hello('alice')
hello('fuck face')

import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Itis certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber == 4:
        return 'reply hazy try again'
    elif answerNumber == 5:
        return 'ask again later'
    elif answerNumber == 6:
        return 'concentrate and ask again'
    elif answerNumber == 7:
        return 'my rply is no'
    elif answerNumber == 8:
        return 'outlook not so good'
    elif answerNumber == 9:
        return 'ver doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print (r)
print()
print (fortune) 
print()
print(getAnswer(random.randint(1, 9)))


print('hello', end='')
print('world')

#Name

'''def spam():
    eggs = 'spam local'
    print(eggs)#prints spam local

def bacon():
    eggs = 'bacon local'
    print(eggs)

spam()

eggs='global'

bacon()

print(eggs)
print()'''
print()
#same-name

'''def spam():
    global eggs
    eggs = 'spam'
    
eggs= 'global'
spam()

print (eggs)
print("break")'''
def spam():
	global eggs
	eggs = 'spam' #this is the global

def bacon():
	eggs = 'bacon' #this is  a local

def ham():
	print(eggs) #global

eggs = 42 #global
spam()
print(eggs)


