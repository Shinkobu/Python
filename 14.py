# 14. Подсчитать сумму цифр в вещественном числе.

S1 = str(abs(float((input("Введите вещественное число: ")))))
S1 = S1.replace(".","0")
S1 = list(S1)


# print(S1)
S=0
# i=0
# S = int(S1[0])
# print(S)

for i in range(len(S1)):
    S+=int(S1[i])


print(f"Сумма цифр составляет {S}")

