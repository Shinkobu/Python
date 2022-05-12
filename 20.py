# 20. Определить, присутствует ли в заданном списке строк, некоторое число 

# сделать список строк

stringList = ["qwe", "asd2", "zxc1", "qwe6", "ertqwe"]
N = str(input(f"Введите число для поиска \n"))


# алгоритм поиска числа в списке

def findNumber(N,stringList):
    F=0
    for i in range(0,len(stringList)):
        F = stringList[i].find(N)
        print(F)    

             


findNumber(N,stringList)