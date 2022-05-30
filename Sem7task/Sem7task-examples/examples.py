# Пример использования маски при записи:


# Ввод вручную
def manual_input():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    note = input("Введите примечание: ")
    orient = input("Выберите метод заполнения (1 - вертикальный, 2 - горизонтальный): ")
    return(surname,name,phone,note,orient)

# Сохранение новой записи
def save(surname,name,phone,note,orient):
    if orient == '1':
        file = open('vertical.csv', 'a')
        file.write(f'{surname}\n{name}\n{phone}\n{note}\n\n')
        file.close()
    if orient == '2':
        file = open('horizontal.csv', 'a')
        file.write(f'{surname};{name};{phone};{note}\n\n')
        file.close()

#  Пример:
temp = manual_input()
print(temp)
save(temp[0], temp[1], temp[2], temp[3], temp[4],)
