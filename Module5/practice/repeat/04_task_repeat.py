import math


def pagination(num_items, items_on_page):
    quantity = num_items / items_on_page
    return math.ceil(quantity)


print(pagination(76, 5))
