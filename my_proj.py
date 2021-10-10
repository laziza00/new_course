import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="lazii",
        passwd="123456789",
        database="Users",
        auth_plugin='mysql_native_password',
)
mycursor = mydb.cursor()
mycursor.execute("create table kurs_ishi (id int unsigned auto_increment primary key, name varchar(20) not null, age int (3) not null, login varchar(20) not null , password varchar(20) not null)")

