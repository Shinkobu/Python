# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.


def genDict1 ():

    n = int(input("Введите количество элементов словаря = "))
    dictionary = {}

    for a in range(1,n+1):    # Можно записать так
        dictionary[a] = 3*a+1

    print('Итоговый словарь: ',dictionary)

def genDict2 ():

    n = int(input("Введите количество элементов словаря = "))
    dictionary = {}

    dictionary = {a: 3*a+1 for a in range(1,n+1)} # тоже самое, но в одно выражение
    print('Итоговый словарь: ',dictionary)

genDict1 () # вариант через for
genDict2 () # вариант через comprehension
