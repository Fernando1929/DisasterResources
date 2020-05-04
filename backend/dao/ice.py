from config.dbconfig import pg_config
import psycopg2

class IceDAO:

    #ice = ice_id, resource_id, supplier_id, ice_name, ice_brand, ice_quantity, ice_price , ice_weight
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllIce(self):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join ice;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableIce(self): #needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join ice where Not in (select * from resource Natural Inner Join ice Natural Inner Join reservation);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedIce(self): #needs test
        cursor = self.conn.cursor()
        query = "select * from resource Natural Inner Join ice Natural Inner Join reservation;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllRequestedIce(self): #needs test
        cursor = self.conn.cursor()
        query = "select * from resource Natural Inner Join ice Natural Inner Join request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceById(self,ice_id): #needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join ice where ice_id = %s;"
        cursor.execute(query,(ice_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result  

    def getIceByResourceId(self,resource_id): #needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join ice where resource_id = %s;"
        cursor.execute(query,(resource_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getIceByBrand(self,ice_brand): #needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join ice where resource_brand = %s;"
        cursor.execute(query,(ice_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceByWeight(self,ice_weight): #needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join ice where ice_weight = %s;" #maybe añadir que no este reserved
        cursor.execute(query,(ice_weight,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getIceBySupplierId(self, supplier_id): #needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join ice where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableIceBySypplierId(self, supplier_id): #needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join ice where supplier_id = %s and  Not in (select * from resource Natural Inner Join ice Natural Inner Join reservation);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedIceBySypplierId(self, supplier_id): #needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join ice Natural Inner Join reservation where Not in (select * from resource Natural Inner Join ice Natural Inner Join reservation);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedIceBySypplierId(self, supplier_id): #needs test
        cursor = self.conn.cursor()
        query = "select * from resource Natural Inner Join ice Natural Inner Join request where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getIceAddress(self, supplier_id): #needs test
        cursor = self.conn.cursor()
        query = "Select * from users Natural Inner Join supplier Natural Inner Join Address where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self,resource_id, ice_weight):
        cursor = self.conn.cursor()
        query = "insert into ice(resource_id, ice_weight) values(%s,%s) returning ice_id;"
        cursor.execute(query,(resource_id, ice_weight))
        ice_id = cursor.fetchone()[0]
        self.conn.commit()
        return ice_id

    def delete(self, resource_id): #needs test
        cursor = self.conn.cursor()
        query = "delete from ice where resource_id = %s returning ice_id;"
        cursor.execute(query,(resource_id))
        ice_id = cursor.fetchone()[0]
        self.conn.commit()
        return ice_id

    def update(self, ice_id, ice_weight): #needs test
        cursor = self.conn.cursor()
        query = "update ice set ice_weight = %s where ice_id = %s returning ice_id;"
        cursor.execute(query,(ice_weight,ice_id))
        ice_id = cursor.fetchone()[0]
        self.conn.commit()
        return ice_id