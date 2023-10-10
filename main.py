import sqlite3

from faker import Faker
import random

# Создаем или подключаемся к базе данных
conn = sqlite3.connect('internet_shop.db')
cursor = conn.cursor()

# Создаем таблицу "Сотрудники"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT
    )
''')

# Создаем таблицу "Клиенты"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        email TEXT,
        phone TEXT
    )
''')

# Создаем таблицу "Товары"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        weight INTEGER,
        size INTEGER,
        description TEXT
    )
''')

# Создаем таблицу "Заказы"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        employee_id INTEGER,
        client_id INTEGER,
        order_date DATE,
        delivery_cost INTEGER,
        order_status BOOLEAN,
        FOREIGN KEY (employee_id) REFERENCES employees (id),
        FOREIGN KEY (client_id) REFERENCES clients (id)
    )
''')

# Создаем таблицу "Корзина"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shopping_cart (
        id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (order_id) REFERENCES orders (id),
        FOREIGN KEY (product_id) REFERENCES products (id)
    )
''')
fake = Faker()

# Добавляем 1000 тестовых записей в таблицу "products" (Товары)
for _ in range(1000):
    product_name = fake.word()
    price = random.randint(10, 1000)
    weight = random.randint(1, 100)
    size = random.randint(1, 50)
    description = fake.sentence()

    cursor.execute("INSERT INTO products (name, price, weight, size, description) VALUES (?, ?, ?, ?, ?)",
                   (product_name, price, weight, size, description))

conn.commit()
conn.close()
