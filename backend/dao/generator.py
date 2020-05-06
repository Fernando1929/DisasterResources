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
    
    def getAllAvailableGenerators(self):
        cursor = self.conn.cursor()
        query = "select * from generators natural inner join resource where resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedGenerators(self):
        cursor = self.conn.cursor()
        query = "select * from generators natural inner join resource natural inner join resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getAllRequestedGenerators(self):
    #     cursor = self.conn.cursor()
    #     query = "select * from generators natural inner join resource natural inner join resource_requests;"
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getGeneratorById(self, generator_id):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where generator_id = %s;"
        cursor.execute(query,(generator_id,))
        result = cursor.fetchone()
        return result

    def getGeneratorByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where resource_id = %s;"
        cursor.execute(query,(resource_id,))
        result = cursor.fetchone()
        return result
    
    def getGeneratorByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query =  "select * from resource Natural Inner Join generators where resource_brand = %s;"
        cursor.execute(query,(resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorsByPowerCapacity(self,power_capacity):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where power_capacity = %s;"
        cursor.execute(query,(power_capacity,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getGeneratorsByPowerCondition(self, power_condition):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where power_condition = %s;"
        cursor.execute(query,(power_condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorsByFuel(self, generator_fuel):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where generator_fuel = %s;"
        cursor.execute(query,(generator_fuel,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getGeneratorsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join generators where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableGeneratorsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from resource natural inner join generators where supplier_id = %s and resource_quantity > 0;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedGeneratorsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from resource natural inner join generators natural inner join resource_reservations where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getAllRequestedGeneratorsBySupplierId(self, supplier_id):
    #     cursor = self.conn.cursor()
    #     query = "select * from resource natural inner join generators natural inner join resource_requests where supplier_id = %s;"
    #     cursor.execute(query,(supplier_id,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    
    def getGeneratorAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from address natural inner join supplier where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result
    
    def insert(self, resource_id, power_capacity, power_condition, generator_fuel):
        cursor = self.conn.cursor()
        query = "insert into generators(resource_id, power_capacity, power_condition, generator_fuel) values (%s, %s, %s, %s) returning generator_id;"
        cursor.execute(query, (resource_id, power_capacity, power_condition, generator_fuel))
        generator_id = cursor.fetchone()[0]
        self.conn.commit()
        return generator_id

    def update(self, resource_id, power_capacity, power_condition, generator_fuel):#VI
        cursor = self.conn.cursor()
        query = "update generators set power_capacity = %s, power_condition = %s, generator_fuel = %s where resource_id = %s returning generator_id;"
        cursor.execute(query,(power_capacity, power_condition, generator_fuel, resource_id))
        generator_id = cursor.fetchone()[0]
        self.conn.commit()
        return generator_id

    def delete(self, resource_id):#VI
        cursor = self.conn.cursor()
        query = "delete from generators where resource_id = %s returning generator_id;"
        cursor.execute(query,(resource_id,))
        generator_id = cursor.fetchone()[0]
        self.conn.commit()
        return generator_id