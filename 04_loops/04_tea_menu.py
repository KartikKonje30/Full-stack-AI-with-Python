
# enumerate() returns a tuple containing a count (from start which is default to 0) the values obtained from iterating over iterable.

menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} Tea")

