""" Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними. """

def even_numbers(a, b):
    if a < b:
        return [i for i in range(a, b) if i%2 == 0]
    elif a > b:
        return [i for i in range(b, a) if i%2 ==0]
    else:
        return []

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(f"Четные числа, которое находятся в заданом диапазоне: {even_numbers(a, b)}")
