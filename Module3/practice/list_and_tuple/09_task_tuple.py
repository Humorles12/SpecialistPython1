a = (9, 15, 97, 3, 2, 86)
b = (9, 46, 97, 8, 2, 50)
c = (9, 39, 97, 187, 0, 86)
count = 0
i = 0

while i < len(c):
    if a[i] == b[i] or a[i] == c[i] or b[i] == c[i]:
        count += 1
    i += 1
print("Кол-во совпадений:", count)
