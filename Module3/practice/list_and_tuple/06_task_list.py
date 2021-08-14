first_number = int(input("Введите 1 число: "))
second_number = int(input("Введите 2 число: "))

for i in range(first_number, second_number + 1):
    if i % 3 == 0:
        print(i)
