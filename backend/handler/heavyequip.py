from flask import jsonify
from dao.heavyequip import HeavyEquipDAO
from dao.resource import ResourceDAO

# h_equip = resource_id, supplier_id, resource_name, resource_brand, resource_quantity, resource_price, heavyequip_type, heavyequip_model, heavyequip_condition
 
class HeavyEquipHandler:
    def build_hequip_dict(self, row):
        result = {}
        result['hequip_id'] = row[0]
        result['supplier_id'] = row[1]
        result['hequip_name'] = row[2]
        result['hequip_brand'] = row[3]
        result['hequip_quantity'] = row[4]
        result['hequip_price'] = row[5]
        result['hequip_type'] = row[6]
        result['hequip_model'] = row[7]
        result['hequip_condition'] = row[8]
        return result

    def build_hequip_attributes(self, hequip_id, supplier_id, hequip_name, hequip_brand, hequip_quantity, hequip_price, hequip_type, hequip_model, hequip_condition):
        result = {}
        result['hequip_id'] = hequip_id
        result['supplier_id'] = supplier_id
        result['hequip_name'] = hequip_name
        result['hequip_brand'] = hequip_brand
        result['hequip_quantity'] = hequip_quantity
        result['hequip_price'] = hequip_price
        result['hequip_type'] = hequip_type
        result['hequip_model'] = hequip_model
        result['hequip_condition'] = hequip_condition
        return result

    def getAllHeavyEquip(self):
        dao = HeavyEquipDAO()
        hequip_list = dao.getAllHeavyEquip()
        result_list = []
        for row in hequip_list:
            result = self.build_hequip_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment = result_list)

    def getHeavyEquipById(self, hequip_id):
        dao = HeavyEquipDAO()
        row = dao.getHeavyEquipById(hequip_id)
        if not row:
            return jsonify(Error = "Heavy Equipment Not Found"), 404
        else:
            hequip = self.build_hequip_dict(row)
            return jsonify(Heavy_Equipment = hequip)

    def getHeavyEquipBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:
            hequip_list = []
            result_list = []
            hequip_dao = HeavyEquipDAO()
            hequip_list = hequip_dao.getHeavyEquipBySupplierId(supplier_id)
            for row in hequip_list:
                result = self.build_hequip_dict(row)
                result_list.append(result)
            return jsonify(Heavy_Equipment = result_list)

    def searchHeavyEquip(self, args):
        hequip_brand = args.get("hequip_brand")
        hequip_type = args.get("hequip_type")
        hequip_condition = args.get("hequip_condition")
        dao = HeavyEquipDAO()
        hequip_list = []
        if (len(args) == 1) and hequip_brand:
            hequip_list = dao.getHeavyEquipByBrand(hequip_brand)
        elif (len(args) == 1) and hequip_type:
            hequip_list = dao.getHeavyEquipByType(hequip_type)
        elif (len(args) == 1) and hequip_condition:
            hequip_list = dao.getHeavyEquipByCondition(hequip_condition)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in hequip_list:
            result = self.build_hequip_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment = result_list)

    def insertHeavyEquip(self, json):
        supplier_id = json["supplier_id"]
        hequip_name = json["hequip_name"]
        hequip_brand = json["hequip_brand"]
        hequip_quantity = json["hequip_quantity"]
        hequip_price = json["hequip_price"]
        hequip_type = json["hequip_type"]
        hequip_model = json["hequip_model"]
        hequip_condition = json["hequip_condition"]
        if supplier_id and hequip_name and hequip_brand and hequip_quantity and hequip_price and hequip_type and hequip_model and hequip_condition:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, hequip_name, hequip_brand, hequip_quantity, hequip_price)
            hequip_dao = HeavyEquipDAO()
            hequip_id = hequip_dao.insert(resource_id, hequip_type, hequip_model, hequip_condition)
            result = self.build_hequip_attributes(resource_id, supplier_id, hequip_name, hequip_brand, hequip_quantity, hequip_price, hequip_type, hequip_model, hequip_condition)
            return jsonify(Heavy_Equipment = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateHeavyEquip(self, hequip_id, json):
        hequip_dao = HeavyEquipDAO()
        if not hequip_dao.getHeavyEquipById(hequip_id):
            return jsonify(Error = "Heavy Equipment not found."), 404
        else:
            supplier_id = json["supplier_id"]
            hequip_name = json["hequip_name"]
            hequip_brand = json["hequip_brand"]
            hequip_quantity = json["hequip_quantity"]
            hequip_price = json["hequip_price"]
            hequip_type = json["hequip_type"]
            hequip_model = json["hequip_model"]
            hequip_condition = json["hequip_condition"]
            if supplier_id and hequip_name and hequip_brand and hequip_quantity and hequip_price and hequip_type and hequip_model and hequip_condition:
                resource_id = hequip_dao.update(hequip_id, hequip_type, hequip_model, hequip_condition)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, hequip_name, hequip_brand, hequip_quantity, hequip_price)
                result = self.build_hequip_attributes(resource_id, supplier_id, hequip_name, hequip_brand, hequip_quantity, hequip_price, hequip_type, hequip_model, hequip_condition)
                return jsonify(Heavy_Equipment = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteHeavyEquip(self, hequip_id):
        hequip_dao = HeavyEquipDAO()
        if not hequip_dao.getHeavyEquipById(hequip_id):
            return jsonify(Error = "Heavy Equipment not found."), 404
        else:
            resource_id = hequip_dao.delete(hequip_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200