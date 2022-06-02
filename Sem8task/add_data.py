
import logger

def students_new_entry():
    id_student = input("Введите id ученика: ")
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    birthday = input("Введите дату рождения: ")
    student_class = input("Введите класс: ")
    id_place = input("Введите id места в кабинете: ")
    status = input("Введите статус: ")
    
    with open('students.csv','a') as file:
        file.write(f'{id_student};{surname};{name};{middle_name};{birthday};{student_class};{id_place};{status}\n')
    
    logger.logger(f"{'students.csv','a'} {id_student};{surname};{name};{middle_name};{birthday};{student_class};{id_place};{status}")


def address_new_entry():
    id_student = input("Введите id ученика: ")
    city = input("Введите город: ")
    street = input("Введите улицу: ")
    house = input("Введите дом: ")
    appartment = input("Введите квартиру: ")
    status = input("Введите статус: ")
    
    with open('address.csv','a') as file:
        file.write(f'{id_student};{city};{street};{house};{appartment};{status}\n')

    logger.logger(f"{'address.csv','a'} {id_student};{city};{street};{house};{appartment};{status}")
# students_new_entry()