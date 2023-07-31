from acessBD import Database

connection = Database.connect_bd()

class System():
    def login(user):
        log = Database.find_users(connection, user)
        if log[0][1] == user:
            Database.disconnect_bd(connection)
            return True
        Database.disconnect_bd(connection)
        return False
    
    def sign_in(user, password):
        # Create ID
        signin = Database.find_users(connection, user)
        if len(signin) == 0:
            Database.insert_user(connection, user, password)
            Database.disconnect_bd(connection)
            return True
        Database.disconnect_bd(connection)
        return False