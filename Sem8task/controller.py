
import pandas
import find_entry
import show_db
import add_data
import logger


def interface():
    a=0
    
    a=input('\nВведите команду: \n 1 - показать всю базу данных\n 2 - добавить новую запись\n 3 - поиск записи\n ')

    while a!= '1' and a!='2'and a!='3':
        a=input('Введите (1) или (2)!!')
    if a=='1':
        print("\nБаза данных имеет вид \n")
        show_db.show_db('students.csv')
        show_db.show_db('class.csv')
        show_db.show_db('address.csv')
    if a=="2":
        b = input("\nДобавить нового ученика(1) или запись об адресах(2)?\n")
        while b!= '1' and b!='2':
            b = input('Введите 1 или 2!!')
        if b =='1':
            add_data.students_new_entry()
            print("\nБаза данных имеет вид \n")
            show_db.show_db('students.csv')
        if b =='2':
            add_data.address_new_entry()
            print("\nБаза данных имеет вид \n")
            show_db.show_db('address.csv')
    if a=="3":
        word = input("\nВведите значение для поиска в таблице учеников\n")
        logger.logger(f"find_entry ({word})")
        find_entry.find_entry(word)

        

        





