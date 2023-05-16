# Trimming a string 7kyu
def trim(phrase, size):
	if size <= 3 and len(phrase) != 3:
		return phrase[:size] + '...'
	elif size >= len(phrase):
		return phrase
	elif size < len(phrase):
		return phrase[:size - 3] + '...' 

# Vowel one 7kyu
def vowel_one(s):
    new_string = ''
    for letter in s.lower():
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            new_string += '1'
        else:
            new_string += '0'
    return new_string

# Band name generator 7kyu
def band_name_generator(name):
    if len(name) == 1:
        return name.upper()
    elif name[0] == name[-1]:
        return name[0].upper() + name[1:-1] + name
    else:
        return 'The ' + name[0].upper() + name[1:]

# Greet Me 7kyu
def greet(name): 
    return 'Hello ' + name.capitalize() + '!'

# The Feast of Many Beasts 8kyu
def feast(beast, dish):
	if beast[0] == dish[0] and beast[len(beast) - 1] == dish[len(dish) - 1]:
		return True
	else:
		return False

# Compare 2 digit numbers 7kyu
def compare(a, b):
	percent = 0
	first_number_digits = list(str(a))
	second_number_digits = list(str(b))

	if first_number_digits[0] == first_number_digits[1]:
		if first_number_digits[0] == second_number_digits[0]:
			percent += 50
		if first_number_digits[0] == second_number_digits[1]:
			percent += 50
	if first_number_digits[0] != first_number_digits[1]:
		if first_number_digits[0] == second_number_digits[0] or first_number_digits[0] == second_number_digits[1]:
			percent += 50
		if first_number_digits[1] == second_number_digits[0] or first_number_digits[1] == second_number_digits[1]:
			percent += 50

	return f'{percent}%'

# Find the stray number 7kyu
def stray(arr):
	for num in arr:
		if arr.count(num) == 1:
			return num

# Divide and Conquer 7kyu
def div_con(x):
    sum = 0
    for char in x:
    	if type(char) == int:
    		sum += char
    	else:
    		sum -= int(char)
    return sum

# Summing a number's digits 7kyu
def sum_digits(number):
    string = str(number)
    array = []    
    for digit in string:
        if digit.isnumeric():
            array.append(int(digit))
    sum_of_digits = sum(array)
    return sum_of_digits

# Sum even numbers 7kyu
def sum_even_numbers(seq): 
	sum = 0
	for num in seq:
		if num % 2 == 0:
			sum += num
	return sum

# Fix My Phone Numbers! 7kyu
def is_it_a_num(str):
	numbers = []
	for char in str:
		if char.isnumeric():
			numbers.append(char)
	if len(numbers) == 11 and numbers[0] == '0':
		numbers = ''.join(numbers)
		return numbers
	else:
		return 'Not a phone number'

# Speed Limit 7kyu
def speed_limit(speed, signals):
    sum = 0
    for signal in signals:
        if speed - signal >= 30:
	    sum += 500
	elif speed - signal >= 20:
	    sum += 250
	elif speed - signal >= 10:
	    sum += 100
    return sum

# Between Extremes 7kyu
def between_extremes(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    return max_value - min_value

# Find the index of the second occurrence of a letter in a string 7kyu
def second_symbol(s, symbol):
    first = s.find(symbol)
    second = s.find(symbol, first + 1)
    return second

# The Office I - Outed 7kyu
def outed(meet, boss):
	score = 0
	members = 0
	for k, v in meet.items():
		members += 1
		if k == boss:
			score += v * 2
		else:
			score += v
	average = score / members

	if average <= 5:
		return 'Get Out Now!'
	else:
		return 'Nice Work Champ!'

# Sum a list but ignore any duplicates 7kyu
def sum_no_duplicates(l):
	sum = 0
	dictionary = {}

	for number in l:
		dictionary[number] = dictionary.get(number, 0) + 1

	for key, value in dictionary.items():
		if value == 1:
			sum += key

	return sum

# Alphabet war 7kyu
def alphabet_war(fight):
	left_side = 0
	right_side = 0
	for letter in fight:
		if letter == 'w':
			left_side += 4
		if letter == 'p':
			left_side += 3
		if letter == 'b':
			left_side += 2
		if letter == 's':
			left_side += 1
		if letter == 'm':
			right_side += 4
		if letter == 'q':
			right_side += 3
		if letter == 'd':
			right_side += 2
		if letter == 'z':
			right_side += 1
	if left_side > right_side:
		return 'Left side wins!'
	elif left_side < right_side:
		return 'Right side wins!'
	else:
		return 'Let\'s fight again!'
 
