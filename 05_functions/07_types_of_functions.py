

# Types of Functions:

# Pure vs Impure
# Recursion 
# Lambdas (Anonymous)

# Pure Function - simply runs and returns

def pure_chai(chai):
    return chai * 10

total_chai = 0

# Impure Function - can manipulate on global scope and are not recommended

def pure_chai(chai):
    global total_chai
    total_chai += chai


# Recursive Function when function calls itself

def pour_chai(n):
    if n == 0:
        return "All cups poured"
    print(n)
    return pour_chai(n-1)

print(pour_chai(3))


# lambdas function - lambda function is a small, anonymous function that is defined without a name. While regular functions are defined using the def keyword, anonymous functions are defined using the lambda keyword.

# Suntax - lambda arguments: expression

chai = ["Masala", "Lemon", "Tulsi", "Lemon"]

chai_filter = list(filter(lambda opt: opt!="Lemon", chai))

print(chai_filter)