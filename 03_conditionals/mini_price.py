
cup_size = input("Please enter the cup size (small/medium/large): ").lower()

if cup_size == "small":
    print(f"{cup_size.upper()} size costs ₹10")
elif cup_size == "medium":
    print(f"{cup_size.upper()} size costs ₹15")
elif cup_size == "large":
    print(f"{cup_size.upper()} size costs ₹20")
else:
    print(f"Entered size is invalid!")

    