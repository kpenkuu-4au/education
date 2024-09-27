my_dict = {'Ivan': '09.09.1999', 'Maria': '07.07.2007', 'Michael': '03.02.2001'}
print(my_dict)
print(my_dict['Maria'])
print(my_dict.get('Igor'))
my_dict.update({'Alex': '02.02.2002', 'Egor': '05.05.2005'})
Michael = my_dict.pop('Michael')
print(Michael)
print(my_dict)
my_set = {True, 'False', 4, 0.7, 0.7, 4, 'False', True}
print(my_set)
my_set.update((False, 'True'))
my_set.discard(4)
print(my_set)
