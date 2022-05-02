# 34.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Берём данные из 1 файла
data = open('Polynom1 - 34.txt', 'r') # a - добавить, w - перезаписать, r - чтение
S1 = str(data.readline())
S1 = S1.replace("=0","") # Убираем лишнее
# print(S1)
data.close

data = open('Polynom2 - 34.txt', 'r') # a - добавить, w - перезаписать, r - чтение
S2 = str(data.readline())
# print(S2)
data.close

# объединяем две строки и записываем результат в файл
S1S2 = S1+'+'+S2
# print (S1S2)

data = open('Result - 34.txt', 'w') # a - добавить, w - перезаписать, r - чтение
data.write(S1S2)
data.close
