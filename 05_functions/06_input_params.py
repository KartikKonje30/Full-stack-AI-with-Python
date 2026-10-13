
# Paramaters can be passed as arguments and the funtion only reads the value.

# chai_Option = "Masala"

# def print_order(type):
#     print(f"Chai : {type}")

# print_order(chai_Option)
# print(f"Chai : {chai_Option}")

# But what if we passsed an list as an argument and run it twice

# Option = [1, 2, 3]

# def print_order(args):
#     args[1] = 30
#     print(f"Updated List : {args}")

# print_order(Option)

# notice as list are mutable in nature so it can be appended

# Lets see what are args & kwargs

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Ginger", "No", "Yes") # Positional 
make_chai(tea="Tulsi", milk="Yes", sugar="Yes") # Keywords 


def special_chai(*ingredients, **extras):
    print(ingredients)
    print(extras)

special_chai("Cinnamon", 'Cardamom', Milk="Low fat" ,foam="No") # Coombination of both positional & keywords

# Default traps 

# Lets say you create a function & pass an empty argument and accidentally run it twice


# def print_order(type=[]):
#     type.append("Masala")
#     print(f"Chai : {type}")

# print_order()
# print_order()

# Notice how it will keep on updating the same array as much times the funtion executes

# To handle this always define the arguments as type None and type check to avoid such default traps

def print_order(type=None):
    if type is None:
        type=[]
    else:
        type.append("Masala")
    print(f"Chai : {type}")

print_order()
print_order(["Ginger"])

