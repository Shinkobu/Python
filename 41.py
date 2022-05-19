# 41.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWww
# Входные данные: 
# 12W1B12W3B24W1B14W

# Берём данные из файла

data = open('task41 input.txt', 'r') # a - добавить, w - перезаписать, r - чтение
rawData = str(data.readline())
print(rawData)
data.close

# Обрабатываем 

outputList = []
charNumber = 0

l = len(rawData)

while charNumber < len(rawData)-1:

    counter = 0
    charName = rawData[charNumber]
    while charName == rawData[charNumber]:
        charNumber += 1
        counter += 1
        if charNumber == len(rawData): break
            
    outputList.append(str(counter)+charName)
    print(outputList)

# Записываем данные в файл
data = open('task41 output.txt', 'w') # a - добавить, w - перезаписать, r - чтение

for i in range(0,len(outputList)): data.write(outputList[i])


data.close
