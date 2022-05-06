# 19 Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел


# Будем генерить случайное число от 0 до 9 от системного времени

from datetime import datetime

sumSec = 0

for i in range(0,100000):
    currentMicrosecond = datetime.now().microsecond
    # print(currentMicrosecond)
    sumSec += currentMicrosecond 

# print(sumSec)

rand = sumSec % 10
print(f"Случайное число: {rand}")



