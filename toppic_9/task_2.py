glasniy = ["а", "у", "е", "о", "э", "я", "ы", "и", "ё", "ю"]
data = input("Введите любое слово: ")
g = 0
sg = 0
for i in data:
    if i in glasniy:
        g += 1
    else:
        sg += 1
print("Количество гласных букв:", g)
print("Количество согласных букв:", sg)

# Твоё решение
'''Введите любое слово: Предприниматель
Количество гласных букв:  5
Количество согласных букв:  10'''

# Моё решение
'''
Введите любое слово: Предприниматель
Количество гласных букв:  10
Количество согласных букв:  5
'''

# Я бы решил эту задачу так:
word = input('Введите любое слово: ')

vowels = 'аяоёуюыиэе'  # гласные

vowels_count = 0  # количество гласных
consonants_count = 0  # количество согласных

for let in word:
    if let not in vowels:  # если буква нет в последовательности гласных
        consonants_count += 1
        continue

    # иначе увеличиваю количество гласных
    vowels_count += 1

print('Количество гласных букв:', vowels_count)
print('Количество согласных букв:', consonants_count)
