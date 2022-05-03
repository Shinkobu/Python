# # 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
# Пример от преподавателя

a = [0, 1]
print('X Y Z F')
for x in a:
    for y in a:
        for z in a:
            f = not(x or y or z) == (not x and not y and not z)
            print (x, y, z, int(f))