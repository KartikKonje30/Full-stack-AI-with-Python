
# For else works if the loops does not break

candidates = [("Amit", 21), ("Yash", 24), ("Raj", 22)]

for name, score in candidates:
    if score > 24:
        print(f"{name} is selected!")
        break
else:
    print("Search continues.....")