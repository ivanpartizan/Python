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

# 07 Lists

# Find all unique words in a file 
# Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce the list of all the words that Shakespeare used? Would you download all his work, read it and track all unique words by hand? Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
file = input('Enter file: ')
text = open(file)

unique_words = list()

for line in text:
	words = line.split()
	# print(words)
	for word in words:
		if word in unique_words:
			continue
		else:
			unique_words.append(word)

print(sorted(unique_words))

# MBOX (mail box) is a popular file format to store and share a collection of emails. This was used by early email servers and desktop apps. Without getting into too many details, MBOX is a text file, which stores emails consecutively. Emails are separated by a special line which starts with From (notice the space). Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.
file = input('Enter a file name: ')
text = open(file)

count = 0

for line in text:
	if line.startswith('From '):
		# print(line)
		words = line.split()
		print(words[1])
		count = count + 1

print('There were', count, 'lines in the file with From as the first word')

# 08 Dictionaries

# Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
file = input('Enter a file name: ')
handle = open(file)

counts = {}
days = list()

for line in handle:
	if not line.startswith('From'): 
		continue
	else:
		words = line.split()
		if len(words) > 2:
			days.append(words[2])

for day in days:
	counts[day] = counts.get(day, 0) + 1

print(days)
print(counts)

# 09 Tuples

# Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
file = input('Enter a file name: ')
handle = open(file)

dict = {}
emails = list()

for line in handle:
	if line.startswith('From '):
		words = line.split()

		if len(words) > 2:
			emails.append(words[1])

print(emails)

for email in emails:
	dict[email] = dict.get(email, 0) + 1

print(dict)

list = list()

for k, v in dict.items():
	tuple = (v, k)
	list.append(tuple)

list = sorted(list, reverse=True)
print(list)

for k, v in list[:1]:
	print(v, k)
