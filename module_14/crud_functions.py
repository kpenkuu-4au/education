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
