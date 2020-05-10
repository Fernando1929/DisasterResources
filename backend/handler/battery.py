from flask import jsonify
from dao.battery import BatteryDAO
from dao.resource import ResourceDAO
from dao.supplier import SupplierDAO
from dao.user import UserDAO

class BatteryHandler:

    def build_battery_dict(self, row): 
        result = {}
        result['resource_id'] = row[0]
        result['supplier_id'] = row[1]
        result['category_id'] = row[2]
        result['battery_name'] = row[3]
        result['battery_brand'] = row[4]
        result['battery_quantity'] = row[5]
        result['battery_price'] = row[6]
        result['battery_id'] = row[7]
        result['power_capacity'] = row[8]
        result['power_condition'] = row[9]
        result['battery_type'] = row[10]
        return result

    def build_address_dic(self,row):
        result = {}
        result['address_id'] = row[0]
        result['user_id'] = row[1]
        result['Addressline'] = row[2]
        result['city'] = row[3]
        result['state_province'] = row[4]
        result['country'] = row[5]
        result['zipcode'] = row[6]
        return result

    def build_battery_attributes(self, supplier_id, resource_id, battery_id, category_id, battery_name, battery_brand, battery_quantity, battery_price, power_capacity, power_condition, battery_type):
        result = {}
        result['supplier_id'] = supplier_id
        result['resource_id'] = resource_id
        result['battery_id'] = battery_id 
        result['category_id']  = category_id
        result['battery_name'] = battery_name 
        result['battery_brand'] = battery_brand
        result['battery_quantity'] = battery_quantity
        result['battery_price'] = battery_price 
        result['power_capacity'] = power_capacity  
        result['power_condition'] = power_condition
        result['battery_type'] = battery_type
        return result

    def getAllBatteries(self): 
        dao = BatteryDAO()
        result = dao.getAllBatteries()
        result_list = []
        for row in result:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Batteries = result_list)

    def getAllAvailableBatteries(self): 
        dao = BatteryDAO()
        result = dao.getAllAvailableBatteries()
        result_list = []
        for row in result:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Batteries = result_list)

    def getAllReservedBatteries(self): 
        dao = BatteryDAO()
        result = dao.getAllReservedBatteries()
        result_list = []
        for row in result:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Batteries = result_list)

    # def getAllRequestedBatteries(self): 
    #     dao = BatteryDAO()
    #     result = dao.getAllRequestedBatteries()
    #     result_list = []
    #     for row in result:
    #         result = self.build_battery_dict(row)
    #         result_list.append(result)
    #     return jsonify(Batteries = result_list)

    def getBatteryById(self, battery_id): 
        dao = BatteryDAO()
        row = dao.getBatteryById(battery_id)
        if not row:
            return jsonify(Error = "Battery Not Found"), 404
        else:
            battery = self.build_battery_dict(row)
            return jsonify(Battery = battery)

    def getBatteryByResourceId(self, resource_id): 
        dao = BatteryDAO()
        row = dao.getBatteryByResourceId(resource_id)
        if not row:
            return jsonify(Error = "Battery Not Found"), 404
        else:
            battery = self.build_battery_dict(row)
            return jsonify(Battery = battery)

    def getBatteriesBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            battery_dao = BatteryDAO()
            result_list = []
            battery_list = battery_dao.getBatteriesBySupplierId(supplier_id)
            for row in battery_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
            return jsonify(Batteries = result_list)

    def getAllAvailableBatteriesBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            battery_dao = BatteryDAO()
            result_list = []
            battery_list = battery_dao.getAllAvailableBatteriesBySupplierId(supplier_id)
            for row in battery_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
            return jsonify(Batteries = result_list)

    def getAllReservedBatteriesBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            battery_dao = BatteryDAO()
            result_list = []
            battery_list = battery_dao.getAllReservedBatteriesBySupplierId(supplier_id)
            for row in battery_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
            return jsonify(Batteries = result_list)
    
    # def getAllRequestedBatteriesBySupplierId(self, supplier_id):
    #     supplier_dao = SupplierDAO()
    #     if not supplier_dao.getSupplierById(supplier_id):
    #         return jsonify(Error = "Supplier Not Found"), 404
    #     else:
    #         battery_dao = BatteryDAO()
    #         result_list = []
    #         battery_list = battery_dao.getAllRequestedBatteriesBySupplierId(supplier_id)
    #         for row in battery_list:
    #             result = self.build_battery_dict(row)
    #             result_list.append(result)
    #         return jsonify(Batteries = result_list)

    def searchBatteries(self, args): 
        battery_power_capacity = args.get('power_capacity')
        battery_power_condition = args.get('power_condition')
        battery_type = args.get('battery_type')
        dao = BatteryDAO()
        battery_list = []
        if (len(args) == 1) and battery_power_capacity:
            battery_list = dao.getBatteriesByPowerCapacity(battery_power_capacity)
        elif (len(args) == 1) and battery_power_condition:
            battery_list = dao.getBatteriesByPowerCondition(battery_power_condition)
        elif (len(args) == 1) and battery_type:
            battery_list = dao.getBatteriesByType(battery_type)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Batteries = result_list)
    
    def getBatteryAddress(self, battery_id):
        battery_dao = BatteryDAO()
        supplier_id = battery_dao.getBatteryById(battery_id)[2]
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            row = battery_dao.getBatteryAddress(supplier_id)
            if not row:
                return jsonify(Error = "Address not found."), 404
            else:
                address = self.build_address_dic(row)
                return jsonify(Address = address)

    def insertBattery(self, json):
        supplier_id = json['supplier_id']
        category_id = json['category_id']
        battery_name = json['battery_name'] 
        battery_brand = json['battery_brand'] 
        battery_quantity = json['battery_quantity'] 
        battery_price = json['battery_price'] 
        power_capacity = json['power_capacity'] 
        power_condition =json['power_condition'] 
        battery_type =json['battery_type']

        if supplier_id and category_id and battery_name and battery_brand and battery_quantity and battery_price and power_capacity and power_condition and battery_type:
            res_dao = ResourceDAO()
            resource_id = res_dao.insert(supplier_id, category_id, battery_name, battery_brand, battery_quantity, battery_price)
            battery_dao = BatteryDAO()
            battery_id = battery_dao.insert(resource_id, power_capacity, power_condition, battery_type)
            result = self.build_battery_attributes(supplier_id, resource_id, battery_id, category_id, battery_name, battery_brand, battery_quantity, battery_price, power_capacity, power_condition, battery_type)
            return jsonify(Battery = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteBaterry(self, battery_id):
        battery_dao = BatteryDAO()
        if not battery_dao.getBatteryById(battery_id):
            return jsonify(Error = "Battery not found."), 404
        else:
            resource_id = battery_dao.delete(battery_id)
            res_dao = ResourceDAO()
            res_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateBattery(self, battery_id, json):
        battery_dao = BatteryDAO()
        if not battery_dao.getBatteryById(battery_id):
            return jsonify(Error = "Battery not found."), 404
        else:
            supplier_id = json['supplier_id']
            category_id = json['category_id']
            battery_name = json['battery_name'] 
            battery_brand = json['battery_brand']
            battery_quantity = json['battery_quantity']
            battery_price = json['battery_price']
            power_capacity = json['power_capacity']
            power_condition = json['power_condition']
            battery_type = json['battery_type']

            if supplier_id and category_id and battery_name and battery_brand and battery_quantity and battery_price and power_capacity and power_condition and battery_type:
                resource_id = battery_dao.update(battery_id, power_capacity, power_condition, battery_type)
                res_dao = ResourceDAO()
                res_dao.update(resource_id, supplier_id, category_id, battery_name, battery_brand, battery_quantity, battery_price)
                result = self.build_battery_attributes(supplier_id, resource_id, battery_id, category_id, battery_name, battery_brand, battery_quantity, battery_price, power_capacity, power_condition, battery_type)
                return jsonify(Battery = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400
