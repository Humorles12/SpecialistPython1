names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
maximum = ""
for i in names:
    if len(maximum) < len(i):
        maximum = i
print(maximum)
