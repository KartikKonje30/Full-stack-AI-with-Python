
# Assignment is a statement for ex. a = 12
# Expression is something that returns a value ex. 3 + 3 -> 6

# walrus operator (:=) that assigns values to variables as part of larger expression.

# Example 1 ->

value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")

# Example 2 ->

# size = ["small", "medium", "large"]

# if (requested_size := input("Enter valid cup size: ")) in size:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Cup size not found! = {requested_size}")


# Example 3 ->

flavours = ["chocolate", "vanilla", "pista"]

while (requested_flavour := input("Enter your choice: ")) not in flavours:
    print(f"Sorry {requested_flavour} not available")

print(f"You Choose {requested_flavour} Icecream!")
