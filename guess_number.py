import random

r = random.randint(1, 100)
count = 0

while True:
	n = input("please guess the number between 1 to 100: ")
	n = int(n)
	count += 1
	print("tries:", count)

	if n == r:
		print("you guess the right number!")
		break	
	if n > 100 or n < 1:
		print("enter an interger between 1 and 100")
	elif n > r:
		print("the answer is less than", n)
	elif n < r:
		print("the answer is greater than", n)


