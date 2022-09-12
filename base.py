import sqlite3 as sql

# Функции работы с базой данных

# создание базы и таблицы
def create_table():
    connection = sql.connect('announcement.db')
    with connection:
        cur = connection.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS `announcement` ('id' INTEGER PRIMARY KEY,'heading' TEXT,'description' TEXT, 'date_of_creation' DATETIME,'user_name' TEXT)")
        connection.commit()
        cur.close()

# Заполнение таблицы "Обьявления"
def zapolnenie_table( id,heading, description, date_of_creation,user_name):
    connection = sql.connect('announcement.db')
    with connection:
        cur = connection.cursor()
        cur.execute(f"INSERT INTO 'announcement' VALUES ('{id}','{heading}','{description}','{date_of_creation}','{user_name}')")
        connection.commit()
        cur.close()

# Просмотр данных из таблицы "Обьявления"
answer = {}
def scan_table(id_user):
    connection = sql.connect('announcement.db')
    with connection:
        cur = connection.cursor()
        select_1 = cur.execute(f"SELECT*FROM announcement WHERE id= '{id_user}';")
        select_2 = select_1.fetchone()
        parameter_0 = select_2[0]
        parameter_1 = select_2[1]
        parameter_2 = select_2[2]
        parameter_3 = select_2[3]
        parameter_4 = select_2[4]
        answer.update({ 'id': parameter_0, 'heading': parameter_1, 'description': parameter_2, 'date_of_creation': parameter_3, 'user_name': parameter_4})
        cur.close()


# удаление обьявления из таблицы "Обьявления"
def delete_announcement(id_user):
    connection = sql.connect('announcement.db')
    with connection:
        cur = connection.cursor()
        cur.execute(f"DELETE FROM announcement WHERE id= '{id_user}';")
        connection.commit()
        cur.close()












