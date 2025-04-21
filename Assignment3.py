# Question 1 
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
print(calculate_discount(100, 30))
print(calculate_discount(200,19))

# Question 2

try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage:"))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"discount applied. final price: R{final_price:.2f}")
    else:
        print(f"No discount applied. price remains: R{final_price:.2f}")
except ValueError:
        print("please enter valid number for price and discount.")