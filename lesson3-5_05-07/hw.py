import fileinput

#==================  task1 ================================

def common_lines(f1, f2):
    file_1 = open(f1)
    file_2 = open(f2)
    for line1, line2 in zip(file_1, file_2):
        if line1 != line2:
            print(line1)
            print(line2)

print(common_lines("C:/Users/lizak/OneDrive/Desktop/text_1.txt","C:/Users/lizak/OneDrive/Desktop/text_2.txt"))
print("====================================================")

#======================  task2 ============================

def file_statistics(f1):
    file_1 = open(f1)
    countV = 0
    countC = 0
    countN = 0
    for j in file_1:
        for i in j.lower():
            if i.lower() in 'aeiou':
                countV += 1
            elif i.lower() in "qwrtyupsdfghjklzxcvbnm":
                countC += 1
            elif i.lower() in '0123456789':
                countN +=1
    file_1.close()
    file_1 = open(f1)
    size = len(file_1.read())
    file_1.close()
    file_1 = open(f1)
    lines = len(file_1.readlines())
    file_1.close()
    line = (f"Количество согласных: {countC}, количество гласных: {countV}, количество цифр: {countN}."\
            f"Количество символов: {size}, количество строк: {lines}")
    path = input("Введите директорию нового файла: ")
    new_file = open(path, 'w')
    new_file.write(line)
    file_1.close()
    new_file.close()

print(file_statistics("C:/Users/lizak/OneDrive/Desktop/text_1.txt"))
print("====================================================")

#======================  task3 ============================

def delete_line(f1, f2):
    f = open(f1)
    f_new = open(f2, "w")

    lines = f.readlines()
    l = lines[:-1]
    f_new.write(f"{l}")
    

    f.close()
    f_new.close()

delete_line("C:/Users/lizak/OneDrive/Desktop/text_2.txt", "C:/Users/lizak/OneDrive/Desktop/text_3.txt")

#======================  task4 ============================

def longest_line(file):
    f = open(file)
    max_line = max(f.readlines(), key=len)
    print(f"Самая длинная строка: {max_line}. Её длина - {len(max_line)}")
    f.close()
longest_line("C:/Users/lizak/OneDrive/Desktop/text_2.txt")

#======================  task5 ============================

def count_word(file, word = input("Введите слово: ")):
    f = open(file)
    data = f.read()
    c = data.count(word)
    print(f"Количество вхождений заданного слова в тексте: {c}")
    f.close()
print("====================================================")

file = "C:/Users/lizak/OneDrive/Desktop/text_1.txt"
print(count_word(file))

#======================  task6 ============================

def replace_in_file(file, word, r_word):
    with fileinput.input(file, inplace=True) as f:
        for line in f:
            line = line.replace(word, r_word)
            print(line, end="")
file = "C:/Users/lizak/OneDrive/Desktop/text_2.txt"
replace_in_file(file, "This", "this")







