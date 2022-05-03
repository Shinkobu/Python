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

xList = [False,False,False,False,True,True,True,True]
yList = [False,False,True,True,False,False,True,True]
zList = [False,True,False,True,False,True,False,True]

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