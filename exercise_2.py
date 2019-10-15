

num = input('Enter a number and i will tell you if it is \
odd or even \n==> ')

if int(num) % 2 == 0:
	print(str(int(num)) + ' is an even number.')
	if int(num) % 4 == 0:
		print(str(int(num)) + ' is divisible by 4')
else:
	print(str(int(num)) + ' is an odd number.')	

num2 = input('Enter a number >> ')
num3 = input('Enter another number >> ')
if num2 == num3:
	print(str(num2) + ' is equal to ' + str(num3) + '.')	
else:
	print(str(num2) + ' is not divisible by ' + str(num3) )	