from config.dbconfig import pg_config
import psycopg2

class FoodDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # food = food_id, resource_id, supplier_id, resource_category, food_name, food_brand, food_quantity, food_price, 
    #           food_category, food_container, food_type, food_ounces, food_expdate

    # food_type = food resource subtype: baby, canned or dry food
    # food_category = food category/group: fruit, grains, vegetables, dairy, protein, fats, etc

    def getAllFoods(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableFoods(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedFoods(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource NATURAL INNER JOIN resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getAllRequestedFoods(self):
    #     cursor = self.conn.cursor()
    #     query = "SELECT * FROM food NATURAL INNER JOIN resource NATURAL INNER JOIN resource_requests;"
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getFoodById(self, food_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE food_id = %s;"
        cursor.execute(query, (food_id,))
        result = cursor.fetchone()
        return result

    def getFoodByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getFoodsByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE resource_brand = %s;"
        cursor.execute(query, (resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodsByCategory(self, food_category):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE food_category = %s;"
        cursor.execute(query, (food_category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodsByContainer(self, food_container):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE food_container = %s;"
        cursor.execute(query, (food_container,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodsByType(self, food_type):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE food_type = %s;"
        cursor.execute(query, (food_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodsByOunces(self, food_ounces):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE food_ounces = %s;"
        cursor.execute(query, (food_ounces,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodsByCategoryAndType(self, food_category, food_type):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE food_category = %s AND food_type = %s;"
        cursor.execute(query, (food_category, food_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableFoodsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource WHERE supplier_id = %s AND resource_quantity > 0;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedFoodsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM food NATURAL INNER JOIN resource NATURAL INNER JOIN resource_reservations WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getAllRequestedFoodsBySupplierId(self, supplier_id):
    #     cursor = self.conn.cursor()
    #     query = "SELECT * FROM food NATURAL INNER JOIN resource NATURAL INNER JOIN resource_requests WHERE supplier_id = %s;"
    #     cursor.execute(query, (supplier_id,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getFoodAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM address NATURAL INNER JOIN supplier WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self, resource_id, food_category, food_container, food_type, food_ounces, food_expdate):
        cursor = self.conn.cursor()
        query = "INSERT INTO food (resource_id, food_category, food_container, food_type, food_ounces, food_expdate) VALUES (%s, %s, %s, %s, %s, %s) RETURNING food_id;"
        cursor.execute(query, (resource_id, food_category, food_container, food_type, food_ounces, food_expdate,))
        food_id = cursor.fetchone()[0]
        self.conn.commit()
        return food_id

    def delete(self, food_id):
        cursor = self.conn.cursor()
        query = "delete from food where food_id = %s returning resource_id;"
        cursor.execute(query,(food_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def update(self, food_id, food_category, food_container, food_type, food_ounces, food_expdate):
        cursor = self.conn.cursor()
        query = "update food set food_category = %s, food_container = %s, food_type = %s, food_ounces = %s, food_expdate = %s where food_id = %s returning resource_id;"
        cursor.execute(query, (food_category, food_container, food_type, food_ounces, food_expdate, food_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id
