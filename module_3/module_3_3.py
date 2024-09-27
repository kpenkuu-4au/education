def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(a=False, b=(4, 7), c=36.6)
print_params(b=25, c=[1, 2, 3])


values_list = [333.333, True, 'Sun']
values_list_2 = ['red', 13]
values_dict = {'a': 'Brown', 'b': 100, 'c': False}


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)