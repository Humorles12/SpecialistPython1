n = int(input("Введите длинну шоколадки: "))
m = int(input("Введите ширину шоколадки: "))
k = int(input("Введите кол-во долек которые хотите отломить: "))

if ((k % n == 0) or (k % m == 0)) and (k < n * m):
    print("Yes")
else:
    print("No")
