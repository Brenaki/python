import mysql.connector

class Database():

    def connect_bd():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database='system_'
        )

        return mydb

    def disconnect_bd(connection):
        connection.close()

    def find_users(connection, username):
        mycursor = connection.cursor()
        mycursor.execute("USE system_")
        mycursor.execute(f"SELECT * FROM login where user = '{username}';")
        find = mycursor.fetchall()
        mycursor.close()
        return find

    def insert_user(connection, user, password):
        mycursor = connection.cursor()
        mycursor.execute(f"INSERT INTO `system_`.`Login` (`User`, `Password`) VALUES ('{user}', '{password}');")
        connection.commit()
        mycursor.close()
        return 