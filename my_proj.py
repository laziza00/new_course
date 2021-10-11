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
        self. name = None
        self. age = None
        self. login = None
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

        if reg_log == opt[0]:
            self.registration()
        if reg_log == opt[1]:
            self.log_in()


    def registration(self):
        self.clear_everthying()
        input_name = input("Name: ").strip().capitalize()

        while not self.is_string_empty(input_name) or not  input_name.isalpha():
            self.clear_everthying()
            print("Invalid input. Please try again")
            input_name = input("Name: ").strip().capitalize()

        






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
        return bool(str_)



person = Project()
person.entering_the_system()





















