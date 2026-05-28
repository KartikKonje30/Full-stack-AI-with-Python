
# Create your own dictionary for accessing predefinded values

users = [
    { "id": 1, "total": 500, "coupon": "50%OFF"},
    { "id": 2, "total": 350, "coupon": "FLAT50"},
    { "id": 3, "total": 1000, "coupon": "10%OFF"},
]

discounts = {
    "50%OFF": (0.5, 0),
    "FLAT50": (0, 50),
    "10%OFF": (0.1, 0),
}

for user in users:
    percent, flat = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + flat
    newtotal = user["total"] - int(discount)
    print(f"{user["id"]} total was {user['total']} but paid {newtotal} and got discount of rupees {int(discount)} using {user['coupon']}")