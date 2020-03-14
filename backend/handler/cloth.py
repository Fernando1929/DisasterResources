from flask import jsonify
from dao.cloth import ClothDAO
from dao.resource import ResourceDAO

# cloth = resource_id, supplier_id, resource_name, resource_brand, resource_quantity, resource_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type

class ClothHandler:
    def build_cloth_dict(self, row):
        result = {}
        result['cloth_id'] = row[0]
        result['supplier_id'] = row[1]
        result['cloth_name'] = row[2]
        result['cloth_brand'] = row[3]
        result['cloth_quantity'] = row[4]
        result['cloth_price'] = row[5]
        result['cloth_size'] = row[6]
        result['cloth_material'] = row[7]
        result['cloth_condition'] = row[8]
        result['cloth_gender'] = row[9]
        result['cloth_type'] = row[10]
        return result

    def build_water_attributes(self, cloth_id, supplier_id, cloth_name, cloth_brand, cloth_quantity, cloth_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type):
        result = {}
        result['cloth_id'] = cloth_id
        result['supplier_id'] = supplier_id
        result['cloth_name'] = cloth_name
        result['cloth_brand'] = cloth_brand
        result['cloth_quantity'] = cloth_quantity
        result['cloth_price'] = cloth_price
        result['cloth_size'] = cloth_size
        result['cloth_material'] = cloth_material
        result['cloth_condition'] = cloth_condition
        result['cloth_gender'] = cloth_gender
        result['cloth_type'] = cloth_type
        return result

    def getAllCloth(self):
        dao = ClothDAO()
        cloth_list = dao.getAllCloth()
        result_list = []
        for row in cloth_list:
            result = self.build_cloth_dict(row)
            result_list.append(result)
        return jsonify(Cloth = result_list)

    def getClothById(self, cloth_id):
        dao = ClothDAO()
        row = dao.getWaterById(cloth_id)
        if not row:
            return jsonify(Error = "Cloth Not Found"), 404
        else:
            cloth = self.build_cloth_dict(row)
            return jsonify(Water = cloth)

    def getWaterBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:
            cloth_list = []
            result_list = []
            cloth_dao = ClothDAO()
            cloth_list = cloth_dao.getClothBySupplierId(supplier_id)
            for row in cloth_list:
                result = self.build_cloth_dict(row)
                result_list.append(result)
            return jsonify(Cloth = result_list)

    def searchCloth(self, args):
        cloth_brand = args.get("cloth_brand")
        cloth_gender = args.get("cloth_gender")
        cloth_type = args.get("cloth_type")
        dao = ClothDAO()
        cloth_list = []
        if (len(args) == 1) and cloth_brand:
            cloth_list = dao.getClothByBrand(cloth_brand)
        elif (len(args) == 1) and cloth_gender:
            cloth_list = dao.getClothByGender(cloth_gender)
        elif (len(args) == 1) and cloth_type:
            cloth_list = dao.getClothByType(cloth_type)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in cloth_list:
            result = self.build_cloth_dict(row)
            result_list.append(result)
        return jsonify(Cloth = result_list)

    def insertCloth(self, json):
        supplier_id = json["supplier_id"]
        cloth_name = json["cloth_name"]
        cloth_brand = json["cloth_brand"]
        cloth_quantity = json["cloth_quantity"]
        cloth_price = json["cloth_price"]
        cloth_size = json["cloth_size"]
        cloth_material = json["cloth_material"]
        cloth_condition = json["cloth_condition"]
        cloth_gender = json["cloth_gender"]
        cloth_type = json["cloth_type"]
        if supplier_id and cloth_name and cloth_brand and cloth_quantity and cloth_price and cloth_size and cloth_material and cloth_condition and cloth_gender and cloth_type:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, cloth_name, cloth_brand, cloth_quantity, cloth_price)
            cloth_dao = ClothDAO()
            cloth_id = cloth_dao.insert(resource_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type)
            result = self.build_cloth_attributes(resource_id, supplier_id, cloth_name, cloth_brand, cloth_quantity, cloth_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type)
            return jsonify(Cloth = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateCloth(self, cloth_id, json):
        cloth_dao = ClothDAO()
        if not cloth_dao.getClothById(cloth_id):
            return jsonify(Error = "Cloth not found."), 404
        else:
            supplier_id = json["supplier_id"]
            cloth_name = json["cloth_name"]
            cloth_brand = json["cloth_brand"]
            cloth_quantity = json["cloth_quantity"]
            cloth_price = json["cloth_price"]
            cloth_size = json["cloth_size"]
            cloth_material = json["cloth_material"]
            cloth_condition = json["cloth_condition"]
            cloth_gender = json["cloth_gender"]
            cloth_type = json["cloth_type"]
            if cloth_name and cloth_brand and cloth_quantity and cloth_price and cloth_size and cloth_material and cloth_condition and cloth_gender and cloth_type:
                resource_id = cloth_dao.update(cloth_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, cloth_name, cloth_brand, cloth_quantity, cloth_price)
                result = self.build_cloth_attributes(resource_id, supplier_id, cloth_name, cloth_brand, cloth_quantity, cloth_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type)
                return jsonify(Cloth = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteCloth(self, cloth_id):
        cloth_dao = ClothDAO()
        if not cloth_dao.getWaterById(cloth_id):
            return jsonify(Error = "Cloth not found."), 404
        else:
            resource_id = cloth_dao.delete(cloth_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200