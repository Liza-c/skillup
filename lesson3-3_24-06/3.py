""" Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. 
Функция принимает в качестве параметров: длину стороны ква- драта, символ и переменную логического типа:
если она равна True, квадрат заполненный; если False, квадрат пустой. """

def draw_square(side_lenght, symbol, a, min_side_len = 3, space = " "):
    if side_lenght < min_side_len:
        print("Длина стороны меньше 3")
        return None
    if a:
        for i in range(side_lenght):
            print(side_lenght * symbol)
    else:
        print(side_lenght * symbol)
        for i in range(side_lenght - 2):
            print(symbol + space * (side_lenght - 2) + symbol)
        print(side_lenght * symbol)    
    
print(draw_square(5,"#",True))
print(draw_square(5,"*",False))
