from flask import jsonify
from dao.cloth import ClothDAO
from dao.resource import ResourceDAO
from dao.user import UserDAO

class ClothHandler:
    def build_cloth_dict(self, row):
        result = {}
        result['cloth_id'] = row[0]
        result['resource_id'] = row[1]
        result['supplier_id'] = row[2]
        result['cloth_name'] = row[3]
        result['cloth_brand'] = row[4]
        result['cloth_quantity'] = row[5]
        result['cloth_price'] = row[6]
        result['cloth_size'] = row[7]
        result['cloth_material'] = row[8]
        result['cloth_condition'] = row[9]
        result['cloth_gender'] = row[10]
        result['cloth_type'] = row[11]
        return result

    def build_cloth_attributes(self, cloth_id, resource_id, supplier_id, cloth_name, cloth_brand, cloth_quantity, cloth_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type):
        result = {}
        result['cloth_id'] = cloth_id
        result['resource_id'] = resource_id
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

    def build_address_dict(self, row):
        result = {}
        result["address_id"] = row[0]
        result["user_id"] = row[1]
        result["address_line"] = row[2]
        result["address_city"] = row[3]
        result["address_state_province"] = row[4]
        result["address_country"] = row[5]
        result["address_zipcode"] = row[6]
        return result


    def getAllCloth(self):
        dao = ClothDAO()
        cloth_list = dao.getAllCloth()
        result_list = []
        for row in cloth_list:
            result = self.build_cloth_dict(row)
            result_list.append(result)
        return jsonify(Cloth = result_list)

    def getAllAvailableCloth(self):
        dao = ClothDAO()
        cloth_list = dao.getAllAvailableCloth()
        result_list = []
        for row in cloth_list:
            result = self.build_cloth_dict(row)
            result_list.append(result)
        return jsonify(Cloth = result_list)

    def getAllReservedCloth(self):
        dao = ClothDAO()
        cloth_list = dao.getAllReservedCloth()
        result_list = []
        for row in cloth_list:
            result = self.build_cloth_dict(row)
            result_list.append(result)
        return jsonify(Cloth = result_list)

    def getClothById(self, cloth_id):
        dao = ClothDAO()
        row = dao.getClothById(cloth_id)
        if not row:
            return jsonify(Error = "Cloth Not Found"), 404
        else:
            cloth = self.build_cloth_dict(row)
            return jsonify(Cloth = cloth)

    def getClothBySupplierId(self, supplier_id):
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

    def getAllAvailableClothBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:
            cloth_list = []
            result_list = []
            cloth_dao = ClothDAO()
            cloth_list = cloth_dao.getAllAvailableClothBySupplierId(supplier_id)
            for row in cloth_list:
                result = self.build_cloth_dict(row)
                result_list.append(result)
            return jsonify(Cloth = result_list)

    def getAllReservedClothBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:
            cloth_list = []
            result_list = []
            cloth_dao = ClothDAO()
            cloth_list = cloth_dao.getAllReservedClothBySupplierId(supplier_id)
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

    def getClothAddress(self, cloth_id):
        cloth_dao = ClothDAO()
        user_id = cloth_dao.getClothById(cloth_id)[2]
        user_dao = UserDAO()
        if not user_dao.getUserById(user_id):
            return jsonify(Error = "User not found."), 404
        else:
            row = cloth_dao.getClothAddress(user_id)
            if not row:
                return jsonify(Error = "Address Not Found"), 404
            else:
                address = self.build_address_dict(row)
                return jsonify(Address = address)

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
            result = self.build_cloth_attributes(cloth_id, resource_id, supplier_id, cloth_name, cloth_brand, cloth_quantity, cloth_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type)
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
                resource_dao.update(resource_id, supplier_id, cloth_name, cloth_brand, cloth_quantity, cloth_price)
                result = self.build_cloth_attributes(cloth_id, resource_id, supplier_id, cloth_name, cloth_brand, cloth_quantity, cloth_price, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type)
                return jsonify(Cloth = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteCloth(self, cloth_id):
        cloth_dao = ClothDAO()
        if not cloth_dao.getClothById(cloth_id):
            return jsonify(Error = "Cloth not found."), 404
        else:
            resource_id = cloth_dao.delete(cloth_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200