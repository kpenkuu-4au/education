some_numbers = [2, 4, 3, 5, 6, 8, 7, 9, 1]


def apply_all_func(int_list, *functions):
    result = {}
    for function in range(len(functions)):
        if map(functions[function], int_list):
            new_dict = {f'{functions[function].__name__}': functions[function](int_list)}
            result.update(new_dict)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func(some_numbers, len, sum, sorted))
