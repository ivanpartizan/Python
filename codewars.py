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
