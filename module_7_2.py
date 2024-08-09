def custom_write(file_name, strings):
    for elem in range(len(strings)):
        test_txt = open(file_name, 'a', encoding='utf-8')
        if isinstance(strings[elem], str):
            test_txt.write(f'{strings[elem]}\n')
            value = {(strings.index(strings[elem]) + 1, test_txt.tell()): strings[elem]}
            print(value)
        test_txt.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

custom_write('test.txt', info)
