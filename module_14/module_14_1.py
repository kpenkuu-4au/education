import sqlite3

connect = sqlite3.connect('not_telegram.db')
cursor = connect.cursor()
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for user in range(1, 11):
    cursor.execute('INSERT INTO Users '
                   '('
                   'username, '
                   'email, '
                   'age, '
                   'balance'
                   ') '
                   'VALUES (?, ?, ?, ?)',
                   (f'User{user}', f'example{user}@gmail.com', f'{user}0', '1000')
                   )

for id in range(1, 11):
    if id % 2 != 0:
        cursor.execute('UPDATE Users SET balance = ? WHERE id = ?',
                       (500, id,))

count = 1
for i in range(1, 11):
    if i == count:
        cursor.execute('DELETE FROM Users WHERE id = ?', (i,))
        count += 3

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))

users = cursor.fetchall()

for user in users:
    print(f'Имя:{user[0]} | Почта:{user[1]} | Возраст:{user[2]} | Баланс:{user[3]}')

connect.commit()
connect.close()
