
# Tuples in python

# Tuples are similar to lists but are immutable (cannot be changed after creation)

# Creating a tuple
my_tuple = (1 , 2, 3, 4, 5)

# Example of a tuple 

masala_spice = ("cardamom", "cinnamon", "clove")

# can be unpacked into variables
spice1, spice2, spice3 = masala_spice 

print(f"Masala spices are: {spice1}, {spice2}, {spice3}")

# Exchanging values using tuples

ginger_ratio, turmeric_ratio = 2, 1

print(f"Before swapping: Ginger ratio = {ginger_ratio}, Turmeric ratio = {turmeric_ratio}")

# Swapping values
ginger_ratio, turmeric_ratio = turmeric_ratio, ginger_ratio

print(f"After swapping: Ginger ratio = {ginger_ratio}, Turmeric ratio = {turmeric_ratio}")

# Python smartly handles exchanging of values because of tuples working behind the scenes.

# Membership testing in tuples

print(f"Is ginger present in masala spices? {'ginger' in masala_spice}")
print(f"Is cinnamon present in masala spices? {'cinnamon' in masala_spice}")

# Note: Tuples check membership wrt values and are case-sensitive.
print(f"Is Cinnamon present in masala spices? {'Cinnamon' in masala_spice}")
