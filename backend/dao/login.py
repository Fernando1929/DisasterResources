from config.dbconfig import pg_config
import psycopg2

class LoginDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # login = login_id, user_id, username, password

    def getLoginById(self, login_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Login WHERE login_id = %s;"
        cursor.execute(query, (login_id))
        result = cursor.fetchone()
        return result

    def getLoginByUsername(self, username):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Login WHERE username = %s;"
        cursor.execute(query, (username))
        result = cursor.fetchone()
        return result

    def getLoginByPassword(self, password):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Login WHERE password = %s;"
        cursor.execute(query, (password))
        result = cursor.fetchone()
        return result

    def getLoginByUsernameAndPassword(self, username, password):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Login WHERE username = %s AND password = %s;"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        return result

    def getLoginByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM login WHERE user_id = %s;"
        cursor.execute(query, (user_id))
        result = cursor.fetchone()
        return result

    def insert(self, user_id, username, password):
        cursor = self.conn.cursor()
        query = "INSERT INTO login (user_id, username, password) VALUES (%s, %s, %s) RETURNING login_id;"
        cursor.execute(query, (user_id, username, password))
        login_id = cursor.fetchone()[0]
        self.conn.commit()
        return login_id

    def delete(self, login_id):
        return login_id

    def update(self, login_id, user_id, username, password):
        return login_id