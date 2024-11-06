import sqlite3


def initiate_db():
    connect = sqlite3.connect('Products.db')
    cursor = connect.cursor()
    cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS Products(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
                        )
                    ''')
    connect.commit()
    connect.close()


def get_all_products():
    connect = sqlite3.connect('Products.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Products")
    table = cursor.fetchall()
    connect.commit()
    connect.close()
    return table

# Создание таблицы:

# initiate_db()
# for prod in range(1, 5):
#     connect = sqlite3.connect('Products.db')
#     cursor = connect.cursor()
#     cursor.execute(
#         'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
#         (f'Продукт {prod}', f'Описание {prod}', f'{prod * 100}')
#     )
#     connect.commit()
#     connect.close()


def initiate_users_db():
    connect = sqlite3.connect('Users.db')
    cursor = connect.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
                        )
                    ''')
    connect.commit()
    connect.close()


def add_user(username, email, age):
    connect = sqlite3.connect('Users.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO Users '
                   '('
                   'username, '
                   'email, '
                   'age, '
                   'balance'
                   ') '
                   'VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', '1000')
                   )
    connect.commit()
    connect.close()


def is_included(username):
    connect = sqlite3.connect('Users.db')
    cursor = connect.cursor()
    cursor.execute('SELECT username FROM Users WHERE username = ?', (f'{username}',))
    found_user = cursor.fetchone()
    connect.commit()
    connect.close()
    if found_user is None:
        return False
    else:
        return True
