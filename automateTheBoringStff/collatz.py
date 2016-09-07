print ('enter a number')

try:
	num = int(input())
except ValueError:
	print('enter a number you dumb fuck')


def collatz(num):
	while num != 1:
		if num % 2 == 0:
			num = num // 2
			print(num)
			#return num // 2
		elif num % 2 == 1:
			num = 3 * num + 1
			print(num)
			#return 3 * num + 1
		#elif num == 1:
		continue 
		
collatz(num)




