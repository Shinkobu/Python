print ('Hello World')

value = None
a=123
b=1.23
print(a)
print(type(a)) # тип данных
print(b)
print(type(b))

s = "hello world"

print (a,b,s)
print (a,'-',b,'-',s)
print ('{} - {} - {}'.format (a,b,s))
print ('{1} - {0} - {2}'.format (a,b,s))
print (f'{a} - {b} - {s}')

#массивы

list = ['1','2','3','hello',1.2,True]
print(list)

# ввод и вывод

print("Введите значения")
k=input()
k=int(input()) # ввод в integer
print(k)

# функция
def f(x):
    if x == 1:
        return "Целое"
    elif x == 2.3:
        return 23
    else:
        return
