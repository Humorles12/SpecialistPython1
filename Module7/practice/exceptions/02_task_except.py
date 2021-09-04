import calendar


while True:
    time = input("Введите месяц и год: ")
    time = time.split(" ")
    try:
        print("Кол-во дней:", calendar.monthrange(int(time[1]), int(time[0]))[1])
        break
    except (ValueError, IndexError):
        print("Введены не верные данные.")
    except Exception as e:
        print(f'Что-то пошло не так {e}')
