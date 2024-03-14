import sqlite3
import csv
class DataBase:
    def __init__(self, create_a_db='database.db'):
        self.create_a_db = create_a_db

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = sqlite3.connect(self.create_a_db)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

# ============================ Brand table uchun yozilgan kod qismi ===============================
    # Brands nomli table yaratib olish
    def create_table_brands(self):
        sql = '''CREATE TABLE IF NOT EXISTS brands(
            brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand_name VARCHAR(15) UNIQUE
        )'''
        self.execute(sql, commit=True)

    def add_table_brands_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                brand_name = line.strip()
                self.add_tabe_brands(brand_name)

    # Brands jadvaliga malumot qo'shish funksiyasi
    def add_tabe_brands(self, brand_name):
        sql = '''INSERT INTO brands(BRAND_NAME) VALUES (?)'''
        self.execute(sql, parameters=(brand_name,), commit=True)

    # Brands jadvalini ko'rsatuvchi funksiya
    def show_table_brands(self):
        sql = '''SELECT * FROM brands'''
        return self.execute(sql, fetchall=True)

    def del_table_brands(self, brand_name):
        sql = '''DELETE FROM brands WHERE brand_name = ?'''
        self.execute(sql, parameters=(brand_name,), commit=True)

# ============================ Models table uchun yozilgan kod qismi ===============================
    # Model nomli table yaratish
    def create_table_models(self):
        sql = '''CREATE TABLE IF NOT EXISTS models(
            model_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT UNIQUE NOT NULL,
            model_brand INTEGER REFERENCES brands(brand_id),
            model_color TEXT NOT NULL,
            engine_capacity TEXT NOT NULL,
            model_price INTEGER NOT NULL
        )'''
        self.execute(sql, commit=True)

    # Models jadvaliga malumot qo'shish funksiyasi
    def add_table_models(self, model_name, model_brand, model_color, engine_capacity, model_price):
        sql = '''INSERT INTO models(model_name, model_brand, model_color, engine_capacity, model_price) 
        VALUES (?, ?, ?, ?, ?)'''
        self.execute(sql, parameters=(model_name, model_brand, model_color, engine_capacity, model_price), commit=True)

    def add_table_model_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 5:
                    model, brand, color, engine, price = data
                    try:
                        # Ma'lumotlar bazasiga qo'shish
                        self.add_table_models(model, brand, color, engine, price)
                    except Exception as e:
                        print(f"Xatolik yuz berdi! {model} ma'lumotlar bazasiga qo'shilmadi. Xabar: {e}")
                else:
                    print(
                        f"Qatorda noto'g'ri ma'lumotlar mavjud. Qatorda 6 ta ma'lumot bo'lishi kerak. Qatorda {len(data)} ta ma'lumot mavjud.")

    # Models jadvalidagi ma'lumotlarni ko'rish funksiyasi
    def show_table_models(self):
        sql = '''SELECT model_id, model_name, brands.brand_name, model_color, engine_capacity, model_price 
        FROM models JOIN brands ON models.model_brand = brands.brand_id'''
        return self.execute(sql, fetchall=True)

    def del_table_models(self, model_id):
        sql = '''DELETE FROM models WHERE model_id = ?'''
        self.execute(sql, parameters=(model_id,), commit=True)

# ============================ Employee table uchun yozilgan kod qismi ===============================
    # Employee mnomli table yaratish
    def create_table_employee(self):
        sql = '''CREATE TABLE IF NOT EXISTS employee(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            lastname TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            email TEXT NOT NULL,
            birthdate TEXT NOT NULL
        )'''
        self.execute(sql, commit=True)

    # Employee ga ma'lumot qo'shish
    def add_table_employee(self, name, lastname, phone, address, email, birthdate):
        sql = '''INSERT INTO employee(name, lastname, phone, address, email, birthdate)
        VALUES (?,?,?,?,?,?)'''
        self.execute(sql, parameters=(name, lastname, phone, address, email, birthdate), commit=True)

    def add_table_employee_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 6:
                    name, lastname, phone, address, email, birthdate = data
                    try:
                        # Ma'lumotlar bazasiga qo'shish
                        self.add_table_employee(name, lastname, phone, address, email, birthdate)
                    except Exception as e:
                        print(f"Xatolik yuz berdi! {name} {lastname} ma'lumotlar bazasiga qo'shilmadi. Xabar: {e}")
                else:
                    print(
                        f"Qatorda noto'g'ri ma'lumotlar mavjud. Qatorda 6 ta ma'lumot bo'lishi kerak. Qatorda {len(data)} ta ma'lumot mavjud.")

    def show_table_employee(self):
        sql = '''SELECT * FROM employee'''
        return self.execute(sql, fetchall=True)

    def delete_table_employee(self, id):
        sql = '''DELETE FROM employee WHERE id = ?'''
        self.execute(sql, parameters=(id,), commit=True)

# ============================ Customer table uchun yozilgan kod qismi ===============================
    # Mijozlar nomli table yaratish
    def create_table_customers(self):
        sql = '''CREATE TABLE IF NOT EXISTS customers(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            customer_lastname TEXT NOT NULL,
            customer_phone TEXT NOT NULL,
            customer_address TEXT NOT NULL
        )'''
        self.execute(sql, commit=True)

    # Mijoz qo'shish funksiyasi
    def add_table_customers(self, customer_name, customer_lastname, customer_phone, customer_address):
        sql = '''INSERT INTO customers(customer_name, customer_lastname, customer_phone, customer_address)
        VALUES (?,?,?,?)'''
        self.execute(sql, parameters=(customer_name, customer_lastname, customer_phone, customer_address), commit=True)

    # Mijozlarni ko'rish funksiyasi
    def show_table_customers(self):
        sql = '''SELECT * FROM customers'''
        return self.execute(sql, fetchall=True)

    def del_table_customers(self, customer_id):
        sql = '''DELETE FROM customers WHERE customer_id = ?'''
        self.execute(sql, parameters=(customer_id,), commit=True)

# ============================ Orders table uchun yozilgan kod qismi ===============================
    # Avtomobil sotib olish nomli table yaratish
    def create_table_orders(self):
        sql = '''CREATE TABLE IF NOT EXISTS orders(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_name TEXT NOT NULL,
            order_lastname TEXT NOT NULL,
            order_model INTEGER REFERENCES models(model_id),
            order_address TEXT NOT NULL,
            order_date TEXT NOT NULL,
            service_employee INTEGER REFERENCES employee(id)
        )'''
        self.execute(sql, commit=True)

    def add_table_order(self, order_name, order_lastname, order_model, order_address, order_date, service_employee):
        sql = '''INSERT INTO orders(order_name, order_lastname, order_model, order_address, order_date, service_employee)
        VALUES (?,?,?,?,?,?)'''
        self.execute(sql, parameters=(order_name, order_lastname, order_model, order_address, order_date, service_employee,), commit=True)

    def show_table_order(self):
        sql = '''SELECT orders.order_id, orders.order_name, orders.order_lastname, 
                models.model_name, 
                orders.order_date, orders.order_address, employee.name FROM orders 
                JOIN models ON orders.order_model = models.model_id 
                JOIN employee ON orders.service_employee = employee.id'''
        return self.execute(sql, fetchall=True)

    def del_table_order(self, order_id):
        sql = '''DELETE FROM orders WHERE order_id = ?'''
        self.execute(sql, parameters=(order_id,), commit=True)

database = DataBase()