"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №8.3
Домашнее задание по теме "Создание исключений"
"""


# Автомобили
class Car:

    # Инициализация автомобиля с (модель, vin-номер, гос-номер)
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin): # Передача значения внутреннему методу на валидацию
            self.__vin = vin
        if self.__is_valid_numbers(numbers): # Передача значения внутреннему методу на валидацию
            self.__numbers = numbers

    # Валидация vin-номера на целочисленность и диапазон
    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    # Валидация гос-номера на строковость и длину
    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


# Исключения по vin-номеру автомобиля
class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message


# Исключения по гос-номеру автомобиля
class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message


    # Запуск
if __name__ == '__main__':

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