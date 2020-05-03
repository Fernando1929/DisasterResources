from config.dbconfig import pg_config
import psycopg2
class RequestCategoryDAO:
    def _init_(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self, request_id, category_id, request_quantity):
        cursor = self.conn.cursor()
        query = "insert into request_category(request_id, category_id, request_quantity) values (%s, %s, %s);"
        cursor.execute(query, (request_id, category_id, request_quantity))
        resource_request_id = cursor.fetchone()[0]
        self.conn.commit()

    def update(self, request_id, category_id, request_quantity):
        return None

    def delete(self, request_id, category_id):
        return None