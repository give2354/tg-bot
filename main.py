import sqlite3

conn = sqlite3.connect('my_database.db')
conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )''')
conn.execute("INSERT INTO orders (user_id, product) VALUES (?, ?)", (2, "Banana"))
conn.execute('''CREATE TABLE IF NOT EXISTS orders (
                    order_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    product TEXT NOT NULL,
										FOREIGN KEY(user_id) REFERENCES users(user_id)
                )''')

data = [
    ("Bob", 30),
    ("Alice", 25)
    ]

conn.executemany("INSERT INTO users (name, age) VALUES (?, ?)", data)
conn.commit()
conn.close()