"""Создайте программу, хранящую информацию о великих баскетболистах. 
Нужно хранить ФИО баскетболиста и его рост. 
Требуется реализовать возможность добавления, удаления, поиска, замены данных. 
Используйте словарь для хранения информации."""

from pprint import pprint

players = ["Kobe Bryant", "By Gasol", "LeBron James", "Vince Carter", "Tracy McGrady"]
height = [202, 198, 210, 208, 196 ]
dictionary_pl = dict(zip(players, height))
pprint(dictionary_pl)
print("==========================================")

# ==================================================================
# ================ Добавление ======================================
# ==================================================================
new_pl = input("Enter the first and last name of the basketball player you want to add: ")
if new_pl in dictionary_pl.keys():
    print("This player is already on the list.")
else:
    new_height = input("Enter this player's height: ")
    dictionary_pl[new_pl] = new_height
    print(f"Dictionary with new word: {dictionary_pl}")
print("==========================================")

# ==================================================================
# ================== Удаление ======================================
# ==================================================================
dell_pl = input("Enter the first and last name of the player you want to remove from the dictionary: ")
if dell_pl in dictionary_pl.keys():
    del dictionary_pl[dell_pl]
    pprint(dictionary_pl)
else:
    print("This player is not in the dictionary")
print("==========================================")

# ==================================================================
# ===================== Поиск ======================================
# ==================================================================
search_pl = input("Enter the first and last name of the player whose height you want to find: " )
if search_pl in dictionary_pl.keys():
    h_p = dictionary_pl.get(search_pl)
    print(f"This player's height: {h_p}")
else:
    print("This player is not on the list")
print("==========================================")

# ==================================================================
# ===================== Замена данных ==============================
# ==================================================================
p = input("Enter the player's first and last name: ")
r_p = input("Enter his height: ")
dictionary_pl.update({p : r_p})
print(f"Updated dictionary: {dictionary_pl}")
print("==========================================")
