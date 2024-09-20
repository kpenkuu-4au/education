from datetime import datetime as dt
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, "r") as text:
        while text.readline() != '':
            all_data.append(text.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]


# Линейный вариант

t1 = dt.now()
for file in filenames:
    read_info(file)
t2 = dt.now()
print(print(f'Линейный расчет: {t2 - t1}'))

# Мультипроцессорный вариант

# if __name__ == '__main__':
#     with Pool(processes=4) as mp:
#         t3 = dt.now()
#         mp.map(read_info, filenames)
#     t4 = dt.now()
#     print(f'Многопроцессорный расчет: {t4 - t3}')
