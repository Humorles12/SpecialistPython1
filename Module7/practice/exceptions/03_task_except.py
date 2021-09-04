while True:
    maxim = 0
    i = 0
    numbers = []
    number = input("Введите числа: ")
    number = number.split(' ')
    try:
        while i <= 4:
            numbers.append(number[i])
            i += 1
        for i in numbers:
            i = int(i)
            if i > 0:
                if maxim < i:
                    maxim = i
        break
    except (ValueError, IndexError):
        print("Введены не верные данные.")
    except Exception as e:
        print(f'Что-то пошло не так {e}')
print(maxim)
