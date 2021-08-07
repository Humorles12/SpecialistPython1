month = int(input("Месяц - "))

if 9 <= month <= 11:
    print("Осень")
elif 6 <= month <= 8:
    print("Лето")
elif 3 <= month <= 5:
    print("Весна")
elif month == 12 or month == 1 or month == 2:
    print("Зима")
