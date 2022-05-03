# 17 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

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


