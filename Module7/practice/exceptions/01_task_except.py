while True:
    try:
        s = str(input('Введите размер: '))

        s = s.split('x')
        count = int(s[0]) // int(s[1])
        break
    except:
        print("Что-то пошло не так...")
print(count)
