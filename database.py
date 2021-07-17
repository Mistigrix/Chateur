import sqlite3


class DataBase:
    """Classe gerant toute la base de donnée"""

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def check_member(self, username, password):
        user_data = (username, password)
        self.cursor.execute("select * from users where name = ? and password = ?", user_data)

        user = self.cursor.fetchone()

        if user:
            return {
                'username':user[1],
                'password': user[2]
            }
        return None

    def create_user(self, username, password):
        new_user = (self.cursor.lastrowid, username, password)
        self.cursor.execute("insert into users values(?,?,?)", new_user)
        self.connection.commit()

        return {
            'username': username,
            'password': password
        }

    def close(self):
        self.connection.close()
