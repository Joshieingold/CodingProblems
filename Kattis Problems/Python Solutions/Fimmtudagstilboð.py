year = int(input())
price = 1000
if year <= 2020:
    print(price)

else:
    multiplier = year - 2020
    price += multiplier * 100
    print(price)