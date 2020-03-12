class WaterDAO:
    def __init__(self):
        super().__init__()

# water = resource_id, supplier_id, resource_name, resource_brand, resource_quantity, resource_price, water_size, water_container, water_type, water_exp_date 
    def getAllWater(self):
        result = [
            ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"],
            ["2", "2", "Water", "Great Value", "5", "1.00", "8", "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterById(self, resource_id):
        result = ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"]
        return result

    def getWAterByBrand(self, resource_brand):
        result = [
            ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"],
            ["2", "2", "Water", "Great Value", "5", "1.00", "8", "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWAterByContainer(self, water_container):
        result = [
            ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"],
            ["2", "2", "Water", "Great Value", "5", "1.00", "8", "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWAterByType(self, water_container):
        result = [
            ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"],
            ["2", "2", "Water", "Great Value", "5", "1.00", "8", "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWatersBySupplierId(self, supplier_id):
        result = [
            ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"],
            ["2", "2", "Water", "Great Value", "5", "1.00", "8", "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def insert(self, resource_id, water_size, water_container, water_type, water_exp_date):
        return resource_id

    def update(self, resource_id, water_size, water_container, water_type, water_exp_date):
        return resource_id

    def delete(self, resource_id):
        return resource_id