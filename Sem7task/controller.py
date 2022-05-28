# Семинар 7. Домашнее задание:
# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# •	под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель
# Фамилия_1
# Имя_1
# Телефон_1
# Описание_1

# Фамилия_2
# Имя_2
# Телефон_2
# Описание_2

# и т.д.в файле на одной строке хранится все записи, символ разделитель - ;
# Фамилия_1,Имя_1,Телефон_1,Описание_1
# Фамилия_2,Имя_2,Телефон_2,Описание_2
# и т.д.

# Можно использование CSV

# Итак:
# 1. Вывести справочник на экран
# 2. Импортировать новые записи (в разных форматах)
# 3. Экспортировать все записи (в разных форматах)
#  Формат включает в себя структуру и разделитель

import csv
from itertools import count
from queue import Empty
from sqlite3 import Row
from csv import writer



# Показывает базу данных в консоли
def show_db():
    with open("database.csv", encoding='windows 1251') as r_file:
        # Создаем объект reader, указываем символ-разделитель 
        file_reader = csv.reader(r_file, delimiter = ",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        print(f'\nТелефонный справочник имеет вид: \n')
        for row in file_reader:
            print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
            count += 1
        print(f'\nВсего в файле {count} строк.\n')

# Импорт данных в базу данных - значения в одну строку
def import_data(delim):
    
    row_counter ('database.csv')
    row_counter ('import.csv')

    with open('database.csv', 'a', newline='') as db_file, open("import.csv",'r') as imp_file:
        csv_db = csv.writer(db_file)
        csv_imp = csv.reader(imp_file, delimiter = delim)

        for row in csv_imp:
            imp_row_list = [row[0], row[1], row[2], row[3]]
            csv_db.writerow(imp_row_list)
            print (row)

# Экспорт данных в файл экспорта - значения в одну строку
def export_data(db_delimiter,out_delimeter):
    
    row_counter ('database.csv')
    row_counter ('export.csv')

    with open('export.csv', 'w', newline='') as exp_file, open("database.csv",'r') as db_file:
        csv_exp = csv.writer(exp_file, delimiter = out_delimeter)
        csv_db = csv.reader(db_file, delimiter = db_delimiter)
        exp_row_list = []
        for row in csv_db:
            exp_row_list = [row[0], row[1], row[2], row[3]]
            csv_exp.writerow(exp_row_list)
            print (row)

# Импорт данных в базу данных - вариант со значениями в одну колонку
# def import_data2(struct,delim):
    
#     row_counter ('database.csv')
#     row_counter ('import.csv')

#     with open('database.csv', 'a', newline='') as db_file, open("import.csv",'r') as imp_file:
#         csv_db = csv.writer(db_file)
#         csv_imp = csv.reader(imp_file, delimiter = delim)

#         # формируем список из компонентов import.csv
#         data = []
#         for row in csv_imp:
#             data.append(row)
#         print(data)
       
#         # формируем список из 4 компонентов для переноса в db
#         imp_row_list = []
        
#         for i in data:
#             imp_row_list.append(i)
            
#         print (imp_row_list)   
#         csv_db.writerow(imp_row_list)
            


    

# поиск пустой строки в базе данных
def row_counter(file):
    with open(file, 'r') as op_file:
        count = 0
        csv_file = csv.reader(op_file)
        for i in csv_file:
            count += 1
    print(f' В файле {file} {count} строк')
    return count


# db_delimiter = ","
# out_delimeter = ","

# export_data(db_delimiter,out_delimeter)