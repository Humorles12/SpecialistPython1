def distance(x1, y1, x2, y2):
    formula = (x2 - x1) ** 2 + (y2 - y1) ** 2
    distance = formula ** 0.5
    return distance

print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
