def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    incorrect_elements = []
    try:
        for index in range(len(numbers)):
            if isinstance(numbers[index], int) or isinstance(numbers[index], float):
                result += numbers[index]
                continue
            elif not isinstance(numbers[index], int) or not isinstance(numbers[index], float):
                incorrect_data += 1
                if isinstance(numbers[index], str):
                    incorrect_elements.append(numbers[index])
    except TypeError:
        if not isinstance(numbers, list):
            print('В numbers записан некорректный тип данных')
    if result != 0 and incorrect_data == 0:
        return result, incorrect_data
    elif result != 0 and incorrect_data != 0 and incorrect_data != []:
        for element in range(len(incorrect_elements)):
            print(f'Некорректный тип данных для подсчёта суммы - {incorrect_elements[element]}')
            continue
        return result, incorrect_data
    elif isinstance(numbers, str):
        for item in range(len(numbers)):
            if isinstance(numbers[item], str):
                to_list = list(numbers[item])
                for symbol in range(len(to_list)):
                    print(f'Некорректный тип данных для подсчёта суммы - {to_list[symbol]}')
                    continue
        return result, incorrect_data


def calculate_average(numbers):
    summa = personal_sum(numbers)
    try:
        return summa[0] / (len(numbers) - summa[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
