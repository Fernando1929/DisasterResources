class HeavyEquipDAO:
    def __init__(self):
        super().__init__()

    def getAllHeavyEquip(self):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 125000.00, "Excavator", "320D", "Used"],
            [2, 2, 2, "Heavy Equipment", "Clark", 1, 1500.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getAllAvailableHeavyEquip(self):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 125000.00, "Excavator", "320D", "Used"],
            [2, 2, 2, "Heavy Equipment", "Clark", 1, 1500.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getAllReservedHeavyEquip(self):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 0.00, "Excavator", "320D", "Used"],
            [2, 2, 2, "Heavy Equipment", "Clark", 1, 0.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getAllRequestedHeavyEquip(self):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 0.00, "Excavator", "320D", "Used"],
            [2, 2, 2, "Heavy Equipment", "Clark", 1, 0.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getHeavyEquipById(self, heavyequip_id):
        result = [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 125000.00, "Excavator", "320D", "Used"]
        return result

    def getHeavyEquipByResourceId(self, resource_id):
        result = [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 125000.00, "Excavator", "320D", "Used"]
        return result

    def getHeavyEquipByBrand(self, resource_brand):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 125000.00, "Excavator", "320D", "Used"],
            [2, 2, 2, "Heavy Equipment", "Clark", 1, 1500.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getHeavyEquipByCondition(self, heavyequip_condition):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 125000.00, "Excavator", "320D", "Used"],
            [2, 2, 2, "Heavy Equipment", "Clark", 1, 1500.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getHeavyEquipByType(self, heavyequip_type):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 125000.00, "Excavator", "320D", "Used"],
            [2, 2, 2, "Heavy Equipment", "Clark", 1, 1500.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getHeavyEquipBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 125000.00, "Excavator", "320D", "Used"],
            [2, 2, 2, "Heavy Equipment", "Clark", 1, 1500.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getAllAvailableHeavyEquipBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 125000.00, "Excavator", "320D", "Used"],
            [2, 2, 1, "Heavy Equipment", "Clark", 1, 1500.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getAllReservedHeavyEquipBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 0.00, "Excavator", "320D", "Used"],
            [2, 2, 1, "Heavy Equipment", "Clark", 1, 0.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getAllRequestedHeavyEquipBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Heavy Equipment", "Caterpillar", 1, 0.00, "Excavator", "320D", "Used"],
            [2, 2, 1, "Heavy Equipment", "Clark", 1, 0.00, "Elevator", "EC500-800 Type E", "Used"]
        ]
        return result

    def getHeavyEquipAddress(self, user_id):
        result = [1, 1, "Barrio Las Palmas", "Utuado", "PR", "US", "00641"]
        return result

    def insert(self, resource_id, heavyequip_type, heavyequip_model, heavyequip_condition):
        hequip_id = 1
        return hequip_id

    def update(self, hequip_id, heavyequip_type, heavyequip_model, heavyequip_condition):
        resource_id = 1
        return resource_id

    def delete(self, equip_id):
        resource_id = 1
        return resource_id