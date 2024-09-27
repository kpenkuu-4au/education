calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    s1 = len(string)
    s2 = string.upper()
    s3 = string.lower()
    return s1, s2, s3


def is_contains(string, list_to_search):
    count_calls()
    t1 = string.upper()
    t2 = ', '.join(list_to_search)
    t3 = t2.upper()
    if t1 in t3:
        return True
    else:
        return False

print(string_info('шоколад'))
print(string_info('конфета'))
print(string_info('мороженое'))
print(is_contains('пЕчеНьЕ', ['Вафля', 'Печенье', 'Кекс']))
print(is_contains('ЧереШНЯ', ['АПЕЛЬСИН', 'ЯБЛОКО', 'БАНАН']))
