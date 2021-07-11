""" Задание 1. Есть три кортежа целых чисел необходимо найти элементы, которые есть во всех кортежах.
    Задание 2. Есть три кортежа целых чисел необходимо найти элементы, которые уникальны для каждого списка.
    Задание 3. Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и 
    находятся в каждом из кортежей на той же позиции."""

from random import randint

A = tuple(randint(1, 6) for i in range(10))
B = tuple(randint(1, 5) for i in range(10))
C = tuple(randint(1, 5) for i in range(10))
print(f"First tuple: {A}\nSecond tuple: {B}\nThird tuple: {C}")

# ==================================================================
# ========== Элементы, которые есть во всех кортежах ===============
# ==================================================================
ABC = tuple(set(A) & set(B) & set(C))
print(f"Elements that are in all tuples: {ABC}")

# ==================================================================
# ========== элементы, которые уникальны для каждого списка ========
# ==================================================================
abc = list(set(A) - set(B) - set(C))
bac = list(set(B) - set(A) - set(C))
cab = list(set(C) - set(A) - set(B))
un_el = tuple(abc + bac + cab)
print(f"Elements that are unique to each list: {un_el}")

# ==================================================================
# ===== Общие элементы, которые находятся на той же позиции ========
# ==================================================================

same_position = []
s = [x for x, y, z in zip(A, B, C) if x == y == z]
for i in s:
    same_position.append(i)
if len(same_position) == 0: 
    print("There are no such elements that are in each of the tuples and are in each of the tuples at the same position")
else: 
    print(f"Common elements that are in each of the tuples at the same position: {same_position}")

#Output
#First tuple: (4, 1, 5, 2, 6, 5, 4, 4, 2, 4)
#Second tuple: (2, 3, 3, 1, 1, 5, 4, 3, 3, 2)
#Third tuple: (4, 4, 3, 5, 5, 5, 1, 3, 3, 3)
#Elements that are in all tuples: (1, 4, 5)
#Elements that are unique to each list: (6,)
#Common elements that are in each of the tuples at the same position: [5]