# 31.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("Введите натуральное число N = "))

digitsList = []


for i in range(2,N):
    
    while N%i == 0:
        digitsList.append(i)
        # print(digitsList)
        N=N/i
        # print(N)

if len(digitsList) == 0:
    print(f"Число является простым")
else:
    print(f"Cписок множителей числа: {digitsList}")

