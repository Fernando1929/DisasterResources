class BatteryDAO:
    def __init__(self):
        super().__init__()

    #battery = supplier_id, resource_id, power_id, battery_id, resource_category, resource_name, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, battery_type
    
    def getAllBatteries(self):
        result = [
            [1,2,3,4, "battery", 'Battery', 'Duracel', 10, 7.00, 1.20, 'new', 'AA'],
            [2,3,4,5, "battery", 'Baterry', 'Energizer',  8, 5.00, 1.5, 'new', 'AAA']
        ]
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

    def insert(self, resource_id, power_id, battery_type):
        resource_id = 1
        return resource_id
        
    def update(self,resource_id):
        resource_id = 1
        return resource_id
    
    def delete(self, resource_id):
        resource_id = 1
        return resource_id