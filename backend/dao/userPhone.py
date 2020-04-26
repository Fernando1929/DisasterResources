from config.dbconfig import pg_config
import psycopg2
class UserPhoneDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self, user_id, phone):
        cursor = self.conn.cursor()
        query = "insert into user_phone(user_id, user_phone) values (%s, %s) returning phone_id;"
        cursor.execute(query, (user_id, phone))
        phone_id = cursor.fetchone()[0]
        self.conn.commit()
        return phone_id

    def update(self, user_id, firstname, lastname, date_bith, email, phone):
        return user_id

    def delete(self, user_id):
        return user_id