from config.dbconfig import pg_config
import psycopg2

class BatteryDAO:
    def __init__(self):
        super().__init__()

    #battery = supplier_id, resource_id, power_id, battery_id, resource_name, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, battery_type
    def getAllBattery(self):
        result = [
            [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result
    
    def getAllAvailableBattery(self):
        result = [
            [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result
    
    def getAllReservedBattery(self):
        result = [
            [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getAllRequestedBattery(self):
        result = [
            [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getBatteryById(self,battery_id):
        result =  [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA']
        return result

    def getBatteryByResourceId(self,resource_id):
        result =  [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA']
        return result

    def getBatteryByPowerCapacity(self,power_capacity):
        result = [
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result
    
    def getBatteryByPowerCondition(self, power_condition):
        result = [
            [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getBatteryByType(self, battery_type):
        result = [
           [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA']
        ]
        return result

    def getBatteryBySupplierId(self, supplier_id):
        result = [
            [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getAllAvailableBatteryBySupplierId(self, supplier_id):
        result = [
            [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result
    
    def getAllReservedBatteryBySupplierId(self, supplier_id):
        result = [
            [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result

    def getAllRequestedBatteryBySupplierId(self, supplier_id):
        result = [
            [1,2,3,4, 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
        return result
    
    def getBatteryAddress(self, user_id):
        result = [1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def insert(self, resource_id, power_id, battery_type):
        resource_id =1
        return resource_id

    def update(self,resource_id):
        resource_id =1
        return resource_id
    
    def delete(self, resource_id):
        resource_id =1
        return resource_id