from flask import jsonify
from dao.water import WaterDAO
from dao.resource import ResourceDAO

class WaterHandler:
    def build_water_dict(self, row):
        result = {}
        result['water_id'] = row[0]
        result['supplier_id'] = row[1]
        result['water_name'] = row[2]
        result['water_brand'] = row[3]
        result['water_quantity'] = row[4]
        result['water_price'] = row[5]
        result['water_size'] = row[6]
        result['water_container'] = row[7]
        result['water_type'] = row[8]
        result['water_exp_date'] = row[9]
        return result

    def build_water_attributes(self, water_id, supplier_id, water_name, water_brand, water_quantity, water_price, water_size, water_container, water_type, water_exp_date):
        result = {}
        result['water_id'] = water_id
        result['supplier_id'] = supplier_id
        result['water_name'] = water_name
        result['water_brand'] = water_brand
        result['water_quantity'] = water_quantity
        result['water_price'] = water_price
        result['water_size'] = water_size
        result['water_container'] = water_container
        result['water_type'] = water_type
        result['water_exp_date'] = water_exp_date
        return result

    def getAllWater(self):
        dao = WaterDAO()
        water_list = dao.getAllWater()
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Waters = result_list)

    def getWaterById(self, water_id):
        dao = WaterDAO()
        row = dao.getWaterById(water_id)
        if not row:
            return jsonify(Error = "Water Not Found"), 404
        else:
            water = self.build_water_dict(row)
            return jsonify(Water = water)

    def getWaterBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:
            water_list = []
            result_list = []
            water_dao = WaterDAO()
            water_list = water_dao.getWaterBySupplierId(supplier_id)
            for row in water_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Water = result_list)

    def searchWater(self, args):
        water_brand = args.get("water_brand")
        water_container = args.get("water_container")
        water_type = args.get("water_type")
        dao = WaterDAO()
        water_list = []
        if (len(args) == 1) and water_brand:
            water_list = dao.getWaterByBrand(water_brand)
        elif (len(args) == 1) and water_container:
            water_list = dao.getWaterByContainer(water_container)
        elif (len(args) == 1) and water_type:
            water_list = dao.getWaterByType(water_type)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Water = result_list)

    def insertWater(self, json):
        supplier_id = json["supplier_id"]
        water_name = json["water_name"]
        water_brand = json["water_brand"]
        water_quantity = json["water_quantity"]
        water_price = json["water_price"]
        water_size = json["water_size"]
        water_container = json["water_container"]
        water_type = json["water_type"]
        water_exp_date = json["water_exp_date"]
        if supplier_id and water_name and water_brand and water_quantity and water_price and water_size and water_container and water_type and water_exp_date:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, water_name, water_brand, water_quantity, water_price)
            water_dao = WaterDAO()
            water_id = water_dao.insert(resource_id, water_size, water_container, water_type, water_exp_date)
            result = self.build_water_attributes(resource_id, supplier_id, water_name, water_brand, water_quantity, water_price, water_size, water_container, water_type, water_exp_date)
            return jsonify(Water = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateWater(self, water_id, json):
        water_dao = WaterDAO()
        if not water_dao.getWaterById(water_id):
            return jsonify(Error = "Water not found."), 404
        else:
            supplier_id = json["supplier_id"]
            water_name = json["water_name"]
            water_brand = json["water_brand"]
            water_quantity = json["water_quantity"]
            water_price = json["water_price"]
            water_size = json["water_size"]
            water_container = json["water_container"]
            water_type = json["water_type"]
            water_exp_date = json["water_exp_date"]
            if water_name and water_brand and water_quantity and water_price and water_size and water_container and water_type and water_exp_date:
                resource_id = water_dao.update(water_id, water_size, water_container, water_type, water_exp_date)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, water_name, water_brand, water_quantity, water_price)
                # Need to find supplier_id
                result = self.build_water_attributes(resource_id, supplier_id, water_name, water_brand, water_quantity, water_price, water_size, water_container, water_type, water_exp_date)
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