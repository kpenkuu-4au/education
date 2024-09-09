from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for item in range(word_count):
            record_words = f'Some word №{range(word_count)[item] + 1}\n'
            file.write(record_words)
            sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')


time_start_functions = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end_functions = datetime.now()
print(time_end_functions - time_start_functions)

time_start_threads = datetime.now()
thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
time_end_threads = datetime.now()
print(time_end_threads - time_start_threads)
