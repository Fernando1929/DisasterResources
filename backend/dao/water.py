class WaterDAO:
    def __init__(self):
        super().__init__()

# water = water_id, supplier_id, water_name, water_brand, water_quantity, water_price, water_size, water_container, water_type, water_exp_date
    def getAllWater(self):
        result = [
            ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"],
            ["2", "2", "Water", "Great Value", "5", "1.00", "8", "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterById(self, resource_id):
        result = ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"]
        return result

    def getWaterByBrand(self, resource_brand):
        result = [
            ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"],
            ["2", "2", "Water", "Great Value", "5", "1.00", "8", "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterByContainer(self, water_container):
        result = [
            ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"],
            ["2", "2", "Water", "Great Value", "5", "1.00", "8", "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterByType(self, water_container):
        result = [
            ["1", "1", "Water", "Nikini", "10", "1.00", "16", "Bottle", "Purified", "02/12/2022"],
            ["2", "2", "Water", "Great Value", "5", "1.00", "8", "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterBySupplierId(self, supplier_id):
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