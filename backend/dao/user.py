from config.dbconfig import pg_config
import psycopg2
class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getUserById(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from users where user_id = %s;"
        cursor.execute(query, (user_id))
        result = cursor.fetchone()
        return result

    def insert(self, firstname, lastname, date_birth, email, phone):
        cursor = self.conn.cursor()
        query = "insert into users(user_firstname, user_lastname, user_date_birth, user_email) values (%s, %s, %s, %s) returning user_id;"
        cursor.execute(query, (firstname, lastname, date_birth, email))
        user_id = cursor.fetchone()[0]
        self.conn.commit()
        self.insertPhone(user_id, phone)
        return user_id

    def insertPhone(self, user_id, phone):
        cursor = self.conn.cursor()
        query = "insert into user_phone(user_id, user_phone) values (%s, %s);"
        cursor.execute(query, (user_id, phone))
        self.conn.commit()

    def update(self, user_id, firstname, lastname, date_bith, email, phone):
        return user_id

    def delete(self, user_id):
        return user_id