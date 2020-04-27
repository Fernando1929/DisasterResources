from config.dbconfig import pg_config
import psycopg2


class BatteryDAO:

    #battery = supplier_id, resource_id, power_id, battery_id, resource_category, resource_name, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, battery_type
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    
    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "Select * from resource Natural Inner Join bateries;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAllAvailableBatteries(self):
        result = [
            [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result
    
    def getAllReservedBatteries(self):
        result = [
            [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getAllRequestedBatteries(self):
        result = [
            [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getBatteryById(self, battery_id):
        result =  [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA']
        return result

    def getBatteryByResourceId(self, resource_id):
        result =  [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA']
        return result

    def getBatteriesByPowerCapacity(self, power_capacity):
        result = [
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result
    
    def getBatteriesByPowerCondition(self, power_condition):
        result = [
            [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getBatteriesByType(self, battery_type):
        result = [
           [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA']
        ]
        return result

    def getBatteriesBySupplierId(self, supplier_id):
        result = [
            [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getAllAvailableBatteriesBySupplierId(self, supplier_id):
        result = [
            [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result
    
    def getAllReservedBatteriesBySupplierId(self, supplier_id):
        result = [
            [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getAllRequestedBatteriesBySupplierId(self, supplier_id):
        result = [
            [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result
    
    def getBatteryAddress(self, user_id):
        result = [1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def insert(self, resource_id, power_condition, power_capacity, battery_type):
        cursor = self.conn.cursor()
        query = "insert into bateries(resource_id, power_condition, power_capacity, battery_type) values(%s,%s,%s,%s) returning baterry_id"
        cursor.execute(query,(resource_id, power_condition, power_capacity, battery_type))
        battery_id = cursor.fetchone()[0]
        self.conn.commit()
        return battery_id
        
    def update(self,resource_id):
        resource_id = 1
        return resource_id
    
    def delete(self, resource_id):
        resource_id = 1
        return resource_id