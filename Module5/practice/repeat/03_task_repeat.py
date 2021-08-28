def palindrome(number):
    return str(number) == str(number)[::-1]


a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))
i = 0

while a <= b:
    if palindrome(a):
        i += 1
        a += 1
    else:
        a += 1
print("Кол-во палиндромов:", i)
