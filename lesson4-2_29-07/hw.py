""" Реализовать 2 вида Стека с применением классов.
Метод push каждого из них будет работать следующим образом:
Принимает только числа.
Если число до 50 - засыпаем на 1 секунду (использовать time.sleep()).
Если число после 50 - засыпаем на 2 секунды. 
Нужно создать 2 объекта этого стека и используя random.randint() добавить в каждый из них по 10 значений.
Реализовать Асинхронный стек с теми же условиями.
Значения от randint() получем из генератора.
Использование исключений обязательно! (edited) """

from time import sleep
from random import randint
import asyncio
import time

class Stack:
    def __init__(self, name) -> None:
        self.__name = name
        self.__data = []
        
    def __repr__(self) -> str:
        return f"{self.__name} = {self.__data}"

    @property
    def name(self):
        return self.__name
    
    def add_value(self, value):
        self.__data.append(value)
    
    def pop(self):
        try:
            value = self.__data[-1]
            del self.__data[-1]
            return value
        except IndexError:
            return None
    
    def push(self, value):
        try:
            v = int(value)
            self.add_value(v)
            if v < 50:
                t = 1
            else:
                t = 2
            print(f"{self.__name} = Value: {v}. Sleep: {t}")
            sleep(t)
        except ValueError:
            print("Wrong value.")

class AsStack(Stack):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    async def push(self, value):
        try:
            v = int(value)
            self.add_value(v)
            if v < 50:
                t = 1
            else:
                t = 2
            print(f"{self.name} = Value: {v}. Sleep: {t}")
            await asyncio.sleep(t)
        except ValueError:
            print("Wrong value.")

def generator(n):
    for i in range(n):
        yield randint(1, 100)

def main():
    n = 10
    count_stacks = 2

    start_time = time.time()
    stasks = []
    for i in range(1, count_stacks + 1):
        stasks.append(Stack(f'stack#{i}'))

    for stack in stasks:
        for i in generator(n):
            stack.push(i)
        print(stack)
    
    print(f"--- {time.time() - start_time} seconds ---")

    start_time = time.time()
    as_stacks = [AsStack(f"async_stack#{i}") for i in range(1, count_stacks + 1)]
    tasks = [asrack.push(i) for asrack in as_stacks for i in generator(n)]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    for i in as_stacks:
        print(i)
    print(f"--- {time.time() - start_time} seconds ---")

if __name__ == "__main__":
    main()

