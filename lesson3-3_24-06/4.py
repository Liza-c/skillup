""" Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров. """

def min_n(*args):
    return f"Минимальное значение: {min(*args)}"

print(min_n(1, 2, 3, 4, 5))