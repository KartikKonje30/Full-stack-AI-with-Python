
# Set & Frozenset in Python

# A set is an unordered collection of unique elements, 
# while a frozenset is an immutable version of a set.

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(f"My Set: {my_set}")

# Creating a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(f"My Frozenset: {my_frozenset}")

# Adding elements to a set
my_set.add(6)
print(f"After adding 6 to my_set: {my_set}")

# Removing elements from a set
my_set.remove(3)
print(f"After removing 3 from my_set: {my_set}")

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Union of set_a and set_b: {set_a | set_b}")
print(f"Intersection of set_a and set_b: {set_a & set_b}")
print(f"Difference of set_a and set_b: {set_a - set_b}")
print(f"Symmetric difference of set_a and set_b: {set_a ^ set_b}")

# Frozensets are immutable, so we cannot add or remove elements from them
# However, we can perform set operations on frozensets
frozenset_a = frozenset([1, 2, 3])
frozenset_b = frozenset([3, 4, 5])
print(f"Union of frozenset_a and frozenset_b: {frozenset_a | frozenset_b}")
print(f"Intersection of frozenset_a and frozenset_b: {frozenset_a & frozenset_b}")
print(f"Difference of frozenset_a and frozenset_b: {frozenset_a - frozenset_b}")
print(f"Symmetric difference of frozenset_a and frozenset_b: {frozenset_a ^ frozenset_b}")


