
# How data is stored in Python

"""
In Python, data is stored in memory as objects. 

Each object has a type, value, and identity. 

Variables are simply references to these objects.

Objects can be of various data types, including:
- Integers (int)    
- Floating-point numbers (float)
- Strings (str)     
- Booleans (bool)
- Lists (list)
- Tuples (tuple)
- Dictionaries (dict)
- Sets (set)
Each data type has its own characteristics and methods for manipulation.

For example:
# Integer
x = 10                              # 'x' references an integer object with value 10
# Floating-point number
y = 3.14                            # 'y' references a float object with value 3.14
# String
name = "Alice"                      # 'name' references a string object with value "Alice"
# Boolean
is_active = True                    # 'is_active' references a boolean object with value True
# List
numbers = [1, 2, 3]                 # 'numbers' references a list object
# Tuple
coordinates = (10, 20)              # 'coordinates' references a tuple object
# Dictionary
person = {"name": "Bob", "age": 25} # 'person' references a dictionary object
# Set
unique_numbers = {1, 2, 3}          # 'unique_numbers' references a set object

Objects are stored in memory, and Python uses a system of reference counting and garbage collection to manage memory efficiently.
Objects that are no longer referenced by any variable are automatically cleaned up by Python's garbage collector.
Overall, understanding how data is stored in Python helps in writing efficient and effective code.

Objects in Python are mutable or immutable:
- Mutable objects (like lists and dictionaries) can be changed after they are created.
- Immutable objects (like strings and tuples) cannot be changed after they are created.

We should always decide whether the object is mutable or immutable based on the identity of the object and not the value it holds.

Given below is an example to illustrate this concept:

"""

# Immutable object example
addSugar = 2;
print(f"Initial sugar amount: {addSugar}, id: {id(addSugar)}");
addSugar = 12;
print(f"Updated sugar amount: {addSugar}, id: {id(addSugar)}");

# Output:
# Initial sugar amount: 2, id: 140718252455064
# Updated sugar amount: 12, id: 140718252455384

# In the above example, the integer object is immutable.
# When we change the value of 'addSugar', a new integer object is created in memory,
# and 'addSugar' now references this new object. 
# The id() function shows that the identity of the object has changed.


# Mutable object example
spice_mix = set()
print(f"Initial spice mix: {spice_mix}, id: {id(spice_mix)}")
spice_mix.add("salt")
spice_mix.add("chili powder")
print(f"Initial spice mix: {spice_mix}, id: {id(spice_mix)}")

# Output:
# Initial spice mix: set(), id: 1849949997536
# Initial spice mix: {'salt', 'chili powder'}, id: 1849949997536
# In the above example, the set object is mutable.
# When we add elements to 'spice_mix', the same object in memory is modified.
# The id() function shows that the identity of the object remains the same.
# Understanding the mutability of objects is crucial for effective memory management and avoiding unintended side effects in code.

