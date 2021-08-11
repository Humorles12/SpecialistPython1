x = float(input("Стоимость товара: "))
i = 1
k = 0

while i <= 20:
    print(i, "ед. товара стоит - ", x + k, "Rub.")
    i += 1
    k = x + k
