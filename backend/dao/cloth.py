class ClothDAO:
    def __init__(self):
        super().__init__()

    # cloth = cloth_id, resource_id, supplier_id, category, cloth_name, cloth_quantity, cloth_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type

    def getAllClothes(self):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllAvailableClothes(self):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllReservedClothes(self):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllRequestedClothes(self):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothById(self, cloth_id):
        result = [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        return result

    def getClothByResourceId(self, resource_id):
        result = [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        return result

    def getClothesByBrand(self, resource_brand):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothesByCondition(self, cloth_condition):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothesByGender(self, cloth_gender):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothesBySize(self, cloth_size):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothesByType(self, cloth_type):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothesBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllAvailableClothesBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllReservedClothesBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllRequestedClothesBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "cloth", "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "cloth", "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothAddress(self, user_id):
        result = [1, 1, "Barrio Las Palmas", "Utuado", "PR", "US", "00641"]
        return result

    def insert(self, resource_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type):
        cloth_id = 1
        return cloth_id

    def update(self, cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type):
        resource_id = 1
        return resource_id

    def delete(self, cloth_id):
        resource_id = 1
        return resource_id