import random

n = int(input("Введите кол-во чисел: "))
numbers = []
i = 0

while i < n:
    numbers.insert(i, random.randint(-100, 100))
    i += 1
print(numbers)
