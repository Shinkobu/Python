# #  Lambda - анонимный метод 

# def f(x):
#     return x**2

# g=f # переменная хранит в себе ссылку на функцию

# print(type(f))
# print(type(g))

# print(f(2))
# print(g(2))


# def math (op, x):
#     print(op(x))

# math(g,4) 

# # Логика с описание функции

# # def sum(x,y):
# #     return x+y

# # То же самое через лямбда
# sum = lambda x,y: x+y
# print(sum(2,3)) # 1 вариант записи

# print((lambda x,y: x+y)(2,3)) # 2 вариант записи

# # List Comprehension

# # Длинный вариант
# list = []

# for i in range(1,21):
#     if (i%2 == 0):
#         list.append(i);
# print(list)

# # Вариант короче

# list1 = [i for i in range (1,21) if i%2 == 0]
# print(list1)

# # Вариант с кортежем

# list1 = [(i,i) for i in range (1,21) if i%2 == 0]
# print(list1)

# # Вариант с функцией

# def f(x):
#     return x**3

# list1 = [f(i) for i in range (1,21) if i%2 == 0]
# print(list1)

# # Вариант с функцией + кортеж

# def f(x):
#     return x**3

# list1 = [(i,f(i)) for i in range (1,21) if i%2 == 0]
# print(list1)

# Задача
# def select(f, col): # описываем функцию, которая создаёт список через применение функции f к тем x, которые есть в col
#     return [f(x) for x in col]

# def where(f, col):  # описываем функцию, которая создаёт список из элементов col при выполнении условия f(x)
#     return [x for x in col if f(x)]

# data = "1 2 3 5 8 15 23 38".split() # создаём список из текстовых значений

# res = select(int, data)  # преобразуем значения в int через обращение к описанной функции select. Int применяется к каждому элементу data
# print(res)
# res = where(lambda x: not x % 2, res)  # создаём новый список чётных элементов. Вызываем функцию where, которая создаёт список из всех элементов res, 
#                                        # которые удовлетворяют условию lambda: нет остатка при делении на 2

# print(res)
# res = select(lambda x: (x, x**2), res)  # применяем выражение lambda ко всем элементам res, в результате получаем новый список кортежей из чисел и их квадратов
# print(res)



# # map - итератор. !!!Это то же, что и описанная функция select


# li = [x for x in range (1,31)] # создаём список
# print (li)
# li = list(map(lambda x:x+10, li)) # с помощью map производим с каждым элементом li операцию x+10
# print (li)

# data = list(map(int,input().split())) # преобразуем вводимые значения в int разбивая их на отдельные значения если встречаем пробел. И преобразуем их в список
# print (data)

# # filter - применяет функцию к каждому элементу итерируемого объекта и возвращает итератор с теми объектами, для которых функция вернула true

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print (res)

# # zip - применяется к набору итерируемых объектов и возращает итератор с кортежами из элементов входных данных

# users = ['user1','user2','user3']
# ids = [4,5,12]

# data = list(zip(users, ids))
# print (data)

# enumerate - применяется к итерируемому объекту и возращает новый итератор с кортежами из индекса и элементов входных данных.

users = ['user1','user2','user3']

data = list(enumerate(users))
print (data)