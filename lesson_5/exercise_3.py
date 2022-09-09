price = int(input("Input a price: "))
price_symbol = "\U000020AC" + str(price)
print(price_symbol)

if price < 50000:
    print("\U0001F602")
else:
    print("\U0001F929")
