""" Напишите функцию, которая проверяет является ли число палиндромом. 
Число передаётся в качестве параметра. 
Если число палиндром нужно вернуть из функции true, иначе false.
 """
def palindrome(a):
    a = str(a)
    if a == a[::-1]:
        return True
    else:
        return False

print(palindrome("oloolo"))
print(palindrome(123321))
print(palindrome(546845))