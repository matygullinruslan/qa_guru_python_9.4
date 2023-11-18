import random


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = " Анна"
    age = 25
    years = " лет"
    output = "Привет," + name + "!" " Тебе " + str(age) + years + "."
    print(output)
    "# Проверяем результат"
    assert output == "Привет, Анна! Тебе 25 лет."


import math


def test_rectangle():
    """
#     Напишите программу, которая берет длину и ширину прямоугольника
#     и считает его периметр и площадь.
#     """
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = (a + b) * 2
    assert perimeter == 60


    # TODO сосчитайте площадь
    area = a * b
    assert area == 200


def test_circle():
    """
 Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
 Используйте константу PI
 """

r = 23

# TODO сосчитайте площадь
area = r**2*math.pi
print(area)
assert area == 1661.9025137490005

# TODO сосчитайте длину окружности
length = 2*math.pi*r
print(length)
assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """
from random import randint
import math

# TODO создайте список

l = (random.sample(range(1, 101), 10))
l.sort()
assert len(l) == 10
assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """


l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
# TODO удалите повторяющиеся элементы
l=list(set(l))
assert isinstance(l, list)
assert len(l) == 10
assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    # TODO создайте словарь

    d = dict(zip(first, second))
    print(d.values())

    assert isinstance(d, dict)
    assert len(d) == 5
