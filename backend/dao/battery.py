from config.dbconfig import pg_config
import psycopg2


class BatteryDAO:

    #battery = supplier_id, resource_id, power_id, battery_id, resource_category, resource_name, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, battery_type
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    
    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN  batteries;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableBatteries(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries WHERE resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedBatteries(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries NATURAL INNER JOIN resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        
    def getBatteryById(self, battery_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries WHERE battery_id = %s;"
        cursor.execute(query,(battery_id,))
        result = cursor.fetchone()
        return result

    def getBatteryByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries WHERE resource_id = %s;"
        cursor.execute(query,(resource_id,))
        result = cursor.fetchone()
        return result

    def getBatteriesByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries WHERE resource_brand = %s;"
        cursor.execute(query,(resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesByPowerCapacity(self, power_capacity):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries WHERE power_capacity = %s;"
        cursor.execute(query,(power_capacity,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getBatteriesByPowerCondition(self, power_condition):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries WHERE power_condition = %s;"
        cursor.execute(query,(power_condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesByType(self, battery_type):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries WHERE battery_type = %s;"
        cursor.execute(query,(battery_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteriesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries WHERE supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableBatteriesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries WHERE supplier_id = %s and resource_quantity > 0;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllReservedBatteriesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, battery_id, power_capacity, power_condition, battery_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM resource NATURAL INNER JOIN batteries NATURAL INNER JOIN resource_reservations WHERE supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getBatteryAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT address_id, user_id, addressline, city, state_province, country, zipcode FROM address NATURAL INNER JOIN supplier WHERE supplier_id = %s;" 
        cursor.execute(query,(supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self, resource_id, power_condition, power_capacity, battery_type):
        cursor = self.conn.cursor()
        query = "insert into batteries(resource_id, power_condition, power_capacity, battery_type) values(%s,%s,%s,%s) returning battery_id;"
        cursor.execute(query,(resource_id, power_condition, power_capacity, battery_type))
        battery_id = cursor.fetchone()[0]
        self.conn.commit()
        return battery_id
        
    def update(self,battery_id, power_capacity, power_condition, battery_type):
        cursor = self.conn.cursor()
        query = "update batteries set power_capacity = %s, power_condition = %s, battery_type = %s where battery_id = %s returning resource_id;"
        cursor.execute(query,(power_capacity, power_condition, battery_type, battery_id))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id
    
    def delete(self, battery_id):
        cursor = self.conn.cursor()
        query = "delete from batteries where battery_id = %s returning resource_id;"
        cursor.execute(query,(battery_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id