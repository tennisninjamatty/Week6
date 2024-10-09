def product_of_numbers(some_list: list[int]) -> int:
    if len(some_list) == 1 or len(some_list) == 0:
        return some_list[0]
    else:
        return some_list[0] * product_of_numbers(some_list[1:])

print(product_of_numbers([10, 12, 2]))