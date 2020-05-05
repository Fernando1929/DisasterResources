from config.dbconfig import pg_config
import psycopg2


class BatteryDAO:

    #battery = supplier_id, resource_id, power_id, battery_id, resource_category, resource_name, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, battery_type
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    
    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join batteries;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableBatteries(self):#needs test
        cursor = self.conn.cursor()
        query = "select * from resource natural inner join batteries where resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedBatteries(self):#needs test
        cursor = self.conn.cursor()
        query = "select * from resource natural inner join batteries natural inner join resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedBatteries(self):#needs test
        cursor = self.conn.cursor()
        query = "select * from resource natural inner join batterues natural inner join resource_requests;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        
    def getBatteryById(self, battery_id): #can be changed to fetch one because ids are unique to only one element
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join batteries where battery_id = %s;"
        cursor.execute(query,(battery_id,))
        result = cursor.fetchone()
        return result

    def getBatteryByResourceId(self, resource_id):  #can be changed to fetch one because ids are unique to only one element
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join batteries where resource_id = %s;"
        cursor.execute(query,(resource_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesByPowerCapacity(self, power_capacity):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join batteries where power_capacity = %s;"
        cursor.execute(query,(power_capacity,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getBatteriesByPowerCondition(self, power_condition):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join batteries where power_condition = %s;"
        cursor.execute(query,(power_condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesByType(self, battery_type):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join batteries where battery_type = %s;"
        cursor.execute(query,(battery_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join batteries where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableBatteriesBySupplierId(self, supplier_id):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join batteries where supplier_id = %s and Not in (select * from resource Natural Inner Joint batteries Natural Inner Join reserved);"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedBatteriesBySupplierId(self, supplier_id): #needs test
        cursor = self.conn.cursor()
        query = "select * from resource Natural Inner Joint batteries Natural Inner Join reserved where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedBatteriesBySupplierId(self, supplier_id): #needs test
        cursor = self.conn.cursor()
        query = "select * from resource Natural Inner Joint batteries Natural Inner Join request where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getBatteryAddress(self, user_id): #needs test
        cursor = self.conn.cursor()
        query = "select address from user Natural Inner Join supplier where supplier_id = %s;" 
        cursor.execute(query,(user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, resource_id, power_condition, power_capacity, battery_type):
        cursor = self.conn.cursor()
        query = "insert into batteries(resource_id, power_condition, power_capacity, battery_type) values(%s,%s,%s,%s) returning battery_id;"
        cursor.execute(query,(resource_id, power_condition, power_capacity, battery_type))
        battery_id = cursor.fetchone()[0]
        self.conn.commit()
        return battery_id
        
    def update(self,resource_id, power_capacity, power_condition, battery_type): #needs test
        cursor = self.conn.cursor()
        query = "update batteries set power_capacity = %s, power_condition = %s, battery_type = %s where resource_id = %s returning battery_id;"
        cursor.execute(query,(power_capacity, power_condition, battery_type, resource_id))
        battery_id = cursor.fetchone()[0]
        self.conn.commit()
        return battery_id
    
    def delete(self, resource_id): #needs test
        cursor = self.conn.cursor()
        query = "delete from batteries where resource_id = %s returning battery_id;"
        cursor.execute(query,(resource_id,))
        battery_id = cursor.fetchone()[0]
        self.conn.commit()
        return battery_id