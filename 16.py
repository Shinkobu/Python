# 16 Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму


import random


def sequenceGen1 ():
    n = int(input("Введите N \n"))
    i=1
    r=0
    resultSum=0
    resultList = []

    for i in range(1,n+1):
        r = round(pow((1+1/i),i),3)
        resultList.append (r)
        resultSum +=r

    print(f"Последовательность: \n {resultList}")

    print(f"Сумма элементов: \n {resultSum}")

def sequenceGen2 ():
    n = random.randint(1,9)   
       
    resultList = [round(((1+1/i)**i),3) for i in range(1,n+1)]
    resultSum = sum(resultList)

    print(f"\n Последовательность: \n {resultList}")
    print(f"Сумма элементов: \n {resultSum}\n")

# sequenceGen2() # через for
sequenceGen2() # через list comprehension
