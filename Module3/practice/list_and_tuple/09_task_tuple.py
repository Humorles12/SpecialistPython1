fruits = ["яблоко", "банан", "киви", "арбуз"]
count = 1

for fruit in fruits:
    print(count, "- ", fruit.rjust(6, " "), sep="")
    count += 1
