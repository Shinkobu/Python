# 14. Подсчитать сумму цифр в вещественном числе.


from functools import reduce


def digitsQuantity1 ():
    S1 = str(abs(float((input("Введите вещественное число: ")))))
    S1 = S1.replace(".","0")
    S1 = list(S1)

    S=0
    for i in range(len(S1)):
        S+=int(S1[i])

    print(f"Сумма цифр составляет {S}")

def digitsQuantity2 ():
    S1 = str(abs(float((input("Введите вещественное число: ")))))
    S1 = S1.replace(".","0")
    S1 = list(S1)

    S=0
    S1 = list(map(lambda x: int(x) ,S1))
    S = reduce(lambda x,y: x+y ,S1)

    print(f"Сумма цифр составляет {S}")

digitsQuantity1 () # через for
digitsQuantity2 () # через map и reduce

