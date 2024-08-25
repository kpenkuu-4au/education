from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in range(len(data_set)):
                file.write(f'{data_set[data]}\n')

    return write_everything


first = 'Мама мыла раму'
second = 'Рамена мало было'

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

text_file = get_advanced_writer('example.txt')
text_file(first, second)
print(list(map(lambda x, y: x == y, first, second)))
