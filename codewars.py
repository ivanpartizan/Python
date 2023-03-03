# Trimming a string 7kyu
def trim(phrase, size):
	if size <= 3 and len(phrase) != 3:
		return phrase[:size] + '...'
	if size >= len(phrase):
		return phrase
	elif size < len(phrase):
		return phrase[:size - 3] + '...' 
