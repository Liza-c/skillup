""" Написать функцию-декоратор, которая подносит к квадрату значения, 
которое возвращает функция, к которой декоратор применяется. """

def decorator_sqare(func):
    def wrapped(arg):
        res = func(arg)
        print(f"Число {arg} в квадрате: {res**2}")
    return wrapped

@decorator_sqare
def function(number):
    return number

print(function(5))
print(function(10))

#Вывод:
#Число 5 в квадрате: 25
#Число 10 в квадрате: 100
