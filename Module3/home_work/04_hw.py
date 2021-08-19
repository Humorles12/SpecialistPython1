numbers = [2, -5, 8, 9, -25, 25, 4]
num_square = []
i = 0

while i < len(numbers):
    if numbers[i] > 0:
        a = float(numbers[i] ** (1 / 2))
        true_false = (a).is_integer()
        if true_false == True:
            num_square.append(int(a))
        i += 1
    else:
        i += 1
print(num_square)
