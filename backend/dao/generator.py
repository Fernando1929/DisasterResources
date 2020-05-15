from config.dbconfig import pg_config
import psycopg2

class GeneratorDAO:

    # generator = supplier_id, resource_id, power_id, generator_id, resource_name, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, generator_fuel
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    
    def getAllGenerators(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableGenerators(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM generators NATURAL INNER JOIN resource WHERE resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedGenerators(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM generators NATURAL INNER JOIN resource natural inner join resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorById(self, generator_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators WHERE generator_id = %s;"
        cursor.execute(query,(generator_id,))
        result = cursor.fetchone()
        return result

    def getGeneratorByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators WHERE resource_id = %s;"
        cursor.execute(query,(resource_id,))
        result = cursor.fetchone()
        return result
    
    def getGeneratorByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query =  "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators WHERE resource_brand = %s;"
        cursor.execute(query,(resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorsByPowerCapacity(self,power_capacity):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators WHERE power_capacity = %s;"
        cursor.execute(query,(power_capacity,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getGeneratorsByPowerCondition(self, power_condition):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators WHERE power_condition = %s;"
        cursor.execute(query,(power_condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorsByFuel(self, generator_fuel):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators WHERE generator_fuel = %s;"
        cursor.execute(query,(generator_fuel,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getGeneratorsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators WHERE supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableGeneratorsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators WHERE supplier_id = %s and resource_quantity > 0;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedGeneratorsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, generator_id, power_capacity, power_condition, generator_fuel, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN generators NATURAL INNER JOIN resource_reservations WHERE supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getGeneratorAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT address_id, user_id, addressline, city, state_province, country, zipcode FROM address NATURAL INNER JOIN supplier WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result
    
    def insert(self, resource_id, power_capacity, power_condition, generator_fuel):
        cursor = self.conn.cursor()
        query = "insert into generators(resource_id, power_capacity, power_condition, generator_fuel) values (%s, %s, %s, %s) returning generator_id;"
        cursor.execute(query, (resource_id, power_capacity, power_condition, generator_fuel,))
        generator_id = cursor.fetchone()[0]
        self.conn.commit()
        return generator_id

    def update(self, generator_id, power_capacity, power_condition, generator_fuel):
        cursor = self.conn.cursor()
        query = "update generators set power_capacity = %s, power_condition = %s, generator_fuel = %s where generator_id = %s returning resource_id;"
        cursor.execute(query,(power_capacity, power_condition, generator_fuel, generator_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def delete(self, generator_id):
        cursor = self.conn.cursor()
        query = "delete from generators where generator_id = %s returning resource_id;"
        cursor.execute(query,(generator_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id