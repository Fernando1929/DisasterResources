from config.dbconfig import pg_config
import psycopg2
class ClothDAO:

    # cloth = cloth_id, resource_id, supplier_id, category, cloth_name, cloth_quantity, cloth_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type
    
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClothes(self):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableClothes(self):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedClothes(self):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource natural inner join resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothById(self, cloth_id):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where cloth_id = %s;"
        cursor.execute(query, (cloth_id,))
        result = cursor.fetchone()
        return result

    def getClothByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getClothesByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where resource_brand = %s;"
        cursor.execute(query, (resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothesByCondition(self, cloth_condition):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where cloth_condition = %s;"
        cursor.execute(query, (cloth_condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothesByGender(self, cloth_gender):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where cloth_gender = %s;"
        cursor.execute(query, (cloth_gender,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothesBySize(self, cloth_size):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where cloth_size = %s;"
        cursor.execute(query, (cloth_size,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothesByType(self, cloth_type):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where cloth_type = %s;"
        cursor.execute(query, (cloth_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableClothesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource where supplier_id = %s and resource_quantity > 0;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedClothesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from cloth natural inner join resource natural inner join resource_reservations where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select address_id, user_id, addressline, city, state_province, country, zipcode from address natural inner join supplier where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self, resource_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type):
        cursor = self.conn.cursor()
        query = "insert into cloth(resource_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type) values (%s, %s, %s, %s, %s, %s) returning cloth_id;"
        cursor.execute(query, (resource_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type))
        cloth_id = cursor.fetchone()[0]
        self.conn.commit()
        return cloth_id

    def update(self, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type):
        cursor = self.conn.cursor()
        query = "update cloth set cloth_size = %s, cloth_material = %s, cloth_condition = %s, cloth_gender = %s, cloth_type = %s where cloth_id = %s returning resource_id;"
        cursor.execute(query, (cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type, cloth_id))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def delete(self, cloth_id):
        cursor = self.conn.cursor()
        query = "delete from cloth where cloth_id = %s returning resource_id;"
        cursor.execute(query,(cloth_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id