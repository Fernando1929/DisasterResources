from config.dbconfig import pg_config
import psycopg2

class ResourceOrdersDAO:

    # order_id, resource_id, order_quantity, discount
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self, order_id, resource_id, order_quantity, discount):
        cursor = self.conn.cursor()
        query = "insert into resource_orders(order_id, resource_id, order_quantity, discount) values (%s, %s, %s, %s);"
        cursor.execute(query, (order_id, resource_id, order_quantity, discount))
        self.conn.commit()

    def update(self, order_id, resource_id, order_quantity, discount):
        cursor = self.conn.cursor()
        query = "update resource_orders set order_quantity = %s, discount = %s where order_id = %s and resource_id = %s"
        cursor.execute(query, (order_quantity, discount, order_id, resource_id))
        self.conn.commit()

    def delete(self, order_id):
        cursor = self.conn.cursor()
        query = "delete from resource_orders where order_id = %s"
        cursor.execute(query, (order_id,))
        self.conn.commit()
