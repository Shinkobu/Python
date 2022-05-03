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
data = open('file.txt', 'r')
for line in data:
    S = int(data.readline())
    print(S)
data.close


