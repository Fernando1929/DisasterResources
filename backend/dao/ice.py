from config.dbconfig import pg_config
import psycopg2

class IceDAO:

    #ice = ice_id, resource_id, supplier_id, ice_name, ice_brand, ice_quantity, ice_price , ice_weight
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllIce(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableIce(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice WHERE resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedIce(self): 
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice NATURAL INNER JOIN resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceById(self,ice_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice WHERE ice_id = %s;"
        cursor.execute(query,(ice_id,))
        result = cursor.fetchone()
        return result  

    def getIceByResourceId(self,resource_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice WHERE resource_id = %s;"
        cursor.execute(query,(resource_id,))
        result = cursor.fetchone()
        return result
    
    def getIceByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice WHERE resource_brand = %s;"
        cursor.execute(query,(resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceByWeight(self,ice_weight):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice WHERE ice_weight = %s;"
        cursor.execute(query,(ice_weight,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getIceBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice WHERE supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableIceBySypplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice WHERE resource_quantity > 0 and supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedIceBySypplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, ice_id, ice_weight, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN ice NATURAL INNER JOIN resource_reservations WHERE supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getIceAddress(self, supplier_id): 
        cursor = self.conn.cursor()
        query = "SELECT address_id, user_id, addressline, city, state_province, country, zipcode FROM users NATURAL INNER JOIN supplier NATURAL INNER JOIN Address WHERE supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self,resource_id, ice_weight):
        cursor = self.conn.cursor()
        query = "insert into ice(resource_id, ice_weight) values(%s,%s) returning ice_id;"
        cursor.execute(query,(resource_id, ice_weight,))
        ice_id = cursor.fetchone()[0]
        self.conn.commit()
        return ice_id

    def delete(self, ice_id):
        cursor = self.conn.cursor()
        query = "delete from ice where ice_id = %s returning resource_id;"
        cursor.execute(query,(ice_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def update(self, ice_id, ice_weight): #VI
        cursor = self.conn.cursor()
        query = "update ice set ice_weight = %s where ice_id = %s returning resource_id;"
        cursor.execute(query,(ice_weight,ice_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id