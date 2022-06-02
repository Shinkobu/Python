import logger

import csv


def find_entry(word):
    find_count = 0

    with open("students.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        for row in file_reader:
            strrow = str(row)
            # print(strrow.find(word))
            if strrow.find(word) != -1:
                print(f"Найдена запись: {row}")
                find_count = find_count + 1
    if find_count == 0:
        print ("Записи не найдены")

    return (find_count)
    
    
# find_entry()

# проект редактирования записи
# def edit_entry():
#     id_student = input("Введите id ученика для изменения записи в базе учеников\n")

#     while find_entry(id_student) != 1:
#         if find_entry(id_student) > 1:
#             id_student = input("\nНайдено несколько записей, введите уникальный id\n")
#         if find_entry(id_student) == 0:
#             id_student = input("\nПовторите ввод id\n")
    
#     with open("students1.csv", encoding='utf-8') as r_file:
#         file_reader = csv.reader(r_file, delimiter = ",")
#         print("\nПерезапишите значения полей\n")
        
#         for row in file_reader:
#             print(f"\nТекущее значение {id_student} - {row}\n")
        

# edit_entry()