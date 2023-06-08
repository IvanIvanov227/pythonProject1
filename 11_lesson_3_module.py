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


def get_user(cursor, ID):
    command = """
    SELECT * FROM users WHERE id == ?;
    """
    result = cursor.execute(command, (ID, ))
    # Все данные возвращает
    users = result.fetchall()
    # Метод fetchone() возвращает первый элемент
    return users


def update_info(cursor, new_name, ID):
    command = """
    UPDATE users SET name = ? WHERE id = ?;
    """
    cursor.execute(command, (new_name, ID))

def select_count(cursor):
    command = """
    SELECT COUNT(*) FROM users;
    """
    res = cursor.execute(command)
    print(res.fetchone())


if __name__ == '__main__':
    with sqlite3.connect('data.db') as cursor:
        create_table(cursor)
        # Удаляет всю таблицу
        delete_table(cursor)
        add_user(cursor, User('Саша', 'Иванов', 'М'))
        add_user(cursor, User('Настя', 'Кузнецова', 'Ж'))
        add_user(cursor, User('Наталья', 'Внукова', 'Ж'))
        print(select_info(cursor))
        print(get_user(cursor, 2))
        update_info(cursor, 'Дарина', 1)
        print(select_info(cursor))
        select_count(cursor)
