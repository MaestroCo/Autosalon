import csv

from data_base import database

# Komandalar
kommanda = {'csv': 'Tableni .csv faylda saqlaydi', 'buy': 'Avtomobil sotib olish', 'commands': 'Buyruqlarni ekranga chiqaradi', 'back': 'Orqaga qaytish',
            'add brand': 'Yangi brend qo\'shish', 'show brands': 'Brendlar ro\'yxatini ko\'rish',
            'del brand': 'Brendni o\'chirish', 'add model': 'Yangi model qo\'shish',
            'show models': 'Modellar ro\'yxatini ko\'rish', 'del model': 'Modelni o\'chirish',
            'show employees': 'Employee ro\'yxatini ko\'rish', 'add employee': 'Yangi employee qo\'shish',
            'del employee': 'Employeeni o\'chirish', 'show customers': 'Xaridorlar ro\'yxatini ko\'rish',
            'add customer': 'Yangi Customer qo\'shish', 'del customer': 'Customerni o\'chirish',
            'show orders': 'Xaridorlar ro\'yxatini ko\'rish', 'del order': 'Xaridorni ro\'yxatdan o\'chirish'}


def commands():
    print("\033[031mKomandalar bilan tanishing: \033[0m")
    print(f"\033[035m{('Komandalar').center(16, ' ')}\033[0m | \033[035m {('Vazifasi').center(16, ' ')}\033[0m")
    for i, y in kommanda.items():
        print(f"\033[032m{str(i).center(16, ' ')}\033[0m | \033[033m{str(y).center(16, ' ')}\033[0m")
commands()

# ======================================== Brends Table uchun yozilgan kod qismi =================================
# Yangi Brend qo'shish
def add_brands():
    count = 0
    yangi_b = int(input("Nechta yangi avtomobil brendini kiritmoqchisiz?: "))
    if yangi_b == 'back':
        commands()
        print("Ortga qaytildi")
        return
    else:
        while count < yangi_b:
            count += 1
            brand = input(f"{count}- yangi kelgan avtomobil brandi nomini kiriting: ")
            if brand == 'back':
                commands()
                print('Ortga qaytildi')
                return
            else:
                try:
                    database.add_tabe_brands(brand)
                except Exception as e:
                    print(f"\033[031mXatolik yuz berdi! \033[032m{brand}\033[0m\033[031m avtomobili ro'yxatda mavjud bo'lsa kerak (show brands) buyrug'i orqali "
                          f"tekshirib ko'ring.\033[0m")
        print("Avtomobil brendini qo'shish yakunlandi!")


# Brendlar ro'yxatini ko'rsatish
def show_brands():
    print("\033[031mAvtosalonda mavjud avtomobil brendlari:\033[0m")
    brand = database.show_table_brands()
    print('|', '\033[035m', "ID".center(8,' '),'\033[0m|', '\033[035m', 'Brand Name'.center(14, ' '), '\033[0m', '|')
    for i in brand:
        print("|\033[032m", str(i[0]).center(9,' '), "\033[0m|\033[033m", str(i[1]).center(16, ' '), '\033[0m|')

# Keraksiz Brendni o'chirish
def delete_brand():
    show_brands()
    input_del = input("O'chirmoqchi bo'lgan brand nomini kiriting: ")
    if input_del == 'back':
        commands()
        print("Ortga qaytildi")
        return
    else:
        database.del_table_brands(input_del)
        print(f"{input_del} brendi ro'yxatdan o'chirildi!")

# ======================================== Models Table uchun yozilgan kod qismi =================================

def add_models():
    count = 0
    yangi_m = int(input("Nechta yangi model kiritmoqchisiz?: "))
    if yangi_m == 'back':
        commands()
        print("Ortga qaytildi!")
        return
    else:
        while count < yangi_m:
            count += 1
            try:
                print('\033[031m', 'Ogohlantirish! Ushbu qismda (back-ortga qaytish) buyrug\'i ishlamaydi iltimos ohirigacha to\'ldiring. \033[0m')
                model = input(f"{count}. Ro'yxatga qo'shmoqchi bo'lgan yangi modelni yozing: ")
                show_brands()
                brand = int(input(f"Yuqoridagi ro'yxatdan {model} brendini ID sini kiriting: "))
                color = input("Rangini kiriting: ")
                dvigatel = input("Dvigatel hajmini kiriting (Misol: 1.6 litr): ")
                price = int(input("Narxini kiriting: "))
                database.add_table_models(model, brand, color, dvigatel, price)
            except Exception as e:
                print(
                    f"\033[031mXatolik yuz berdi! \033[032m{model}\033[0m\033[031m avtomobili ro'yxatda mavjud bo'lsa kerak (show models) buyrug'i orqali "
                    f"tekshirib ko'ring.\033[0m")
        print("Yangi avtomobil kiritish yakunlandi!")

def show_models():
    print(f"\033[031mAvtosalonda mavjud avtomobil modellari ro'yxati: \033[0m")
    show = database.show_table_models()
    print('|', '\033[035m', "ID".center(8, ' '), '\033[0m|', '\033[035m',
          'Name'.center(14, ' '), '\033[0m|', '\033[035m', 'Brand'.center(11, ' '), '\033[0m|',
          '\033[035m', 'Color'.center(14, ' '), '\033[0m|\033[035m', 'Engine'.center(10, ' '), '\033[0m|',
          '\033[035m', 'Price'.center(15, ' '), '\033[0m|')
    for i in show:
        print("|\033[032m", str(i[0]).center(9, ' '), "\033[0m"
              "|\033[033m", str(i[1]).center(15, ' '), '\033[0m|\033[034m', str(i[2]).center(12, ' '),
              '\033[0m|\033[036m', str(i[3]).center(15, ' '),
              '\033[0m|\033[035m', str(i[4]).center(10, ' '), '\033[0m|\033[037m', str(i[5]).center(16, ' '),
              '\033[0m|')

def delete_model():
    show_models()
    del_model = input("O'chirmochi bo'lgan model ID sini kiriting: ")
    if del_model == 'back':
        commands()
        return
    else:
        database.del_table_models(del_model)
        print(f"{del_model} avtomobili MODELS ro'yxatidan o'chirildi!")

# ============================ Employee table uchun yozilgan kod qismi ===============================

def add_employee():
    count = 0
    son = int(input('Nechta yangi employee kiritmoqchisiz?: '))
    if son == 'back':
        commands()
        print("Ortga qaytildi")
        return
    else:
        print('\033[031m', 'Ogohlantirish! Ushbu qismda (back-ortga qaytish) buyrug\'i ishlamaydi iltimos ohirigacha'
                           'to\'ldiring. \033[0m')
        while count < son:
            count += 1
            try:
                name = input(f"{count}. Yangi hodimning ismini kiriting: ")
                lastname = input(f"{name}ning familiyasini kiriting: ")
                phone = input(f"{name} {lastname}ning telefon raqamini kiriting kiriting: ")
                address = input(f"{name} {lastname}ning mazilini kiriting kiriting: ")
                email = input(f"{name} {lastname}ning emailini kiriting kiriting: ")
                birthdate = input(f"{name} {lastname}ning tug'ilgan sanasini kiriting kiriting: ")
                database.add_table_employee(name, lastname, phone, address, email, birthdate)
            except:
                print(
                    f"\033[031mXatolik yuz berdi! Boshqatdan urinib ko'ring.\033[0m")
        print("Yangi xodim kiritish yakunlandi!")

def show_employee():
    print(f"\033[031mAvtosalonda ishlovchi hodimlar ro'yxati: \033[0m")
    show_employee1 = database.show_table_employee()
    print('|', '\033[035m', "ID".center(8, ' '), '\033[0m|', '\033[035m',
          'Name'.center(14, ' '), '\033[0m|', '\033[035m', 'Lastname'.center(15, ' '), '\033[0m|',
          '\033[035m', 'Phone'.center(14, ' '), '\033[0m|', '\033[035m',
          'Address'.center(14, ' '), '\033[0m|\033[035m', 'Email'.center(25, ' '), '\033[0m|\033[035m',
          'Birthdate'.center(12, ' '), '\033[0m|')
    for i in show_employee1:
        print('|', '\033[032m', str(i[0]).center(8, ' '), '\033[0m|', '\033[033m',
              str(i[1]).center(14, ' '), '\033[0m|', '\033[034m', str(i[2]).center(15, ' '), '\033[0m|',
              str(i[3]).center(15, ' '), '\033[0m|\033[036m', str(i[4]).center(15, ' '), '\033[0m|\033[037m',
              str(i[5]).center(25, ' '), '\033[0m|\033[032m', str(i[6]).center(12, ' '), '\033[0m|')
def del_employee():
    show_employee()
    del_employee = input("O'chirmochi bo'lgan hodim ID sini kiriting: ")
    if del_employee == 'back':
        commands()
        return
    else:
        database.delete_table_employee(del_employee)
        print(f"{del_employee} ID dagi hodim EMPLOYEE ro'yxatidan o'chirildi!")

# ============================ Customers table uchun yozilgan kod qismi ===============================

def add_customers():
    count = 0
    son = int(input('Nechta yangi customer kiritmoqchisiz?: '))
    if son == 'back':
        commands()
        print("Ortga qaytildi")
        return
    else:
        print('\033[031m', 'Ogohlantirish! Ushbu qismda (back-ortga qaytish) buyrug\'i ishlamaydi iltimos ohirigacha'
                           'to\'ldiring. \033[0m')
        while count < son:
            count += 1
            try:
                name = input(f"{count}. Yangi xaridorning ismini kiriting: ")
                lastname = input(f"{name}ning familiyasini kiriting: ")
                phone = input(f"{name} {lastname}ning telefon raqamini kiriting kiriting: ")
                address = input(f"{name} {lastname}ning mazilini kiriting kiriting: ")
                database.add_table_customers(name, lastname, phone, address)
            except Exception as e:
                print(
                    f"\033[031mXatolik yuz berdi! Boshqatdan urinib ko'ring.\033[0m {e}")
        print("Yangi xodim kiritish yakunlandi!")

def show_customers():
    print(f"\033[031mAvtosalon xaridorlari ro'yxati: \033[0m")
    show_customers = database.show_table_customers()
    print('|', '\033[035m', "ID".center(8, ' '), '\033[0m|', '\033[035m',
          'Name'.center(14, ' '), '\033[0m|', '\033[035m', 'Lastname'.center(15, ' '), '\033[0m|',
          '\033[035m', 'Phone'.center(14, ' '), '\033[0m|', '\033[035m',
          'Address'.center(14, ' '), '\033[0m|')
    for i in show_customers:
        print('|', '\033[032m', str(i[0]).center(8, ' '), '\033[0m|', '\033[033m',
              str(i[1]).center(14, ' '), '\033[0m|', '\033[034m', str(i[2]).center(15, ' '), '\033[0m|',
              str(i[3]).center(15, ' '), '\033[0m|\033[035m', str(i[4]).center(15, ' '), '\033[0m|')

def del_customer():
    show_customers()
    del_customer = input("O'chirmochi bo'lgan hodim ID sini kiriting: ")
    if del_customer == 'back':
        commands()
        return
    else:
        database.del_table_customers(del_customer)
        print(f"{del_customer} ID dagi xarifor CUSTOMERS ro'yxatidan o'chirildi!")

# ============================ Orders table uchun yozilgan kod qismi ===============================
def add_buy():
    customer_name = input("Mijozning ismi: ")
    customer_lastname = input("Mijozning familiyasi: ")
    customer_phone = input("Mijozning telefon raqami: ")
    customer_address = input("Mijozning  manzili: ")
    show_employee()
    service_employee = int(input("Xizmat ko'rsatgan hodim ID sini kiritng: "))
    # Mijozni qo'shish
    database.add_table_customers(customer_name, customer_lastname, customer_phone, customer_address)
    show_models()
    model_id = input("Sotib olish uchun avtomobil model id sini kiriting: ")
    purchase_date = input("Sotib olingan sana (sana: dd.mm.yyyy): ")

    # Avtomobilni sotib olish
    database.add_table_order(customer_name, customer_lastname, model_id, customer_address, purchase_date, service_employee)
    # database.del_table_models(model_id)
    print("Avtomobil sotib olindi!")

def show_orders():
    print(f"\033[031mAvtosalonda sotilgan avtomobillar ro'yxati: \033[0m")
    show_orders = database.show_table_order()
    print('|', '\033[035m', "ID".center(8, ' '), '\033[0m|', '\033[035m',
          'Name'.center(14, ' '), '\033[0m|', '\033[035m', 'Lastname'.center(15, ' '), '\033[0m|',
          '\033[035m', 'Model'.center(14, ' '), '\033[0m|', '\033[035m',
          'Date'.center(14, ' '), '\033[0m|\033[035m', 'Address'.center(15, ' '), '\033[0m|\033[035m',
          'Employee'.center(15, ' '), '\033[0m|')
    for i in show_orders:
        print('|', '\033[032m', str(i[0]).center(8, ' '), '\033[0m|', '\033[033m',
              str(i[1]).center(14, ' '), '\033[0m|', '\033[034m', str(i[2]).center(15, ' '), '\033[0m|',
              '\033[035m', str(i[3]).center(14, ' '), '\033[0m|', '\033[036m',
              str(i[4]).center(14, ' '), '\033[0m|\033[037m', str(i[5]).center(15, ' '), '\033[0m|\033[0m',
              str(i[6]).center(15, ' '), '\033[0m|')
def del_order():
    show_orders()
    del_orders = input("O'chirmochi bo'lgan mijoz ID sini kiriting: ")
    if del_customer == 'back':
        commands()
        return
    else:
        database.del_table_order(del_orders)
        print(f"{del_orders} ID dagi mijoz ORDERS ro'yxatidan o'chirildi!")

def export_to_csv_models():
    with open('model_data.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Model ID', 'Model Name', 'Brand Name', 'Color', 'Engine Capacity', 'Price'])
        csv_writer.writerows(database.show_table_models())
    print(f"Models jadvali ma'lumotlari CSV faylga muvaffaqiyatli yozildi!")

def export_to_csv_orders():
    with open('orders_data.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['ID', 'Name', 'Last Name', 'Model', 'Date', 'Address', 'Employee'])
        csv_writer.writerows(database.show_table_order())
    print(f"Orders jadvali ma'lumotlari CSV faylga muvaffaqiyatli yozildi!")

def export_to_csv_customers():
    with open('customers_data.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['ID', 'Name', 'Last Name', 'Phone', 'Address'])
        csv_writer.writerows(database.show_table_customers())
    print(f"Customers jadvali ma'lumotlari CSV faylga muvaffaqiyatli yozildi!")

def export_to_csv_employees():
    with open('employees_data.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['ID', 'Name', 'Last Name', 'Phone', 'Address', 'Email', 'Birthdate'])
        csv_writer.writerows(database.show_table_employee())
    print(f"Employees jadvali ma'lumotlari CSV faylga muvaffaqiyatli yozildi!")

def export_to_csv_brands():
    with open('model_data.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['ID', 'Brand Name'])
        csv_writer.writerows(database.show_table_brands())
    print(f"Brands jadvali ma'lumotlari CSV faylga muvaffaqiyatli yozildi!")