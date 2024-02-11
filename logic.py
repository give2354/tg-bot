import sqlite3

DATABASE = 'store.db'

class StoreManager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            # Создание таблицы "одежда"
            conn.execute('''CREATE TABLE IF NOT EXISTS items (
                                item_id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                price INTEGER NOT NULL,
                                color TEXT,
                                img TEXT
                            )''')

            # Создание таблицы "корзина"
            conn.execute('''CREATE TABLE IF NOT EXISTS cart (
                                user_id INTEGER,
                                item_id INTEGER,
                                count INTEGER,
                                FOREIGN KEY(item_id) REFERENCES items(item_id)
                            )''')
            conn.commit()

    def add_items(self, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany("INSERT INTO items (name, price, color, img ) VALUES (?, ?, ?, ?)", data)
            conn.commit()

    def show_items(self):
        conn = sqlite3.connect(self.database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM items")
        result = cur.fetchall()
        return result
        
