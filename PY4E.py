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
