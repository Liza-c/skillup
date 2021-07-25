"""При старте приложения запускаются три потока.Первый поток заполняет список случайными числами.
Два других потока ожидают заполнения. Когда списокзаполнен оба потока запускаются. Первый поток находит
сумму элементов списка, второй поток средне арифметическое значение в списке. Полученный список, сумма и 
средне арифметическое выводятся на экран."""

import  sys, os
import random
from threading import Thread
from time import sleep

class List:
    def __init__(self, random_list = [], sum_numbers = 0, num_avg=0):
        self.random_list = random_list
        self.sum_numbers = sum_numbers
        self.num_avg = num_avg
        
    def rand_list(self):
        self.random_list = [random.randint(0, 10) for i in range(10)]
        print(f"Список: {self.random_list}")
    
    def sum_list(self):
        self.sum_numbers = sum(self.random_list)
        print(f"Сумма: {self.sum_numbers}")

    def avg(self):
        self.num_avg = sum(self.random_list) / len(self.random_list)
        print(f"Среднее арифметическое: {self.num_avg}")
    
def main():
    rl = List()

    t1 = Thread(target=rl.rand_list())
    t2 = Thread(target=rl.sum_list())
    t3 = Thread(target=rl.avg())

    t1.start()
    t1.join()
    t2.start()
    t3.start()

if __name__ == "__main__":
    main()
