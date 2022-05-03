# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

import os
os.system("cls")

x = [True, False]
y = [True, False]
z = [True, False]
print('\tX\tY\tZ\t¬(X ⋁ Y ⋁ Z)\t¬X ⋀ ¬Y ⋀ ¬Z\t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print('_'*100)
for index in range(2):
    for count in range(2):
        for i in range(2):
            left = not(x[index] and y[count] and z[i]) # левая часть равенства
            print(f"\t{x[index]} \t{y[count]} \t{z[i]}\t\t{left}", end='')
            right = not(x[index]) or not(y[count]) or not(
            z[i]) # правая часть равенства
            print(f"\t\t{right}", end='')
            print('\t\t', left == right)
print('\n')