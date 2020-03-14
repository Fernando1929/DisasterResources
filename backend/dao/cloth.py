class ClothDAO:
    def __init__(self):
        super().__init__()

# cloth = resource_id, supplier_id, resource_name, resource_brand, resource_quantity, resource_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type
    def getAllCloth(self):
        result = [
            ["1", "1", "Cloth", "Aeropostal", "5", "10.00", "Medium", "Cotton", "New", "M", "T-shirts"],
            ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothById(self, resource_id):
        result = ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        return result

    def getClotheByBrand(self, resource_brand):
        result = [
            ["1", "1", "Cloth", "Aeropostal", "5", "10.00", "Medium", "Cotton", "New", "M", "T-shirts"],
            ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothByCondition(self, cloth_condition):
        result = [
            ["1", "1", "Cloth", "Aeropostal", "5", "10.00", "Medium", "Cotton", "New", "M", "T-shirts"],
            ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothByGender(self, cloth_gender):
        result = [
            ["1", "1", "Cloth", "Aeropostal", "5", "10.00", "Medium", "Cotton", "New", "M", "T-shirts"],
            ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothBySize(self, cloth_size):
        result = [
            ["1", "1", "Cloth", "Aeropostal", "5", "10.00", "Medium", "Cotton", "New", "M", "T-shirts"],
            ["2", "2", "Cloth", "Adidas", "10", "15.00", "30", "Cotton", "New", "F", "Pants"]
        ]
        return result

    def getClothByType(self, cloth_type):
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

    def insert(self, resource_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type):
        return resource_id

    def update(self, resource_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type):
        return resource_id

    def delete(self, resource_id):
        return resource_id