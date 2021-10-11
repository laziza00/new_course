import getpass
import os

import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="lazii",
        passwd="123456789",
        database="Users",
        auth_plugin='mysql_native_password',
)
# mycursor = mydb.cursor()
# mycursor.execute("create table kurs_ishi (id int unsigned auto_increment primary key, name varchar(20) not null, age int (3) not null, login varchar(20) not null , password varchar(20) not null)")

class Project:
    def __init__(self):
        self.name = None
        self.age = None
        self.login = None
        self.password = None
        self.options = ["1", "2", "3", "4"]

    def entering_the_system(self):
        opt = ["1", "2"]
        self.initial_message()
        reg_log = input("Enter [1/2]>>>: ")
        while reg_log not in opt:
            self.clear_everthying()
            print("Invalid input. Please selcet one of options below")
            reg_log = input("Enter [1/2]>>>: ")
        self.clear_everthying()
        if reg_log == opt[0]:
            self.registration()
        if reg_log == opt[1]:
            self.log_in()


    def registration(self):
        self.clear_everthying()
        input_name = input("Name: ").strip().capitalize()

        while self.is_string_empty(input_name) or not input_name.isalpha():
            self.clear_everthying()
            print("Invalid input. Please try again")
            input_name = input("Name: ").strip().capitalize()

        input_age = input("Age: ").strip()
        while self.is_string_empty(input_age) or not input_age.isnumeric():
            self.clear_everthying()
            print("Invalid input. Please try again")
            input_age = input("Age: ").strip()

        input_login = input("Login: ").strip().lower()
        while self.is_string_empty(input_login) or not input_login.isalnum() and self.user_exsists(input_login):
            self.clear_everthying()
            print("""Invalid input. Posibble errors
                     You have entered an empty password
                     Pasword don't match
                """)
            input_login = input("Login: ").strip().lower()

        input_password = getpass.getpass("Password: ").strip()
        check_password = getpass.getpass("Check password: ").strip()

        while self.is_string_empty(input_password) and input_password != check_password or not input_password.isalnum():
            self.clear_everthying()
            print("Invalid input. Please try again")
            input_password = getpass.getpass("Password: ").strip()
            check.password = getpass.getpass("Check password: ").strip()



        self.add_class(input_name, input_age, input_login, input_password)


    def add_class(self, input_name, input_age, input_login, input_password):
        self.name = input_name
        self.age = input_age
        self.login = input_login
        self.password = input_password

    def log_in(self):
        print("""You are welcome
                 [1] - Update login
                 [2] - Update password
                 [3] - Delete account 
                 [4] - Log out   
            """)
    def update_login(self):
        pass
    def update_password(self):
        pass
    def delete_account(self):
        pass
    def log_out(self):
        pass
    def initial_message(self):
        print("""Entering the system
                 [1] - Registr
                 [2] - Login  
              """)


    def clear_everthying(self):
        os.system("clear")

    def is_string_empty(self, str_):
        return  not bool(str_)

    def user_exsists(self, input_login):
        mycursor = mydb.cursor()
        mycursor.execute(f"select login from kurs_ishi where login = '{input_login}'")
        all_data = mycursor.fetchall()
        if all_data:
            return True
        else:
            return False
    def write_database(self):
        pass


person = Project()
person.entering_the_system()





















