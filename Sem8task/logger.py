
from datetime import datetime
import csv

def logger(mtd):

    with open('log.csv', 'a') as csv_log:

        csv_log.write(f'{datetime.today().strftime("%Y-%m-%d %H:%M:%S")}; {mtd}\n')


