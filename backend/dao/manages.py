from config.dbconfig import pg_config
import psycopg2

class ManagesDAO:

    # admin_id, user_id
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self, admin_id, user_id):
        cursor = self.conn.cursor()
        query = "insert into manages(admin_id, user_id) values (%s, %s);"
        cursor.execute(query, (user_id, admin_id))
        self.conn.commit()

    def update(self, admin_id, user_id):
        cursor = self.conn.cursor()
        query = "update manages set user_id = %s where admin_id = %s;"
        cursor.execute(query, (user_id, admin_id))
        self.conn.commit()

    def delete(self, admin_id, user_id):
        cursor = self.conn.cursor()
        query = "delete from manages where user_id = %s and admin_id = %s;"
        cursor.execute(query, (user_id, admin_id))
        self.conn.commit()