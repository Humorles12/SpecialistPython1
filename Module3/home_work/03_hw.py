import random

n = int(input("Введите кол-во чисел: "))
numbers = []
i = 0
s = 0

while i < n:
    numbers.insert(i, random.randint(-100, 100))
    if numbers[i] % 2 == 0 and numbers[i] > 0:
        s = s + numbers[i]
    i += 1
print(numbers)
print(s)
