
# Strings in Python

# Strings are sequences of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

# Example of string literals
single_quote_string = 'Hello, World!'

user = 'Alice'
quote_string = "Python"

print(f'Welcome {user} to the world of {quote_string}!')

# Strings are immutable, meaning once created, they cannot be changed.
# However, you can create new strings based on existing ones.
greeting = "Hello"
new_greeting = greeting + ", " + user + "!"
print(new_greeting)

# String are sequences, so you can access individual characters using indexing.
first_char = single_quote_string[0]
print(f'First character from the string: {first_char}')

# similarly you can access the last character using negative indexing
last_char = single_quote_string[-1]
print(f"Last character from the string: {last_char}")

# You can also use slicing to get substrings.
substring = single_quote_string[0:5]  # Get characters from index 0 to 4
print(f'Substring (0 to 4): {substring}')

# similarly you can also perform same
substring = single_quote_string[:5]  # without using starting index
print(f'Substring: {substring}')

substring = single_quote_string[7:]  # without using ending index
print(f'Substring: {substring}')

# Understanding how string can be sliced
# String['Start Index' : 'End Index' : 'Step']
# step means how many characters to skip

substring = single_quote_string[::2]
print(f'Substring with step 2: {substring}')  # Hlo ol!

# Here we are skipping every second character.

# You can also reverse a string using slicing
reversed_string = single_quote_string[::-1]
print(f'Reversed String: {reversed_string}')  # !dlroW ,olleH

# People often use this technique to reverse strings in Python.


# String Encoding
# Strings in Python are represented using Unicode, which allows for a wide range of characters from different languages and symbol sets.
# You can encode a string to bytes using the encode() method and decode bytes back to a string using the decode() method.

original_string = "Hello, 世界"  # Contains both English and Chinese characters
print(f'Original String: {original_string}')
encoded_string = original_string.encode('utf-8')
print(f'Encoded String (bytes): {encoded_string}')
decoded_string = encoded_string.decode('utf-8')
print(f'Decoded String: {decoded_string}')


