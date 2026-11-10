

# Generators are a special type of iterator in Python that allow you to iterate over a sequence of values without storing the entire sequence in memory. 
# They are defined using functions and the `yield` statement. 
# When a generator function is called, it returns a generator object, which can be iterated over using a loop or the `next()` function.

# why generators are useful:
# 1. Memory Efficiency: Generators produce items one at a time and only when requested, which is useful for large datasets or streams of data.
# 2. Lazy Evaluation: Generators allow for lazy evaluation, meaning that values are computed only when needed, which can improve performance and reduce memory usage.

# example -

def infinite_call():
    count = 1
    while True:
        yield count
        count += 1

refill = infinite_call()

for _ in range(3):
    print(next(refill))

# Yield statement is used to produce a value from the generator function and pause its execution, allowing it to be resumed later.
# next() function is used to retrieve the next value from the generator. When the generator is exhausted, it raises a StopIteration exception.
# send() method is used to send a value to the generator function, which can be used to modify its behavior or state. It can also be used to resume the generator's execution after it has been paused by a yield statement.
# yield from statement is used to delegate part of a generator's operations to another generator. It allows for more complex generator compositions and can simplify code by avoiding nested loops.
# close() method is used to terminate a generator function and release any resources it may be holding. It raises a GeneratorExit exception inside the generator, which can be caught to perform cleanup operations.

def chai_order():
    print("What type of chai would you like?")
    order = yield
    while True:
        print(f"Preparing your {order} chai...")
        order = yield

stall = chai_order()
next(stall)  # Start the generator and reach the first yield statement

stall.send("Masala")  # Send the order to the generator 
stall.send("Green")


def tea_collection():
    yield "Green Tea"
    yield "Black Tea"

def coffee_collection():
    yield "Espresso"
    yield "Latte"

def beverage_collection():
    yield from tea_collection()  # Delegate to tea_collection generator
    yield from coffee_collection()  # Delegate to coffee_collection generator

for beverage in beverage_collection():
    print(beverage)


try:
    stall.close()  # Close the generator
except GeneratorExit:
    print("Generator closed. Cleaning up resources...")
    