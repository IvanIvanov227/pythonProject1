import sqlite3


class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


def create_table(cursor):
    command = """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                gender TEXT);
            """
    cursor.execute(command)


def add_user(cursor, user):
    # Вопросы означают, что сюда нужно будет что-то вставить
    command = """
    INSERT INTO users (name, surname, gender) VALUES (?, ?, ?);
    """
    cursor.execute(command, (user.name, user.surname, user.gender))


def select_info(cursor):
    command = """
    SELECT * FROM users;
    """
    result = cursor.execute(command)
    # Все данные возвращает
    users = result.fetchall()
    # Метод fetchone() возвращает первый элемент
    return users


def delete_table(cursor):
    command = """
    DELETE FROM users;
    """
    cursor.execute(command)


def delete_table_id(cursor, ID):
    command = """
    DELETE FROM users WHERE id = ?;
    """
    cursor.execute(command, (ID, ))


def get_user(cursor, ID):
    command = """
    SELECT * FROM users WHERE id == ?;
    """
    result = cursor.execute(command, (ID, ))
    # Все данные возвращает
    users = result.fetchall()
    # Метод fetchone() возвращает первый элемент
    return users


def update_info(cursor, new_name, new_surname, gender, ID):
    command = """
    UPDATE users SET name = ?, surname = ?, gender = ? WHERE id = ?;
    """
    cursor.execute(command, (new_name, new_surname, gender, ID))


def select_count(cursor):
    command = """
    SELECT COUNT(*) FROM users;
    """
    res = cursor.execute(command)
    return res.fetchone()


def select_workers_gender(cursor):
    command = """
    SELECT * FROM users WHERE gender = ?;
    """
    gender_m = cursor.execute(command, ('М', )).fetchall()
    gender_w = cursor.execute(command, ('Ж', )).fetchall()
    return [gender_m, gender_w]


if __name__ == '__main__':
    with sqlite3.connect('data2.db') as cursor:
        create_table(cursor)
        # Удаляет всю таблицу
        delete_table(cursor)
        add_user(cursor, User('Саша', 'Иванов', 'М'))
        add_user(cursor, User('Настя', 'Кузнецова', 'Ж'))
        add_user(cursor, User('Наталья', 'Внукова', 'Ж'))
        print(select_info(cursor))
        print(get_user(cursor, 2))
        update_info(cursor, 'Михаил', 'Торопыжкин', 'М', 1)
        print(select_info(cursor))
        print(select_count(cursor))
        delete_table_id(cursor, 2)
        add_user(cursor, User('Владислав', 'Ильиных', 'М'))
        print(select_workers_gender(cursor))