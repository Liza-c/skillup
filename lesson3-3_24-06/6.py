""" Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра. 
Из функции нужно вернуть полученное количество цифр. """

def count_n(a):
    lenght = len(str(a))
    return f"Количество цифр в числе: {lenght}"

print(count_n(3154))