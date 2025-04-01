def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent/100)
    return price

price = float(input("Enter Original price"))
discount_percent = float(input("Enter Discount Price"))

final_price = calculate_discount(price, discount_percent)

if discount_percent >=20:
    print(f"New price: ${final_price:.2f}")
else:
    print(f"No discount allowed. Price remains: ${price:.2f}")