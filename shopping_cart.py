# SHOPPING CART PROGRAM

name = input("Customer name: ")

product1 = input("Product 1: ")
price1 = float(input("Price: "))
print()
product2 = input("Product 2: ")
price2 = float(input("Price: "))
print()
product3 = input("Product 3: ")
price3 = float(input("Price: "))
print()

subtotal = price1 + price2 + price3



def discount(data):
  if data >= 5000:
    return 20
  elif data >= 3000 and data <= 4999:
    return 10
  elif data >= 1000 and data <= 2999:
    return 5
  elif data < 1000:
    return 0

discount_rate = discount(subtotal)

product_discount = subtotal * (discount_rate / 100)

final_total = subtotal - product_discount

print(f"Subtotal: {subtotal}")
print(f"Discount: {product_discount}")
print(f"Final Total: {final_total}")