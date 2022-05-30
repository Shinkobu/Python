
##################################### Запись данных в файл.
#### Вариант 1

# colors = ['red', 'green', 'blue1']
# data = open('file.txt', 'a') # a - добавить, w - перезаписать, r - чтение
# # data.writelines(colors) # разделителей не будет
# data.write('Line 2\n') - # \n - переход на следующую строку
# data.write('Line 3\n')
# data.close() # закрыть подключение к файлу

##### Вариант 2. не нужна команда data.close()
# with open ('file.txt','w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

###### Чтение данных из файла
# path = 'file.txt'
# data = open(path,'r')
# for line in data:
#     print(line)
# data.close()
# exit()

##### вызов функции из другого файла

# import lec

# print(lec.f(1))

##### функция с умножением числа на строку  
# def new_string (symbol, count=3):  # можно передать любое значение в count, но по умолчанию оно будет равно 3
#     return symbol*count

# print(new_string('!',5))

##### функция с неограниченным количеством аргументов

# def concatenatio(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res

# def concatenatio(*params):
#     res = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio ('a','s','d','f'))
# print(concatenatio(1,2,3,4))

######## Рекурсия

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         list = []
# for e in range (1,10):  return fib(n-1)+fib(n-2)

#     list.append(fib(e))
# print(list)

############ Кортежи - неизменяемый список

# a = (3,4)
# print(a)

########### Словари

# dictionary = {}
# dictionary = \
#     {
#         'up': '1',
#         'left': '2',
#         'right': '3',
#         'down': '4'
#     }
# print(dictionary)
# print(dictionary['left'])

# for i in dictionary.keys():
#     print(i)

# for i in dictionary.values():
#     print(i)

########### Множества

# colors = {'red','green','blue'} 
# print(colors)
# colors.add('gray') # в множество можно добавить только уникальный элемент. Не может быть в нём 2х одинаковых элементов
# #  есть все операции со множествами

############ Списки

list1 = [1,2,3,4,5]

print(list1.pop()) # извлекает последний элемент списка
print(list1)
print(list1.pop(2)) # извлекает второй элемент списка
print(list1)

print(list1.insert(2, 11)) # добавляет элемент списка на позицию 2
print(list1)
print(list1.append(11)) # добавляет элемент списка в конец
print(list1)

