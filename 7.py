# # 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# Возможные варианты:
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

xList = [0,0,0,0,1,1,1,1]
yList = [0,0,1,1,0,0,1,1]
zList = [0,1,0,1,0,1,0,1]

for i in range(0,8):
    X = xList[i]
    Y = yList[i]
    Z = zList[i]


    if not(X or Y or Z) == ((not X) and (not Y) and (not Z)):
        print(f'Равенство истинно при значениях ¬({X} ⋁ {Y} ⋁ {Z}) = ¬{X} ⋀ ¬{Y} ⋀ ¬{Z}')
        # print(f'Левая часть {not(X or Y or Z)}')
        # print(f'Правая часть {(not X) and (not Y) and (not Z)}')
    else:
        print(f'Равенство не истинно: ¬({X} ⋁ {Y} ⋁ {Z}) = ¬{X} ⋀ ¬{Y} ⋀ ¬{Z}')
        # print(f'Левая часть {not(X or Y or Z)}')
        # print(f'Правая часть {(not X) and (not Y) and (not Z)}')