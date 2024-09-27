first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))
second_result = (True if len(first[i]) == len(second[i]) else False
                 for i in range(0, len(first), 3) for i in range(0, len(second), 1))
print(list(first_result))
print(list(second_result))
