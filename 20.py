# 20. Определить, присутствует ли в заданном списке строк, некоторое число 

# сделать список строк

stringList = ["qwe", "asd2", "zx2c1", "q33we6", "ertqwe"]
print(f"Имеем список {stringList}")
N = str(input(f"Введите число для поиска \n"))


# алгоритм поиска числа в списке

def findNumber(N,stringList):
    F=0
    findSuccess = 0
    for i in range(0,len(stringList)):
        F = stringList[i].find(N)
        # print(F)
        if F !=-1:
            print(f"Число найдено в элементе номер {i+1} ")
            findSuccess = 1
    if findSuccess != 1:
        print(f"Число не найдено")
             


findNumber(N,stringList)