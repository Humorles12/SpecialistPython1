year = int(input("Год: "))

if year % 400 == 0 or (year % 4 == 0 and year != 100):
    print("Високосный")
else:
    print("Не високосный")
