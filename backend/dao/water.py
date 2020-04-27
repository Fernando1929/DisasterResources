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
        query = "select * from water;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableWaters(self):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "water", "Water", "Great Value", 5, 0.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllReservedWaters(self):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "water", "Water", "Great Value", 5, 0.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllRequestedWaters(self):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "water", "Water", "Great Value", 5, 0.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterById(self, water_id):
        result = [1, 1, 1, "water", "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"]
        return result

    def getWaterByResourceId(self, resource_id):
        result = [1, 1, 1, "water", "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"]
        return result

    def getWatersByBrand(self, resource_brand):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "water", "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWatersByContainer(self, water_container):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "water", "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWatersByType(self, water_type):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "water", "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWatersBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "water", "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllAvailableWatersBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 1, "water", "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllReservedWatersBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 1, "water", "Water", "Great Value", 5, 0.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllRequestedWatersBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "water", "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 1, "water", "Water", "Great Value", 5, 0.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterAddress(self, user_id):
        result = [1, 1, "Barrio Las Palmas", "Utuado", "PR", "US", "00641"]
        return result

    def insert(self, resource_id, water_size, water_container, water_type, water_exp_date):
        cursor = self.conn.cursor()
        query = "insert into water(resource_id, water_size, water_container, water_type, water-exp_date) values (%s, %s, %s, %s, %s) returning water_id;"
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