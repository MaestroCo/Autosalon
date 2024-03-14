from data_base import database
from command_functions import (commands, add_models, add_brands, show_models, show_brands, delete_brand, delete_model,
                               show_employee, add_employee, del_employee, show_customers, add_customers, del_customer,
                               add_buy, show_orders, del_order, export_to_csv_models, export_to_csv_brands,
                               export_to_csv_orders, export_to_csv_customers, export_to_csv_employees)

database.create_table_brands()
database.create_table_models()
database.create_table_employee()
database.create_table_customers()
database.create_table_orders()

# ================== ISHLATILMASIN =====================
'''Qachonki (database.db) fayli bo'lmasa keyin yoqib ishlatilad va bir martta ishlatilganidan 
so'ng yana o'chirib qo'yiladi. '''
# database.add_table_model_from_file('model_data.txt')
# database.add_table_brands_from_file('brands_data.txt')
# database.add_table_employee_from_file('employee_data.txt')
'''database.db fayli yaratib olingandan keyin o'chirib qo'yish shart!'''
# ================== ISHLATILMASIN =====================

def run():
    while True:
        command = input("Nima qilmoqchisiz? : ").lower()
        if command == 'add brand':
            add_brands()

        if command == 'csv':
            print('Models, Orders, Customers, Employees, Brands')
            fayl = input("Qaysi ro'yxatni .csv qilib saqlamoqchisiz?: ").lower()
            if fayl == 'models':
                export_to_csv_models()
            elif fayl == 'orders':
                export_to_csv_orders()
            elif fayl == 'customers':
                export_to_csv_customers()
            elif fayl == 'employees':
                export_to_csv_employees()
            elif fayl == 'brands':
                export_to_csv_brands()
            else:
                print(f"{fayl} bunday table mavjud emas!")

        if command == 'del brand':
            delete_brand()

        if command == 'show brands':
            show_brands()

        if command == 'add model':
            add_models()

        if command == 'show models':
            show_models()

        if command == 'del model':
            delete_model()

        if command == 'commands':
            commands()

        if command == 'show employees':
            show_employee()

        if command == 'add employee':
            add_employee()

        if command == 'del employee':
            del_employee()

        if command == 'show customers':
            show_customers()

        if command == 'add customer':
            add_customers()

        if command == 'del customer':
            del_customer()

        if command == 'show orders':
            show_orders()

        if command == 'buy':
            add_buy()

        if command == 'del order':
            del_order()


        if command == 'stop':
            break



if __name__ == '__main__':
    run()