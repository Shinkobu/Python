import controller as c


ch = int(input("Что нужно сделать? Показать базу данных - 1, Импортировать данные - 2, Экспортировать данные - 3\n"))

if ch == 1:
    c.show_db()
if ch == 2:
    out_delimeter = input("Укажите разделитель данных в файле импорта (например , или ;)\n")
    c.import_data(out_delimeter)
if ch == 3:
    out_delimeter = input("Укажите разделитель данных в файле экспорта (например , или ;)\n")
    db_delimiter = ","
    c.export_data(db_delimiter,out_delimeter)







