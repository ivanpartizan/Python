# 01 Variables

# Write a program that uses input to prompt a user for their name and then welcomes them.
# Enter your name: Chuck
# Hello Chuck
name = input('Enter your name: ')
print('Hello', name)

# Write a program to prompt the user for hours and rate per hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = float(hours) * float(rate)
print('Pay:', pay)

# 02 Conditionals

# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
if float(hours) > 40:
	overtime = float(hours) - 40
	pay = overtime * 1.5 * float(rate) + float(rate) * 40
else: 
	pay = float(hours) * float(rate)
print('Pay:', pay)

# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
	float(hours)
	float(rate)

	if float(hours) > 40:
			overtime = float(hours) - 40
			pay = overtime * 1.5 * float(rate) + float(rate) * 40
			print('Pay:', pay)
	else: 
			pay = float(hours) * float(rate)
			print('Pay:', pay)
except: 
	print('Error, please enter numeric input')

# 03 Functions

# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
h = input('Enter Hours: ')
r = input('Enter Rate: ')

def computepay(hours, rate):
	try:
		float(hours)
		float(rate)

		if float(hours) > 40:
				overtime = float(hours) - 40
				pay = overtime * 1.5 * float(rate) + float(rate) * 40
				# print('Pay:', pay)
		else: 
				pay = float(hours) * float(rate)
				# print('Pay:', pay)
		return pay
	except: 
		print('Error, please enter numeric input')

payment = computepay(h, r)
print("Payment:", payment)

# 04 Iterations

# Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
sum = 0
count = 0
while True:
	number = input('Enter a number: ')
	if number == 'done':
		break
	try: 
		number = float(number)
		sum = sum + number
		count = count + 1
	except:
		print('Invalid input')
	
print('Sum:', sum, 'Count:', count, 'Average:', sum / count)

# 05 Strings

# Take the following Python code that stores a string: str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
str = 'X-DSPAM-Confidence:0.8475'
colon_position = str.find(':')
number = float(str[colon_position + 1:])
print(number)
print(type(number))

# 06 Files

# Write a program to read through a file and print the contents of the file (line by line) all in upper case. 
file = input('Enter a file name: ')
text = open(file)
for line in text:
	line = line.rstrip().upper()
	print(line)
