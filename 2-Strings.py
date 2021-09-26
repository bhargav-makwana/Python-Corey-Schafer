# Strings - Working with Textual Data

message = 'Hello World'
print(message)

new_message = 'Hello Bhargav'
print(new_message)

# Printing single quotes and double quotes
print("I'm learning Python!")
print('I\'m learning Python!')

# Multiline Comments
print("""\nCartoons made in the 1990s 
are my favourite.\n""")

# Accessing the index of the string
print(message[0])

# Index ranges (First index inclusive, last index exclusive)
print(message[0:5])
print(message[:5])
print(message[6:11])
print(message[6:])

# Functíons vs Methods. Methods belong to object of the class.

# Lower case, Upper case
print(message.lower())
print(message.upper())

# Counting characters in the string
print("There are " + str(message.count('l')) + " l's in the message.") # Typecasting : int > str

# Finding and replacing the words in the string
print(message.find('Worlds')) # Returns -1 if it didn't find the string
print(message.find('World'))  # Returns the index where the matching string starts
print(message.replace('World', 'Universe'))

# String concatenation
greeting = 'Hiii'
name = 'Bhargav'
print(greeting + " " + name)

# String Formatting
print('{}, {}! How are you?'.format(greeting, name))

#fstring (for Python 3.6+) (replacing placeholders with variable names)
print(f'{greeting}, {name.upper()}! How are you?')

# Information about variable methods and datatypes
print(dir(name))
print(help(str.replace))
