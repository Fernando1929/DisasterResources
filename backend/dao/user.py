from config.dbconfig import pg_config
import psycopg2

class UserDAO:
    def _init_(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getUserById(self, user_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM users WHERE user_id = %s;"
        cursor.execute(query, (user_id))
        result = cursor.fetchone()
        # result = [1, "Alex", "Smith", "03/03/1996", "alexsmith@gmail.com", "7870007777"]
        return result

    def insert(self, firstname, lastname, date_birth, email, phone):
        cursor = self.conn.cursor()
        query = "INSERT INTO users (user_firtname, user_lastname, user_date_birth, user_email) VALUES (%s, %s, %s, %s) RETURNING user_id;"
        cursor.execute(query, (firstname, lastname, date_birth, email))
        user_id = cursor.fetchone()[0]
        query = "INSERT INTO user_phone (user_id, phone) VALUES (%s, %s);"
        cursor.execute(query, (user_id, phone))
        self.conn.commit()
        # user_id = 1
        return user_id

    def update(self, user_id, firstname, lastname, date_bith, email, phone):
        return user_id

    def delete(self, user_id):
        return user_id