def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def can_triangle(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p1, *p3)
    c = distance(*p2, *p3)
    if a + b > c and a + c > b and b + c > a:
        p = a + b + c
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s
    else:
        return "Такого треугольника не существует."


print(can_triangle((10, 12), (14, 12), (12, 12)))
