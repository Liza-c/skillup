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
    list_1 = List()

    thread_1 = Thread(target=list_1.rand_list())
    thread_2 = Thread(target=list_1.sum_list())
    thread_3 = Thread(target=list_1.avg())

    thread_1.start()
    print(f"thread status: {thread_1.is_alive()}")
    sleep(5)
    print(f"thread status: {thread_1.is_alive()}")
    thread_1.join()
    print(f"thread status: {thread_1.is_alive()}")
    thread_2.start()
    thread_3.start()


if __name__ == "__main__":
    main()
