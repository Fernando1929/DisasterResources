from config.dbconfig import pg_config
import psycopg2

class GeneratorDAO:
    # generator = supplier_id, resource_id, power_id, generator_id, resource_name, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, generator_fuel
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    
    def getAllGenerators(self):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableGenerators(self):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where Not in (select * from resource Natural Inner Join generators Natural Inner Join reserved);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedGenerators(self):#needs test
        cursor = self.conn.cursor()
        query = "select * from resource Natural Inner Join generators Natural Inner Join reserved;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedGenerators(self):#needs test
        cursor = self.conn.cursor()
        query = "select * from resource Natural Inner Join generators Natural Inner Join request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorById(self, generator_id): #can be changed to fetch one to get one only rows id are unique
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where generator_id = %s;"
        cursor.execute(query,(generator_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorsByPowerCapacity(self,power_capacity):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where power_capacity = %s;"
        cursor.execute(query,(power_capacity,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getGeneratorsByPowerCondition(self, power_condition):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where power_condition = %s;"
        cursor.execute(query,(power_condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorsByFuel(self, generator_fuel):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where generator_fuel = %s;"
        cursor.execute(query,(generator_fuel,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getGeneratorsBySupplierId(self, supplier_id):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorsByResourceId(self, resource_id):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where resource_id = %s;"
        cursor.execute(query,(resource_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableGeneratorsBySupplierId(self, supplier_id):#needs test
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where supplier_id = %s and Not in (select * from resource Natural Inner Join generators Natural Inner Join reserved);"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedGeneratorsBySupplierId(self, supplier_id):#needs test
        cursor = self.conn.cursor()
        query = "select * from resource Natural Inner Join generators Natural Inner Join reserved where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedGeneratorsBySupplierId(self, supplier_id):#needs test
        cursor = self.conn.cursor()
        query = "select * from resource Natural Inner Join generators Natural Inner Join request where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getGeneratorAddress(self, user_id): # should be user id or supplier_id ? # we need to verify the location of this method (we are locking for the supplier addres not the object address)
        cursor = self.conn.cursor()
        query = "select * from user Natural Inner Join supplier where supplier_id = %s;" #I think it shoud be supplier id but idk 
        cursor.execute(query,(user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def insert(self, resource_id, power_capacity, power_condition, generator_fuel):
        cursor = self.conn.cursor()
        query = "insert into generators(resource_id, power_capacity, power_condition, generator_fuel) values (%s, %s, %s, %s) returning resource_id;"
        cursor.execute(query, (resource_id, power_capacity, power_condition, generator_fuel))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def update(self, resource_id, power_capacity, power_condition, battery_type):#needs test
        cursor = self.conn.cursor()
        query = "update batteries set power_capacity = %s, power_condition = %s, battery_type = %s where resource_id = %s returning battery_id;"
        cursor.execute(query,(power_capacity, power_condition, battery_type, resource_id))
        battery_id = cursor.fetchone()[0]
        self.conn.commit()
        return battery_id

    def delete(self, resource_id):#needs test
        cursor = self.conn.cursor()
        query = "delete from batteries where resource_id = %s returning battery_id;"
        cursor.execute(query,(resource_id,))
        battery_id = cursor.fetchone()[0]
        self.conn.commit()
        return battery_id