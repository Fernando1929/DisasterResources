class FoodDAO:
    def __init__(self):
        super().__init__()

# food = food_id, resource_id, supplier_id, food_name, food_brand, food_quantity, food_price, 
#           food_category, food_container, food_type, food_ounces, food_expdate
    def getAllFoods(self):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getAllAvailableFood(self):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getAllReservedFood(self):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getFoodById(self, resource_id):
        result = [1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]
        return result

    def getFoodByBrand(self, resource_brand):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getFoodsByCategory(self, food_category):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getFoodsByContainer(self, food_container):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getFoodsByType(self, food_type):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getFoodsByOunces(self, food_ounces):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getFoodsByCategoryAndType(self, food_category, food_type):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getFoodsBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getAllAvailableFoodBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def getAllReservedFoodBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "Canned peaches", "Del Monte", 12, 10.00, "fruit", "aluminum", "canned", 8, "12/31/2020"]]
        return result

    def insert(self, resource_id, food_category, food_container, food_type, food_ounces, food_expdate):
        food_id = 1
        return food_id

    def delete(self, food_id):
        resource_id = 1
        return resource_id

    def update(self, food_id, food_category, food_container, food_type, food_ounces, food_expdate):
        resource_id = 1
        return resource_id
