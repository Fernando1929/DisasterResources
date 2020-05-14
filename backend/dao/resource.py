from config.dbconfig import pg_config
import psycopg2
class ResourceDAO:

    # resource = resource_id, supplier_id, category, name, brand, quantity, price
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = "select * from resource where resource_id = %s;"
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
        query = "insert into resource(supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price) values (%s, %s, %s, %s, %s, %s) returning resource_id;"
        cursor.execute(query, (supplier_id, category, name, brand, quantity, price,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def update(self, resource_id, supplier_id, category_id, name, brand, quantity, price):
        cursor = self.conn.cursor()
        query = "update resource set supplier_id = %s, category_id = %s, resource_name = %s, resource_brand = %s, resource_quantity = %s, resource_price = %s where resource_id = %s returning resource_id;"
        cursor.execute(query, (supplier_id, category_id, name, brand, quantity, price, resource_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def delete(self, resource_id):
        cursor = self.conn.cursor()
        query = "delete from resource where resource_id = %s returning resource_id;"
        cursor.execute(query,(resource_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id 
