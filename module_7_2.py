def custom_write(file_name, strings):
    test_txt = open(file_name, 'w+', encoding='utf-8')
    for elem in range(len(strings)):
        if isinstance(strings[elem], str):
            print({(strings.index(strings[elem]) + 1, test_txt.tell()): strings[elem]})
            test_txt.write(f'{strings[elem]}\n')
    test_txt.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

custom_write('test.txt', info)
