price = 600
years = range(4)
rate_change = 0.02

for i in years:
    print('Price in year',i,"is: $",price)
    price = (price*rate_change) + price
    price = round(price, 2)