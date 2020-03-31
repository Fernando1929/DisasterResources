class ResourceDAO:
    def __init__(self):
        super().__init__()

    # resource = resource_id, supplier_id, category, name, brand, quantity, price
    def getAllResources(self):
        result = [
            [1, 1, "fuel", "Gasoline", "Shell", 1, 20.00],
            [2, 2, "food", "Canned peaches", "Del Monte", 12, 10.00],
            [3, 3, "medicine", "Sumatriptan", "Walgreens", 1, 10.00],
            [4, 4, "tools", "Wrench", "Craftsman", 5, 40.00],
            [5, 5, "battery", 'Battery', 'Duracel', 10, 7.00],
            [6, 6, "cloth", "Cloth", "Aeropostal", 5, 10.00],
            [7, 7, "generator", 'generator', 'WEN', 10, 300.00],
            [8, 8, "heavy_equipment", "Heavy Equipment", "Caterpillar", 1, 125000.00],
            [9, 9, "ice", 'ice', 'el angel', 10, 2.50],
            [10, 10, "medical_device", "Medical Device", "Forcemech", 1, 1900.00],
            [11, 11, "water", "Water", "Nikini", 10, 1.00]
        ]
        return result

    def getResourceById(self, resource_id):
        # result = [1, 1, "fuel", "Gasoline", "Shell", 1, 20.00]
        # result = [2, 2, "food", "Canned peaches", "Del Monte", 12, 10.00]
        # result = [3, 3, "medicine", "Sumatriptan", "Walgreens", 1, 10.00]
        # result = [4, 4, "tools", "Wrench", "Craftsman", 5, 40.00]
        # result = [5, 5, "battery", 'Battery', 'Duracel', 10, 7.00]
        # result = [6, 6, "cloth", "Cloth", "Aeropostal", 5, 10.00]
        # result = [7, 7, "generator", 'generator', 'WEN', 10, 300.00]
        # result = [8, 8, "heavy_equipment", "Heavy Equipment", "Caterpillar", 1, 125000.00]
        # result = [9, 9, "ice", 'ice', 'el angel', 10, 2.50]
        # result = [10, 10, "medical_device", "Medical Device", "Forcemech", 1, 1900.00]
        result = [11, 11, "water", "Water", "Nikini", 10, 1.00]
        return result

    def insert(self, supplier_id, category, name, brand, quantity, price):
        resource_id = 1
        return resource_id

    def update(self, resource_id, supplier_id, category, name, brand, quantity, price):
        return resource_id

    def delete(self, resource_id):
        return resource_id