class ResourceDAO:
    def _init_(self):
        super()._init_()

    # resource = resource_id, supplier_id, category, name, brand, quantity, price
    def getAllResources(self):
        result = [
            [1, 1, "fuel", "Gasoline", "Shell", 1, 20.00],
            [2, 2, "food", "Canned peaches", "Del Monte", 12, 10.00],
            [3, 3, "medicine", "Sumatriptan", "Walgreens", 1, 10.00],
            [4, 4, "tools", "Wrench", "Craftsman", 5, 40.00]
        ]
        return result

    def getResourceById(self, resource_id):
        result = [1, 1, "fuel", "Gasoline", "Shell", 1, 20.00]
        # result = [2, 2, "food", "Canned peaches", "Del Monte", 12, 10.00]
        # result = [3, 3, "medicine", "Sumatriptan", "Walgreens", 1, 10.00]
        # result = [4, 4, "tools", "Wrench", "Craftsman", 5, 40.00]
        return result

    def insert(self, supplier_id, name, brand, quantity, price):
        resource_id = 1
        return resource_id

    def update(self, resource_id, supplier_id, name, brand, quantity, price):
        return resource_id

    def delete(self, resource_id):
        return resource_id