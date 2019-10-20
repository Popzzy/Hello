num = input('Enter a number and i will tell you if it is \
    odd or even \n==> ')                                    # Man i form yauandika
                                                            # ivi nmejua saa ii 😜😜😜😜

if int(num) % 2 == 0:
	print(str(int(num)) + ' is an even number.')            # apa kuna redundacy str(int(num)) 
                                                            # ungeeka tu ivi iacha tu ikiwa num since ni string already
	if int(num) % 4 == 0:
		print(str(int(num)) + ' is divisible by 4')
else:
	print(str(int(num)) + ' is an odd number.')	

"""Alternatively"""
# first check if input is number/digit
if num.isdecimal():
    if int(num) % 2 == 0:
        print(num + ' is an even number.')
    if int(num) % 4 == 0:
        print(str(int(num)) + ' is divisible by 4')



num2 = input('Enter a number >> ')
num3 = input('Enter another number >> ')

#Not what was expected for this part of the question lazima uangalie kaa number inaweza divide iyo ingine
#
"""if num2 == num3:
    print(str(num2) + ' is equal to ' + str(num3) + '.')    
else:
    print(str(num2) + ' is not divisible by ' + str(num3) )    
"""
