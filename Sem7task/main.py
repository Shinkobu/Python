import controller as c


ch = int(input("\nЧто нужно сделать?\n\n Показать базу данных - 1\n Импортировать данные - 2\n Экспортировать данные - 3\n Ввести новую запись вручную - 4\n\n"))

if ch == 1:
    c.show_db()
if ch == 2:
    out_delimeter = input("Укажите разделитель данных в файле импорта (например , или ;)\n")
    c.import_data(out_delimeter)
if ch == 3:
    out_delimeter = input("Укажите разделитель данных в файле экспорта (например , или ;)\n")
    db_delimiter = ","
    c.export_data(db_delimiter,out_delimeter)
if ch == 4:
    db_delimeter = ','
    temp = c.manual_input()
    print(temp)
    c.save(temp[0], temp[1], temp[2], temp[3])








