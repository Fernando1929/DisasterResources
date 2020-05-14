from config.dbconfig import pg_config
import psycopg2
class RequestCategoryDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self, request_id, category_id, request_quantity):
        cursor = self.conn.cursor()
        query = "insert into request_category(request_id, category_id, request_quantity) values (%s, %s, %s);"
        cursor.execute(query, (request_id, category_id, request_quantity))
        self.conn.commit()

    def update(self, request_id, category_id, request_quantity):
        cursor = self.conn.cursor()
        query = "update request_category set request_quantity = %s where request_id = %s and category_id = %s;"
        cursor.execute(query, (request_quantity, request_id, category_id))
        self.conn.commit()

    def delete(self, request_id):
        cursor = self.conn.cursor()
        query = "delete from request_category where request_id = %s;"
        cursor.execute(query, (request_id,))
        self.conn.commit()