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
