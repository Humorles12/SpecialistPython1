item = {"name": "Кроссовки", "price": 7540.5, "currency": "rub", "count": 10}
dollar_rate = 74.12

price_s = item["price"] * item["count"] / dollar_rate
print(price_s)
