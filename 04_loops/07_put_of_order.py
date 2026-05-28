
# continue statement skips to next iteration
# break statement exits the loop

flavours = ["Chocolate", "Vanilla", "Out of stock", "Discountinued", "Pista"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discountinued":
        print("Discountinued item found")
        break
    print(f"{flavour} flavour found!")

print("Outside the loop")