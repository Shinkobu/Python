# 18. Реализовать алгоритм перемешивания списка. 

import random


newList = [1,2,3,4,5,6,7,8,9,10]

print(f"Исходный список: \n {newList}")

for i in range(0,len(newList)-1):
    j = random.randint(0,len(newList)-1)
    tempElement = newList[i]
    newList[i] = newList[j]
    newList[j] = tempElement

print(f"\n Перемешаный список: \n {newList}")
    