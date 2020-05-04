from config.dbconfig import pg_config
import psycopg2

class ResourceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # resource = resource_id, supplier_id, category, name, brand, quantity, price

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM resource WHERE resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getResourcesByName(self, resource_name):
        cursor = self.conn.cursor()
        query = "SELECT * FROM resource WHERE resource_name = %s;"
        cursor.execute(query, (resource_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, supplier_id, category, name, brand, quantity, price):
        cursor = self.conn.cursor()
        query = "INSERT INTO resource (supplier_id, resource_category, resource_name, resource_brand, resource_quantity, resource_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING resource_id;"
        cursor.execute(query, (supplier_id, category, name, brand, quantity, price,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def update(self, resource_id, supplier_id, category, name, brand, quantity, price):
        return resource_id

    def delete(self, resource_id):
        return resource_id