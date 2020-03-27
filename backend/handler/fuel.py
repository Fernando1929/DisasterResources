from flask import jsonify
from dao.resource import ResourceDAO
from dao.fuel import FuelDAO

class FuelHandler:
    def build_fuel_dict(self, row):
        result = {}
        result['fuel_id'] = row[0]
        result['resource_id'] = row[1]
        result['supplier_id'] = row[2]
        result['fuel_name'] = row[3]
        result['fuel_brand'] = row[4]
        result['fuel_quantity'] = row[5]
        result['fuel_price'] = row[6]
        result['fuel_type'] = row[7]
        result['fuel_gallons'] = row[8]
        return result

    def build_fuel_attributes(self, fuel_id, resource_id, supplier_id, fuel_name, fuel_brand, fuel_quantity, fuel_price, fuel_type, fuel_gallons):
        result = {}
        result['fuel_id'] = fuel_id
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        result['fuel_name'] = fuel_name
        result['fuel_brand'] = fuel_brand
        result['fuel_quantity'] = fuel_quantity
        result['fuel_price'] = fuel_price
        result['fuel_type'] = fuel_type
        result['fuel_gallons'] = fuel_gallons
        return result

    def getAllFuels(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuels()
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuels = result_list)

    def getAllAvailableFuels(self):
        dao = FuelDAO()
        fuel_list = dao.getAllAvailableFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel = result_list)

    def getAllReservedFuels(self):
        dao = FuelDAO()
        fuel_list = dao.getAllReservedFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel = result_list)

    def getFuelById(self, fuel_id):
        dao = FuelDAO()
        row = dao.getFuelById(fuel_id)
        if not row:
            return jsonify(Error = "Fuel Not Found"), 404
        else:
            fuel = self.build_fuel_dict(row)
            return jsonify(Fuel = fuel)

    def getFuelBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:

        fuel_list = []
        result_list = []
        fuel_dao = FuelDAO()
        fuel_list = fuel_dao.getFuelsBySupplierId(supplier_id)
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel = result_list)

    def getAllAvailableFuelBySupplierId(self, supplier_id):
        fuel_list = []
        result_list = []
        fuel_dao = FuelDAO()
        fuel_list = fuel_dao.getAllAvailableFuelBySupplierId(supplier_id)
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel = result_list)

    def getAllReservedFuelBySupplierId(self, supplier_id):
        fuel_list = []
        result_list = []
        fuel_dao = FuelDAO()
        fuel_list = fuel_dao.getAllReservedFuelBySupplierId(supplier_id)
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel = result_list)

    def searchFuel(self, args):
        fuel_brand = args.get("fuel_brand")
        fuel_type = args.get("fuel_type")
        fuel_gallons = args.get("fuel_gallons")
        dao = FuelDAO()
        fuel_list = []
        if (len(args) == 1) and fuel_brand:
            fuel_list = dao.getFuelByBrand(fuel_brand)
        elif (len(args) == 1) and fuel_type:
            fuel_list = dao.getFuelsByType(fuel_type)
        elif (len(args) == 1) and fuel_gallons:
            fuel_list = dao.getFuelsByGallons(fuel_gallons)
        elif (len(args) == 2) and fuel_type and fuel_gallons:
            fuel_list = dao.getFuelsByTypeAndGallons(fuel_type, fuel_gallons)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel = result_list)

    def insertFuel(self, json):
        supplier_id = json["supplier_id"]
        fuel_name = json["fuel_name"]
        fuel_brand = json["fuel_brand"]
        fuel_quantity = json["fuel_quantity"]
        fuel_price = json["fuel_price"]
        fuel_type = json["fuel_type"]
        fuel_gallons = json["fuel_gallons"]

        if supplier_id and fuel_name and fuel_brand and fuel_quantity and fuel_price and fuel_type and fuel_gallons:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, fuel_name, fuel_brand, fuel_quantity, fuel_price)
            fuel_dao = FuelDAO()
            fuel_id = fuel_dao.insert(resource_id, fuel_type, fuel_gallons)
            result = self.build_fuel_attributes(fuel_id, resource_id, supplier_id, fuel_name, fuel_brand, fuel_quantity, fuel_price, fuel_type, fuel_gallons)
            return jsonify(Fuel = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateFuel(self, fuel_id, json):
        fuel_dao = FuelDAO()
        if not fuel_dao.getFuelById(fuel_id):
            return jsonify(Error = "Fuel not found."), 404
        else:
            supplier_id = json["supplier_id"]
            fuel_name = json["fuel_name"]
            fuel_brand = json["fuel_brand"]
            fuel_quantity = json["fuel_quantity"]
            fuel_price = json["fuel_price"]
            fuel_type = json["fuel_type"]
            fuel_gallons = json["fuel_gallons"]

            if supplier_id and fuel_name and fuel_brand and fuel_quantity and fuel_price and fuel_type and fuel_gallons:
                resource_id = fuel_dao.update(fuel_id, fuel_type, fuel_gallons)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, fuel_name, fuel_brand, fuel_quantity, fuel_price)

                result = self.build_fuel_attributes(fuel_id, resource_id, supplier_id, fuel_name, fuel_brand, fuel_quantity, fuel_price, fuel_type, fuel_gallons)
                return jsonify(Fuel = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteFuel(self, fuel_id):
        fuel_dao = FuelDAO()
        if not fuel_dao.getFuelById(fuel_id):
            return jsonify(Error = "Fuel not found."), 404
        else:
            resource_id = fuel_dao.delete(fuel_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200