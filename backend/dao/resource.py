from config.dbconfig import pg_config
import psycopg2

class ResourceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # resource = resource_id, supplier_id, category, name, brand, quantity, price

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        # result = [
        #     [1, 1, "fuel", "Gasoline", "Shell", 1, 20.00],
        #     [2, 2, "food", "Canned peaches", "Del Monte", 12, 10.00],
        #     [3, 3, "medicine", "Sumatriptan", "Walgreens", 1, 10.00],
        #     [4, 4, "tools", "Wrench", "Craftsman", 5, 40.00],
        #     [5, 5, "battery", 'Battery', 'Duracel', 10, 7.00],
        #     [6, 6, "cloth", "Cloth", "Aeropostal", 5, 10.00],
        #     [7, 7, "generator", 'generator', 'WEN', 10, 300.00],
        #     [8, 8, "heavy_equipment", "Heavy Equipment", "Caterpillar", 1, 125000.00],
        #     [9, 9, "ice", 'ice', 'el angel', 10, 2.50],
        #     [10, 10, "medical_device", "Medical Device", "Forcemech", 1, 1900.00],
        #     [11, 11, "water", "Water", "Nikini", 10, 1.00]
        # ]
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Resource WHERE resource_id = %s;"
        cursor.execute(query, (resource_id))
        result = cursor.fetchone()
        # result = [11, 11, "water", "Water", "Nikini", 10, 1.00]
        return result

    def insert(self, supplier_id, category, name, brand, quantity, price):
        cursor = self.conn.cursor()
        query = "INSERT INTO Resource (supplier_id, resource_category, resource_name, resource_brand, resource_quantity, resource_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING resource_id;"
        cursor.execute(query, (supplier_id, category, name, brand, quantity, price))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        # resource_id = 1
        return resource_id

    def update(self, resource_id, supplier_id, category, name, brand, quantity, price):
        return resource_id

    def delete(self, resource_id):
        return resource_id