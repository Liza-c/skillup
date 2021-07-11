print("--------------------------------- list --------------------------------")
list1 = ['l', 'i', 's', 't']
list2 = list('list2') #создание списка с помощью функции list()
print(list1)
print(list2)
print(list1[0]) #обращение к элементу списка по номеру
print(list1[1::]) #срез
print(list1[::2]) #срез с шагом 2
print(list2[::-1]) #перевернуть список
list2.reverse() #перевернуть список с помощью метода reverse()
print(list2)
list1[0] = 'list' #поменять первый элемент списка
print(list1)
print(len(list1)) #количество элементов в списке
print(sorted(list1)) #сортировка элементов списка по возрастанию

list3 = [1, '2', list('numbers')]
print(list3)
print(list3[2][5])

print("--------------------------------- dictionary --------------------------------")
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': '5'}
d = dict(short='dict', long='dictionary')
b = dict([(1, 2), (3, 4)])
print(numbers)
print(d)
print(b)
d = dict.fromkeys(["a", "b"]) #{"a": None, "b": None}
d = dict.fromkeys(["a", "b"], 1)
print(d)
d.clear()
d = {i: pow(i, 2) for i in range(5)}
print(d)
print(d[0])
d[0] = 15
print(d)
d_copy = d.copy() #Копия словаря
print(d_copy.get(0)) #Значение ключа
print(d_copy.items()) #Ключ-значение
print(d_copy.keys()) #Возврат ключей
print(d_copy.pop(0)) #удаляет ключ и возвращает значение
print(d_copy.popitem())
print(d_copy.setdefault(1))
print(d_copy.values())


print("--------------------------------- tuple --------------------------------")
print(tuple()) 
t = ('t', )
print(t)
t = tuple('tuple')
print(t)
print(sorted(t))


print("--------------------------------- set_frozenset --------------------------------")
s = set('hello')
print(s)
s_1 = {i**2 for i in range(10)}
print(s_1)
words = {'hello', 'number', 'typle', 'hello'}
s = set(words)
print(s)
print(len(s))
print('1' in s)
print(s.isdisjoint(s_1))
print(s == s_1)
print(s.union(s_1))
s.add('15')
print(s)
s.discard('hello')
print(s)

a = set('chdskn')
b = frozenset('chdskn')
print(a == b)
print(a - b)
a.add('kk')
print(a)


print("--------------------------------- bool --------------------------------")
items = [1, 2, 3, 4, 5]
it = []
print(bool(items))
print(bool(it))
print(bool(0))


print("--------------------------------- type_conversion --------------------------------")
print(int('15'))
print(int("11111111", 2))
print(bin(10))
print(bin(15))
print(hex(15))
print(list('hello'))
print(set('hello hello'))
print(tuple([1, 2, 3, 4, 5]))
print(str(15))


print("--------------------------------- str --------------------------------")
line_1 = "Hello World !"
print(len(line_1))
print(line_1.find('a'))
print(line_1.rfind('l'))
print(line_1.index('l'))
print(line_1.rindex('l'))
print(line_1.replace('World', 'world'))
print(line_1.split())
print(line_1.isdigit())
print(line_1.isalpha())
print(line_1.isalnum())
print(line_1.islower())
print(line_1.upper())
w = ['Hello', 'world', '!']
print(' '.join(w))