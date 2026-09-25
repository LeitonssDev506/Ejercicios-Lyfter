

price = int(input("Enter the price of the product: "))

first_discount = 0.10
second_discount = 0.02


if price >= 100:
    final_price = price * (1-first_discount)
    print(f"The discounted price is {final_price}")

else:
    final_price = price * (1-second_discount)
    print(f"The discounted price is {final_price}")


    