
# Показывает базу данных в консоли
import csv
import pandas
import logger

def show_db(csv_show):
    with open(csv_show, encoding = 'UTF-8') as r_file:
        csv = pandas.read_csv (r_file, delimiter = ";")
        print (f'\n{csv}\n')
    logger.logger(show_db)

# show_db('students.csv')