
# Dictionary in Python

# A dictionary is an unordered collection of key-value pairs, where each key is unique.

# Creating a dictionary

bhel = dict(type="snack", price=30, taste="spicy")

# print(f"bhel: {bhel}")

# Another way to create a dictionary is by using curly braces {}

snack_recipe = {}

# Adding key-value pairs to the dictionary

snack_recipe["name"] = "Bhel"
snack_recipe["base"] = "puffed rice"
snack_recipe["ingredients"] = ["onions", "tomatoes", "coriander", "lemon juice", "spices"]
snack_recipe["liquid"] = ["tamarind chutney", "green chutney"]

# print(f"Snack recipe: {snack_recipe}")

# Accessing values in a dictionary

# print(f"Snack recipe: {snack_recipe['name']}")

# Modifying values in a dictionary

snack_recipe["ingredients"] = snack_recipe["ingredients"] + ["raw mango"]

# print(f"Snack recipe: {snack_recipe}")

# Removing key-value pairs from a dictionary

del snack_recipe["liquid"]

# print(f"Snack recipe: {snack_recipe}")

# Memebership Testing in dictionary

# print(f"Is Liquid present in recipe: {"Liquid" in snack_recipe}")

# Dictionary methods

# print(f"Keys in snack_recipe : {snack_recipe.keys()}")
# print(f"Values in snack_recipe : {snack_recipe.values()}")
# print(f"Items in snack_recipe : {snack_recipe.items()}")

order_coffee = { "type": "Filtered", "price": 50, "taste": "sweet" }

last_item = order_coffee.popitem()

print(f"Popped Item: {last_item}")
print(f"Order: {order_coffee}")

more_information = { "size": "medium", "additional" : "cream", "sugar": 1}
order_coffee.update(more_information)

print(f"Order: {order_coffee}")

print(f"Order size: {order_coffee.get("size")}")

# Trying to access key values which are not available will return error or "None"
# You can also add additional values to return incase if the key value does not exist

print(f"Customer note: {order_coffee.get("customer_note", "No note")}")


