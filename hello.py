# Ask user for their name
name = input("What's your name? ")
name = input("What's your name? ").strip().title()

print('hello, ' + name)
print('hello,', name)

print('hello, ', name, 'world', sep='---', end='???')
print(name)

# Remove whitespace from str
name = name.strip()

# Capitalize
name = name.capitalize()
name = name.title()

# Format strings
print(f"hello, {name}")
