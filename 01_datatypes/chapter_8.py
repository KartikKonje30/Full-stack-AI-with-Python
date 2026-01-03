
# Lists in Python

# Lists are mutable sequences, typically used to store collections of homogeneous items.
# Lists are exactly like arrays in other programming languages but can hold items of different data types.

# Creating a list

chai_ingredients = ["water", "milk", "tea leaves", "sugar", "spices"]
print(f"Chai Ingredients: {chai_ingredients}")

# Accessing elements in a list
first_ingredient = chai_ingredients[0]
print(f"First ingredient in chai: {first_ingredient}")

# Combining lists
additional_ingredients = ["ginger", "cardamom"]
all_ingredients = chai_ingredients.extend(additional_ingredients)
print(f"All Chai Ingredients after adding more: {chai_ingredients}")

# Modifying elements in a list
chai_ingredients[3] = "honey"  # Replacing sugar with honey
print(f"Chai Ingredients after modification 3rd element: {chai_ingredients}")

# Removing elements from a list
chai_ingredients.remove("tea leaves")
print(f"Chai Ingredients after removing tea leaves: {chai_ingredients}")

# Inserting elements in a list
chai_ingredients.insert(2, "black tea leaves")
print(f"Chai Ingredients after inserting black tea leaves at 2nd Index: {chai_ingredients}")

# Popping elements from a list
popped_ingredient = chai_ingredients.pop()  # Removes the last item
print(f"Popped ingredient: {popped_ingredient}")
print(f"Chai Ingredients after popping last element: {chai_ingredients}")

# Reversing a list
chai_ingredients.reverse()
print(f"Chai Ingredients after reversing: {chai_ingredients}")

# Sorting a list
chai_ingredients.sort()
print(f"Chai Ingredients after sorting: {chai_ingredients}")

# Maximum and Minimum in a list
numbers = [5, 2, 9, 1, 5, 6]
print(f"Maximum number in the list: {max(numbers)}")
print(f"Minimum number in the list: {min(numbers)}")

