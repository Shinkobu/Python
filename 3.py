# 3. Вывести на экран числа от -N до N

a= int(input('Число для операции ='))


print(f'Числа от {-a} до {a}:')
for i in range(-a,a+1):
    print(i)
