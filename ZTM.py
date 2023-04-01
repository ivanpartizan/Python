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

# Exercise: Cats Everywhere
# Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Whiskers', 5)
cat2 = Cat('Smudge', 3)
cat3 = Cat('Fluffy', 7)


# 2 Create a function that finds the oldest cat
def oldest(*args):
  oldest = 0
  for age in args:   
    if age > oldest:
      oldest = age
  return oldest
  

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old.')

# Exercises: map, filter, zip, reduce
from functools import reduce

# 1 Capitalize all of the pet names and print the list
def capitalize(item):
	return item.capitalize()
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
def over50(score):
	return score > 50
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(over50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
joined = scores + my_numbers
def accumulator(acc, item):
	return acc + item
print(reduce(accumulator, joined))
