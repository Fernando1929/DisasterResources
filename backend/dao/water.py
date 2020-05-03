from config.dbconfig import pg_config
import psycopg2
class WaterDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # water = water_id, resource_id, supplier_id, category, water_name, water_quantity, water_price, water_size, water_container, water_type, water_exp_date

    def getAllWaters(self):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableWaters(self):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource where resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedWaters(self):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource natural inner join resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedWaters(self):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource natural inner join resource_requests;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterById(self, water_id):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource where water_id = %s;"
        cursor.execute(query, (water_id,))
        result = cursor.fetchone()
        return result

    def getWaterByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getWatersByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource where resource_brand = %s;"
        cursor.execute(query, (resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWatersByContainer(self, water_container):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource where water_container = %s;"
        cursor.execute(query, (water_container,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWatersByType(self, water_type):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource where water_type = %s;"
        cursor.execute(query, (water_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWatersBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableWatersBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource where supplier_id = %s and resource_quantity > 0;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedWatersBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource natural inner join resource_reservations where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedWatersBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource natural inner join resource_requests where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from address natural inner join supplier where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self, resource_id, water_size, water_container, water_type, water_exp_date):
        cursor = self.conn.cursor()
        query = "insert into water(resource_id, water_size, water_container, water_type, water_exp_date) values (%s, %s, %s, %s, %s) returning water_id;"
        cursor.execute(query, (resource_id, water_size, water_container, water_type, water_exp_date))
        water_id = cursor.fetchone()[0]
        self.conn.commit()
        return water_id

    def update(self, water_id, water_size, water_container, water_type, water_exp_date):
        resource_id = 1
        return resource_id

    def delete(self, water_id):
        resource_id = 1
        return resource_id