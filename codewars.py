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
