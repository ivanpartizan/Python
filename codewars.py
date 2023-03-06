# Trimming a string 7kyu
def trim(phrase, size):
	if size <= 3 and len(phrase) != 3:
		return phrase[:size] + '...'
	if size >= len(phrase):
		return phrase
	elif size < len(phrase):
		return phrase[:size - 3] + '...' 

# Vowel one 7kyu
def vowel_one(s):
    new_string = ''
    for letter in s:
        if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U':
            new_string += '1'
        else:
            new_string += '0'
    return new_string
