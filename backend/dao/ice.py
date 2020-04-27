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

    def getAllAvailableIce(self):
        result = [
            [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5],
            [2, 1, 2, "ice", 'ice', 'submarine', 8, 2.50, 6]
        ]
        return result

    def getAllReservedIce(self):
        result = [
            [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5],
            [2, 1, 2, "ice", 'ice', 'submarine', 8, 2.50, 6]
        ]
        return result
    
    def getAllRequestedIce(self):
        result = [
            [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5],
            [2, 1, 2, "ice", 'ice', 'submarine', 8, 2.50, 6]
        ]
        return result

    def getIceById(self,ice_id):
        result = [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5]
        return result    

    def getIceByResourceId(self,resource_id):
        result = [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5]
        return result  
    
    def getIceByBrand(self,ice_brand):
        result = [
            [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5],
            [2, 1, 2, "ice", 'ice', 'submarine', 8, 2.50, 6]
        ]
        return result

    def getIceByWeight(self,ice_weight):
        result = [
            [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5],
            [2, 1, 2, "ice", 'ice', 'submarine', 8, 2.50, 6]
        ]
        return result
    
    def getIceBySupplierId(self, supplier_id):
        result = [
            [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5],
            [2, 1, 2, "ice", 'ice', 'submarine', 8, 2.50, 6]
        ]
        return result
    
    def getAllAvailableIceBySypplierId(self, supplier_id):
        result = [
            [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5],
            [2, 1, 2, "ice", 'ice', 'submarine', 8, 2.50, 6]
        ]
        return result

    def getAllReservedIceBySypplierId(self, supplier_id):
        result = [
            [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5],
            [2, 1, 2, "ice", 'ice', 'submarine', 8, 2.50, 6]
        ]
        return result

    def getAllRequestedIceBySypplierId(self, supplier_id):
        result = [
            [1, 2, 1, "ice", 'ice', 'el angel', 10, 2.50, 5],
            [2, 1, 2, "ice", 'ice', 'submarine', 8, 2.50, 6]
        ]
        return result
    
    def getIceAddress(self, user_id):
        result = [1, 1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def insert(self,resource_id, ice_weight):
        cursor = self.conn.cursor()
        ice_query = "insert into ice(resource_id, ice_weight) values(%s,%s) returning ice_id"
        cursor.execute(ice_query,(resource_id, ice_weight))
        ice_id = cursor.fetchone()[0]
        self.conn.commit()
        return ice_id

    def delete(self, resource_id):
        resource_id = 1
        return resource_id

    def update(self, ice_id, ice_weight):
        resource_id = 1
        return resource_id