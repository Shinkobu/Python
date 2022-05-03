# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

n = int(input("Введите N \n"))
i=1
r=1
resultList = []

for i in range(1,n+1):
    r=r*i
    resultList.append (r)

print(f"Набор произведений от 1 до {n}: \n {resultList}")


