"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №8.1
Домашнее задание по теме "Try и Except"
"""


def add_everything_up(a, b):
    try:
        return a + b

    except TypeError:
        return str(a) + str(b)


# Запуск
if __name__ == '__main__':

    print(add_everything_up(123.456, 'строка')) # 123.456строка
    print(add_everything_up('яблоко', 4215)) # яблоко4215
    print(add_everything_up(123.456, 7)) #130.45600000000002