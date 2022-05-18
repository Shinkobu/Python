# 39.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"




import random


# Игра против человека

def candyGame (Total,pList):

    # Жеребьёвка
    turnNumber = random.randint(-1,0)
    print (f"\n По результатам жеребьёвки первым ходит {pList[turnNumber+1]}\n")

    # Игра
    while Total > 0:

        turnNumber += 1
        turn = int(input(f"Ходит {pList[turnNumber%2]}.\n На столе {Total} конфет. Сколько конфет берёшь? \n"))
        
        # Проверка значения
        while turn > 28 or turn > Total:
            turn = int(input(f"За один ход можно забрать не более чем 28 конфет и не больше, чем лежит на столе!  \n"))
        
        Total = Total - turn
        
    print (f"На столе осталось {Total} конфет! Последние конфеты взял {pList[turnNumber%2]}.\n Победил {pList[((turnNumber)%2)]} !!!")

   
# Игра против примитивного бота

def candyGameBot (Total,pList):

    pList[1] = "Компьютер"
    # Жеребьёвка
    turnNumber = random.randint(-1,0)
    print (f"\n По результатам жеребьёвки первым ходит {pList[turnNumber+1]}\n")

    # Игра
    while Total > 0:

        turnNumber += 1

        # Блок выбора бота с проверкой значения
        if pList[turnNumber%2] == "Компьютер":
            print(f"Ходит {pList[turnNumber%2]}.\n На столе {Total} конфет. Сколько конфет берёшь?")
            turn = random.randint(1,28)
            while turn > Total:
                turn = random.randint(1,28)
            print(turn)
        else:
            turn = int(input(f"Ходит {pList[turnNumber%2]}.\n На столе {Total} конфет. Сколько конфет берёшь? \n"))
                   
        # Проверка значения для человека
            while turn > 28 or turn > Total:
                turn = int(input(f"За один ход можно забрать не более чем 28 конфет и не больше, чем лежит на столе!  \n"))
        
        Total = Total - turn
        
    print (f"На столе осталось {Total} конфет! Последние конфеты взял {pList[turnNumber%2]}.\n Победил {pList[((turnNumber)%2)]} !!!")


Total = 50
pList = ["Игрок 1","Игрок 2"]

candyGameBot (Total,pList)