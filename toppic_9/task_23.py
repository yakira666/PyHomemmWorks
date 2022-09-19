people_age = int(input("Введите возраст посетителя (0 для окончания ввода): "))
age_1 = 0  # Количество детей до 3
age_2 = 0  # Количество детей от 3 до 12
age_3 = 0  # Количество взрослых
age_4 = 0  # Количество пенсионеров

while people_age != 0:
    if 0 < people_age < 3:
        age_1 += 1
    elif 2 < people_age < 13:
        age_2 += 1
    elif 12 < people_age < 66:
        age_3 += 1
    elif people_age > 65:
        age_4 += 1
    elif people_age == "":  # бывает проскакивает пустой пробел - решил сделать чтоб просто не считало))
        continue
    people_age = int(input("Введите возраст посетителя (0 для окончания ввода): "))
print(
    f'\nКоличестово детей до двух лет: {age_1}\n'
    f'Количестово детей от 3-х до 12 лет: {age_2}\n'
    f'Количестово взрослых: {age_3}\n'
    f'Количестово пенсионер: {age_4}\n'
    f'\nОбщая стоимость билетов {(age_4 * 1449) + (age_3 * 2099) + (age_1 * 1055) + (age_2 * 0):,.2f}\n')


'''
1. Самый первый вопрос, который у меня возник, был - что будет, если поменяются возрастные категории?

2. Задачу можно улучшить с помощью оператора "морж"

3. Если ввести входные данные со скриншота, то твоя программа показывает неверный результат

    Количестово детей до двух лет: 3
    Количестово детей от 3-х до 12 лет: 5
    Количестово взрослых: 4
    Количестово пенсионер: 4
    
    Общая стоимость билетов 17,357.00

а, общая стимость должна быть 19,467.00 и символ рубля
'''


