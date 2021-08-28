import random


def gen_list(size, of, to):
    i = 0
    while i <= size:
        numbers.append(random.randint(of, to))
        i += 1
    return numbers


numbers = []
l = int(input("Введие длинну: "))
n = int(input("Введите начальное число: "))
e = int(input("Введите конечное число: "))

gen_list(l, n, e)
print(numbers)
