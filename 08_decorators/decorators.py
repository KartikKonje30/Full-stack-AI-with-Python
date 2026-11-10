from functools import wraps

# Decorators are a way to modify or enhance the behavior of functions or methods in Python. 
# They allow you to wrap a function with another function, which can add functionality before or after the original function is called.

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()  # This will call the wrapper function, which in turn calls say_hello() and adds additional behavior before and after it.
print(say_hello.__name__)