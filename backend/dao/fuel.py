from config.dbconfig import pg_config
import psycopg2

class FuelDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

# fuel = fuel_id, resource_id, supplier_id, fuel_name, fuel_brand, fuel_quantity, fuel_price, fuel_type, fuel_gallons

    def getAllFuels(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Fuel;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllAvailableFuels(self):
        cursor = self.conn.cursor()
        query = ""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllReservedFuels(self):
        cursor = self.conn.cursor()
        query = ""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllRequestedFuels(self):
        cursor = self.conn.cursor()
        query = ""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelById(self, fuel_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Fuel NATURAL INNER JOIN Resource WHERE fuel_id = %s;"
        cursor.execute(query, (fuel_id))
        result = cursor.fetchone()
        # result = [1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]
        return result

    def getFuelByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Fuel NATURAL INNER JOIN Resource WHERE resource_id = %s;"
        cursor.execute(query, (resource_id))
        result = cursor.fetchone()
        # result = [1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]
        return result

    def getFuelsByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Fuel NATURAL INNER JOIN Resource WHERE resource_brand = %s;"
        cursor.execute(query, (resource_brand))
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelsByType(self, fuel_type):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Fuel NATURAL INNER JOIN Resource WHERE fuel_type = %s;"
        cursor.execute(query, (fuel_type))
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelsByGallons(self, fuel_gallons):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Fuel NATURAL INNER JOIN Resource WHERE fuel_gallons = %s;"
        cursor.execute(query, (fuel_gallons))
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelsByTypeAndGallons(self, fuel_type, fuel_gallons):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Fuel NATURAL INNER JOIN Resource WHERE fuel_type = %s AND fuel_gallons = %s;"
        cursor.execute(query, (fuel_type, fuel_gallons))
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Fuel NATURAL INNER JOIN Resource WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id))
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllAvailableFuelsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = ""
        cursor.execute(query, (supplier_id))
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllReservedFuelsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = ""
        cursor.execute(query, (supplier_id))
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getAllRequestedFuelsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = ""
        cursor.execute(query, (supplier_id))
        result = []
        for row in cursor:
            result.append(row)
        # result = [[1, 1, 1, "fuel", "Gasoline", "Shell", 1, 20.00, "gasoline", 12]]
        return result

    def getFuelAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Address NATURAL INNER JOIN Supplier WHERE user_id = %s;"
        cursor.execute(query, (supplier_id))
        result = []
        for row in cursor:
            result.append(row)
        # result = [1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def insert(self, resource_id, fuel_type, fuel_gallons):
        cursor = self.conn.cursor()
        query = "INSERT INTO Fuel (resource_id, fuel_type, fuel_gallons) VALUES (%s, %s, %s) RETURNING fuel_id;"
        cursor.execute(query, (resource_id, fuel_type, fuel_gallons))
        fuel_id = cursor.fetchone()[0]
        self.conn.commit()
        # fuel_id = 1
        return fuel_id

    def delete(self, fuel_id):
        resource_id = 1
        return resource_id

    def update(self, fuel_id, fuel_type, fuel_gallons):
        resource_id = 1
        return resource_id