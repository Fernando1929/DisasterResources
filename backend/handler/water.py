from flask import jsonify
from dao.water import WaterDAO
from dao.resource import ResourceDAO
from dao.user import UserDAO
from dao.supplier import SupplierDAO

class WaterHandler:

    def build_water_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['water_id'] = row[1]
        result['water_size'] = row[2]
        result['water_container'] = row[3]
        result['water_type'] = row[4]
        result['water_exp_date'] = row[5]
        result['supplier_id'] = row[6]
        result['category_id'] = row[7]
        result['water_name'] = row[8]
        result['water_brand'] = row[9]
        result['water_quantity'] = row[10]
        result['water_price'] = row[11]
        return result

    def build_water_attributes(self, water_id, resource_id, supplier_id, category_id, water_name, water_brand, water_quantity, water_price, water_size, water_container, water_type, water_exp_date):
        result = {}
        result['water_id'] = water_id
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        result['category_id'] = category_id
        result['water_name'] = water_name
        result['water_brand'] = water_brand
        result['water_quantity'] = water_quantity
        result['water_price'] = water_price
        result['water_size'] = water_size
        result['water_container'] = water_container
        result['water_type'] = water_type
        result['water_exp_date'] = water_exp_date
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

    def getAllWaters(self):
        dao = WaterDAO()
        water_list = dao.getAllWaters()
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Waters = result_list)

    def getAllAvailableWaters(self):
        dao = WaterDAO()
        water_list = dao.getAllAvailableWaters()
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Waters = result_list)

    def getAllReservedWaters(self):
        dao = WaterDAO()
        water_list = dao.getAllReservedWaters()
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Waters = result_list)

    # def getAllRequestedWaters(self):
    #     dao = WaterDAO()
    #     water_list = dao.getAllRequestedWaters()
    #     result_list = []
    #     for row in water_list:
    #         result = self.build_water_dict(row)
    #         result_list.append(result)
    #     return jsonify(Waters = result_list)

    def getWaterById(self, water_id):
        dao = WaterDAO()
        row = dao.getWaterById(water_id)
        if not row:
            return jsonify(Error = "Water Not Found"), 404
        else:
            water = self.build_water_dict(row)
            return jsonify(Water = water)

    def getWaterByResourceId(self, resource_id):
        dao = WaterDAO()
        row = dao.getWaterByResourceId(resource_id)
        if not row:
            return jsonify(Error = "Water Not Found"), 404
        else:
            water = self.build_water_dict(row)
            return jsonify(Water = water)

    def getWatersBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            water_list = []
            result_list = []
            water_dao = WaterDAO()
            water_list = water_dao.getWatersBySupplierId(supplier_id)
            for row in water_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Waters = result_list)

    def getAllAvailableWatersBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            water_list = []
            result_list = []
            water_dao = WaterDAO()
            water_list = water_dao.getAllAvailableWatersBySupplierId(supplier_id)
            for row in water_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Waters = result_list)

    def getAllReservedWatersBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            water_list = []
            result_list = []
            water_dao = WaterDAO()
            water_list = water_dao.getAllReservedWatersBySupplierId(supplier_id)
            for row in water_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Waters = result_list)

    # def getAllRequestedWatersBySupplierId(self, supplier_id):
    #     supplier_dao = SupplierDAO()
    #     if not supplier_dao.getSupplierById(supplier_id):
    #         return jsonify(Error = "Supplier not found."), 404
    #     else:
    #         water_list = []
    #         result_list = []
    #         water_dao = WaterDAO()
    #         water_list = water_dao.getAllRequestedWatersBySupplierId(supplier_id)
    #         for row in water_list:
    #             result = self.build_water_dict(row)
    #             result_list.append(result)
    #         return jsonify(Waters = result_list)

    def searchWaters(self, args):
        water_brand = args.get("water_brand")
        water_container = args.get("water_container")
        water_type = args.get("water_type")
        dao = WaterDAO()
        water_list = []
        if (len(args) == 1) and water_brand:
            water_list = dao.getWatersByBrand(water_brand)
        elif (len(args) == 1) and water_container:
            water_list = dao.getWatersByContainer(water_container)
        elif (len(args) == 1) and water_type:
            water_list = dao.getWatersByType(water_type)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Waters = result_list)

    def getWaterAddress(self, water_id):
        water_dao = WaterDAO()
        try:
            supplier_id = water_dao.getWaterById(water_id)[6]
        except Exception:
            return jsonify(Error = "Water not found."), 404
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            row = water_dao.getWaterAddress(supplier_id)
            if not row:
                return jsonify(Error = "Address Not Found"), 404
            else:
                address = self.build_address_dict(row)
                return jsonify(Address = address)

    def insertWater(self, json):
        supplier_id = json["supplier_id"]
        category_id = json["category_id"]
        water_name = json["water_name"]
        water_brand = json["water_brand"]
        water_quantity = json["water_quantity"]
        water_price = json["water_price"]
        water_size = json["water_size"]
        water_container = json["water_container"]
        water_type = json["water_type"]
        water_exp_date = json["water_exp_date"]

        if supplier_id and category_id and water_name and water_brand and water_quantity and (water_price>=0) and water_size and water_container and water_type and water_exp_date:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, category_id, water_name, water_brand, water_quantity, water_price)
            water_dao = WaterDAO()
            water_id = water_dao.insert(resource_id, water_size, water_container, water_type, water_exp_date)
            result = self.build_water_attributes(water_id, resource_id, supplier_id, category_id, water_name, water_brand, water_quantity, water_price, water_size, water_container, water_type, water_exp_date)
            return jsonify(Water = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateWater(self, water_id, json):
        water_dao = WaterDAO()
        if not water_dao.getWaterById(water_id):
            return jsonify(Error = "Water not found."), 404
        else:
            supplier_id = json["supplier_id"]
            category_id = json["category_id"]
            water_name = json["water_name"]
            water_brand = json["water_brand"]
            water_quantity = json["water_quantity"]
            water_price = json["water_price"]
            water_size = json["water_size"]
            water_container = json["water_container"]
            water_type = json["water_type"]
            water_exp_date = json["water_exp_date"]
            
            if supplier_id and category_id and water_name and water_brand and water_quantity and (water_price>=0) and water_size and water_container and water_type and water_exp_date:
                resource_id = water_dao.update(water_id, water_size, water_container, water_type, water_exp_date)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, category_id, water_name, water_brand, water_quantity, water_price)
                result = self.build_water_attributes(water_id, resource_id, supplier_id, category_id, water_name, water_brand, water_quantity, water_price, water_size, water_container, water_type, water_exp_date)
                return jsonify(Water = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteWater(self, water_id):
        water_dao = WaterDAO()
        if not water_dao.getWaterById(water_id):
            return jsonify(Error = "Water not found."), 404
        else:
            resource_id = water_dao.delete(water_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200