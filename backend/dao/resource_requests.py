from config.dbconfig import pg_config
import psycopg2
class ResourceRequestsDAO:
    def _init_(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self, request_id, resource_id, request_quantity):
        cursor = self.conn.cursor()
        query = "insert into resource_requests(request_id, resource_id, request_quantity) values (%s, %s, %s);"
        cursor.execute(query, (request_id, resource_id, request_quantity))
        resource_request_id = cursor.fetchone()[0]
        self.conn.commit()

    def update(self, payment_id, user_id):
        return payment_id

    def delete(self, payment_id):
        return payment_id