class ClothDAO:
    def __init__(self):
        super().__init__()

    # cloth = cloth id, resource id, user id, name, brand, quantity, price, size, material, condition, gender, type

    def getAllCloth(self):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllAvailableCloth(self):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllReservedCloth(self):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothById(self, resource_id):
        result = [2, 2, 2, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        return result

    def getClothByBrand(self, resource_brand):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothByCondition(self, cloth_condition):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothByGender(self, cloth_gender):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothBySize(self, cloth_size):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothByType(self, cloth_type):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 2, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllAvailableClothBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 10.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 1, "Cloth", "Adidas", 10, 15.00, "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getAllReservedClothBySupplierId(self, supplier_id):
        result = [
            [1, 1, 1, "Cloth", "Aeropostal", 5, 0.00, "Medium", "Cotton", "New", "M", "T-shirts"],
            [2, 2, 1, "Cloth", "Adidas", 10, 0.00, "30", "Cotton", "New", "F", "Pants"]
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