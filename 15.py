# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

import math
import random


def multyplic1 ():
    n = int(input("Введите N \n"))

    r=1
    resultList = []

    for i in range(1,n+1):
        r=r*i
        resultList.append (r)

    print(f"Набор произведений от 1 до {n}: \n {resultList}")

def multyplic2 ():
    n = random.randint(5,10)

    resultList = [math.factorial(i) for i in range (1,n+1)]

    print(f"Набор произведений от 1 до {n}: \n {resultList}")

multyplic1() # через for
multyplic2() # через list comprehension и факториал

# Чужой вариант через accumulate

# import os
# from itertools import accumulate
# import operator
# import random
# os.system("cls")

# n = random.randint(8, 16)

# print(' Задать последовательность из', n, 'элементов\n',
# 'Последовательность:', *list(accumulate([x for x in range(1, n + 1)], operator.mul)), '\n')

