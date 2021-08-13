n = int(input("Длинна стороны квадрата равна: "))
i = 1

print("#" * n)
while (i + 2) <= n:
    print("#", " " * (n - 2), "#", sep="")
    i += 1
print("#" * n)
