import math

# comprehension are concise way of creating lists, sets, dictionaries or generators in python using a single line of code.

# Real life Used in filter items, transform item, creating collection and flatten nested structure.

# What is the purpose of using them - cleaner code and fester execution.

# Types of comprehension
# - list
# - set
# - Dictionary
# - Generator

# 1. List 

# syntax - [expression for item in iterable if condition]

menu = [
    "Masala tea",
    "Iced Lemon tea",
    "Ginger tea",
    "Green tea",
    "Iced Peach tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

# print(iced_tea)


# 2. set 

# syntax - {expression for item in iterable if condition}

favourite_chai = [
    "Masala tea",
    "Iced Lemon tea",
    "Ginger tea",
    "Green tea",
    "Iced Peach tea",
    "Masala tea",
    "Green tea"
]

unique_chai = {chai for chai in favourite_chai}

# print(unique_chai)

# 3. dictionary 

# syntax - {expression for item in iterable if condition}

tea_prices_inr = {
    "Masala tea": 30,
    "Coffee": 30,
    "Lemon tea": 50
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}

# print(tea_prices_usd)


# 4 - Generators - memory saving stream

# syntax - (expression for item in iterable if condition)

daily_sales = [10, 20, 15, 12, 30, 16]

sales = sum(sale for sale in daily_sales if sale > 15)

print(sales)


