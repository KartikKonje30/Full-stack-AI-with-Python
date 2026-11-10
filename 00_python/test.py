
# Test runs for practice

def infinite_call():
    count = 1
    while True:
        yield count
        count += 1

refill = infinite_call()

for _ in range(3):
    print(next(refill))

