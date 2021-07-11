"""Создайте программу «Англо-французский словарь». 
Нужно хранить слово на английском языке и его перевод на французский. 
Требуется реализовать возможность до- бавления, удаления, поиска, замены данных. 
Используйте словарь для хранения информации."""

from pprint import pprint

words_english = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
words_french = ["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neof", "dix"]
dictionary_ef = dict(zip(words_english, words_french))
pprint(dictionary_ef)
print("==========================================")

# ==================================================================
# ================ Добавление ======================================
# ==================================================================
w_english = input("Enter the new English word you want to add to the dictionary: ")
if w_english.lower() in words_english:
    print("This word is already in the dictionary")
else:
    w_french = input("Enter this word in French: ")
    dictionary_ef[w_english.lower()] = w_french.lower()
    print(f"Dictionary with new word: {dictionary_ef}")
print("==========================================")

# ==================================================================
# ================== Удаление ======================================
# ==================================================================
dell_en = input("Enter the english word you want to remove from the dictionary: ")
if dell_en.lower() in dictionary_ef.keys():
    del dictionary_ef[dell_en.lower()]
    pprint(dictionary_ef)
else:
    print("This word is not in the dictionary")
print("==========================================")

# ==================================================================
# ===================== Поиск ======================================
# ==================================================================
search_w = input("Enter the word you want to find: " )
if search_w in dictionary_ef.keys():
    s_w = dictionary_ef.get(search_w.lower())
    print(f"This word is in French: {s_w}")
else:
    print("This word is not in the dictionary")
print("==========================================")

# ==================================================================
# ===================== Замена данных ==============================
# ==================================================================
k_w = input("Enter the English word you want to replace: ")
v_w = input("Enter the translation of this word in French: ")
dictionary_ef.update({k_w : v_w})
print(f"Updated dictionary: {dictionary_ef}")
print("==========================================")
