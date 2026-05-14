
names = ["Kartik", "Hitesh", "Nikhil", "Sumedh", "yash"]

bills = [50, 70, 80, 50, 100]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} Rupees")


