# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

for line in picture:
	array = []
	for item in line:
		if item == 0:
			array.append(' ')
		if item == 1:
			array.append('*')
	print(array)

for line in picture:
	for item in line:
		if item == 0:
			print(' ', end='')
		if item == 1:
			print('*', end='')
	print('')

# Exercise: Check for duplicates in a list
some_list = ['a', 'b', 'c', 'd', 'a', 'x', 'y', 'z', 'x']
dict = {}
new_list = []

for item in some_list:
	dict[item] = dict.get(item, 0) + 1

for key, value in dict.items():
	if value > 1:
		new_list.append(key)

print(new_list)

# Exercise: Highest even number in a list
def highest_even(li):
	highest = 0
	for number in li:
		if number % 2 == 0:
			if number > highest:
				highest = number
	return highest
