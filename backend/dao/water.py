class WaterDAO:
    def __init__(self):
        super().__init__()

    def getAllWater(self):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllAvailableWater(self):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllReservedWater(self):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "Water", "Great Value", 5, 0.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllRequestedWater(self):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "Water", "Great Value", 5, 0.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterById(self, water_id):
        result = [1, 1, 1, "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"]
        return result

    def getWaterByResourceId(self, resource_id):
        result = [1, 1, 1, "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"]
        return result

    def getWaterByBrand(self, resource_brand):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterByContainer(self, water_container):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterByType(self, water_type):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 2, "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllAvailableWaterBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 1.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 1, "Water", "Great Value", 5, 1.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllReservedWaterBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 1, "Water", "Great Value", 5, 0.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getAllRequestedWaterBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Water", "Nikini", 10, 0.00, 16, "Bottle", "Purified", "02/12/2022"],
            [2, 2, 1, "Water", "Great Value", 5, 0.00, 8, "Bottle", "Purified", "02/24/2024"]
        ]
        return result

    def getWaterAddress(self, user_id):
        result = [1, 1, "Barrio Las Palmas", "Utuado", "PR", "US", "00641"]
        return result

    def insert(self, resource_id, water_size, water_container, water_type, water_exp_date):
        water_id = 1
        return water_id

    def update(self, water_id, water_size, water_container, water_type, water_exp_date):
        resource_id = 1
        return resource_id

    def delete(self, water_id):
        resource_id = 1
        return resource_id