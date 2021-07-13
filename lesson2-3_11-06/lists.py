""""Два списка целых заполняются случайными числами. Необходимо:
Сформировать третий список, содержащий элементы обоих списков;
Сформировать третий список, содержащий элементы обоих списков без повторений;
Сформировать третий список, содержащий элементы общие для двух списков;
Сформировать третий список, содержащий только уникальные элементы каждого из списков;
Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков."""

from random import randint

list_1 = sorted([randint(1, 30) for i in range(15)])
list_2 = sorted([randint(1, 50) for i in range(15)])

print(f"First list: {list_1}")
print(f"Second list: {list_2}")

list_3 = sorted(list(set(list_1+list_2)))
print(f"Third list containing the elements of both lists without repetitions: {list_3}")

list_4 = sorted(list(set(list_1) & set(list_2)))
print(f"Third list containing elements common to the two lists: {list_4}")

list_5 = sorted(list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1)))
print(f"List containing only the unique elements of each of the lists: {list_5}")

list_6 = []
list_6.append(min(list_1))
list_6.append(min(list_2))
list_6.append(max(list_1))
list_6.append(max(list_2))
print(f"List containing only the minimum and maximum value of each of the lists: {sorted(list_6)}")
