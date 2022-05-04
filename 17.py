# 17 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

n = int(input("Введите N \n"))

# создаём список [-N, N]
i=1
resultList = []

for i in range(-n,n+1):
    resultList.append (i)
   
print(f"Последовательность: \n {resultList}")

#  считываем позиции из файла и находим результат 

# Берём данные из 1 файла
indexList = []
data = open('file.txt', 'r')

for line in data:
    S = int(line)
    indexList.append (S)
data.close

print (f"Список с номерами элементов: \n {indexList}")

# Вычисляем произведение элементов
productResult = 1

for j in range(0,len(indexList)):
    productResult *= resultList[indexList[j]-1]
    # print (productResult)

print (f"Произведение элементов: \n {productResult}")

