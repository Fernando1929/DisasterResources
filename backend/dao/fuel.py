from config.dbconfig import pg_config
import psycopg2

class FuelDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

# fuel = fuel_id, resource_id, supplier_id, fuel_name, fuel_brand, fuel_quantity, fuel_price, fuel_type, fuel_gallons

    def getAllFuels(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableFuels(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource WHERE resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedFuels(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource NATURAL INNER JOIN resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedFuels(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource NATURAL INNER JOIN resource_requests;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelById(self, fuel_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource WHERE fuel_id = %s;"
        cursor.execute(query, (fuel_id))
        result = cursor.fetchone()
        return result

    def getFuelByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource WHERE resource_id = %s;"
        cursor.execute(query, (resource_id))
        result = cursor.fetchone()
        return result

    def getFuelsByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource WHERE resource_brand = %s;"
        cursor.execute(query, (resource_brand))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelsByType(self, fuel_type):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource WHERE fuel_type = %s;"
        cursor.execute(query, (fuel_type))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelsByGallons(self, fuel_gallons):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource WHERE fuel_gallons = %s;"
        cursor.execute(query, (fuel_gallons))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelsByTypeAndGallons(self, fuel_type, fuel_gallons):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource WHERE fuel_type = %s AND fuel_gallons = %s;"
        cursor.execute(query, (fuel_type, fuel_gallons))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableFuelsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource WHERE supplier_id = %s AND resource_quantity > 0;"
        cursor.execute(query, (supplier_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedFuelsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource NATURAL INNER JOIN resource_reservations WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedFuelsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM fuel NATURAL INNER JOIN resource NATURAL INNER JOIN resource_requests WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM address NATURAL INNER JOIN supplier WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id))
        result = cursor.fetchone()
        return result

    def insert(self, resource_id, fuel_type, fuel_gallons):
        cursor = self.conn.cursor()
        query = "INSERT INTO fuel (resource_id, fuel_type, fuel_gallons) VALUES (%s, %s, %s) RETURNING fuel_id;"
        cursor.execute(query, (resource_id, fuel_type, fuel_gallons))
        fuel_id = cursor.fetchone()[0]
        self.conn.commit()
        return fuel_id

    def delete(self, fuel_id):
        resource_id = 1
        return resource_id

    def update(self, fuel_id, fuel_type, fuel_gallons):
        resource_id = 1
        return resource_id