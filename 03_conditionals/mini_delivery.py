
order_amount = int(input("Please enter the amount: "))

delivery_fees = "Free Delivery" if order_amount > 300 else "Delivery Charges: 30"

print(f"Order Amount: {order_amount} + {delivery_fees} ")