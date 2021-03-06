"""Создать множества: A, B, C з любыми элементами. Найти:
    1. Разные элементы для A и B.
    2. Одинаковые элементы для A и C.
    3. Объединение 3-х множеств."""

from random import randint

A = set(randint(1, 20) for i in range(10))
B = set(randint(1, 20) for i in range(10))
C = set(randint(5, 20) for i in range(10))
print(f"Set A: {A}\nSet B: {B}\nSet C: {C}")

# ==================================================================
# ========== Объединение 3-х множеств ==============================
# ==================================================================
ABC = (A | B | C)
print(f"Union of 3 sets: {ABC}")

# ==================================================================
# ========== Одинаковые элементы для A и C =========================
# ==================================================================
intersection_AC = (A & C) 
#AC = A.intersection(C)
print(f"Intersection of sets A and C: {intersection_AC}")

# ==================================================================
# ========== Разные элементы для A и B =============================
# ==================================================================
symm_diff_AB = (A ^ B)
#AB = A.symmetric_difference(B)
print(f"Different items for sets A and B: {symm_diff_AB}")

#Вывод
#Set A: {1, 2, 5, 6, 7, 8, 11, 12, 17}
#Set B: {7, 9, 10, 11, 12, 14, 15, 20}
#Set C: {5, 7, 8, 11, 15, 16, 17}
#Union of 3 sets: {1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 20}
#Intersection of sets A and C: {5, 7, 8, 11, 17}
#Different items for sets A and B: {1, 2, 5, 6, 8, 9, 10, 14, 15, 17, 20}