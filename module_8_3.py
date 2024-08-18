class IncorrectVinNumber(Exception):
    def __init__(self, vin_number, message):
        self.vin_number = vin_number
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, numbers, message):
        self.numbers = numbers
        self.message = message


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = str(model)
        self.__vin = int(__vin)
        self.__numbers = str(__numbers)
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_number):
        if 999999 < vin_number < 10000000:
            self.__vin = vin_number
            return True
        elif not isinstance(vin_number, int):
            raise IncorrectVinNumber(vin_number, 'Некорректный тип vin номер')
        else:
            raise IncorrectVinNumber(vin_number, 'Неверный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):
        if 5 < len(numbers) < 7:
            self.__numbers = numbers
            return True
        elif not isinstance(numbers, str):
            raise IncorrectCarNumbers(numbers, 'Некорректный тип данных для номеров')
        else:
            raise IncorrectCarNumbers(numbers, 'Неверная длина номера')


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
