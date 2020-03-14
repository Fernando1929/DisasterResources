class HeavyEquipDAO:
    def __init__(self):
        super().__init__()

# h_equip = resource_id, supplier_id, resource_name, resource_brand, resource_quantity, resource_price, heavyequip_type, heavyequip_model, heavyequip_condition
    def getAllHeavyEquip(self):
        result = [
            ["1", "1", "Heavy Equipment", "Caterpillar", "1", "125000.00", "Excavator", "320D", "Used"],
            ["2", "2", "Heavy Equipment", "Clark", "1", "1500.00", "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getHeavyEquipById(self, resource_id):
        result = ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        return result

    def getHeavyEquipByBrand(self, resource_brand):
        result = [
            ["1", "1", "Cloth", "Aeropostal", "5", "10.00", "Medium", "Cotton", "New", "M", "T-shirts"],
            ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getHeavyEquipByCondition(self, heavyequip_condition):
        result = [
            ["1", "1", "Cloth", "Aeropostal", "5", "10.00", "Medium", "Cotton", "New", "M", "T-shirts"],
            ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getHeavyEquipByType(self, heavyequip_type):
        result = [
            ["1", "1", "Cloth", "Aeropostal", "5", "10.00", "Medium", "Cotton", "New", "M", "T-shirts"],
            ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothBySupplierId(self, supplier_id):
        result = [
            ["1", "1", "Cloth", "Aeropostal", "5", "10.00", "Medium", "Cotton", "New", "M", "T-shirts"],
            ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def insert(self, resource_id, heavyequip_type, heavyequip_model, heavyequip_condition):
        return resource_id

    def update(self, resource_id, heavyequip_type, heavyequip_model, heavyequip_condition):
        return resource_id

    def delete(self, resource_id):
        return resource_id