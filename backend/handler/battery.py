from flask import jsonify
from dao.battery import BatteryDAO
from dao.power import PowerDAO
from dao.resource import ResourceDAO
from dao.supplier import SupplierDAO

class BatteryHandler:

    #battery = battery_id, battery_name, battery_description, battery_brand, battery_quantity, battery_price, power_capacity, power_condition, battery_type
    def build_battery_dict(self, row): 
        result = {}
        result['supplier_id'] = row[0]
        result['resource_id'] = row[1]
        result['power_id'] = row[2]
        result['battery_id'] = row[3]
        result['battery_name'] = row[4]
        result['battery_brand'] = row[5]
        result['battery_quantity'] = row[6]
        result['battery_price'] = row[7]
        result['power_capacity'] = row[8]
        result['power_condition'] = row[9]
        result['battery_type'] = row[10]
        return result

    def build_battery_attributes(self, supplier_id, resource_id, power_id, battery_id, battery_name, battery_brand, battery_quantity,battery_price, power_capacity, power_condition, battery_type):
        result = {}
        result['supplier_id'] = supplier_id
        result['resource_id'] = resource_id
        result['power_id'] = power_id
        result['battery_id'] = battery_id 
        result['battery_name'] = battery_name 
        result['battery_brand'] = battery_brand
        result['battery_quantity'] = battery_quantity
        result['battery_price'] = battery_price 
        result['power_capacity'] = power_capacity  
        result['power_condition'] = power_condition
        result['battery_type'] = battery_type
        return result

    def getAllBattery(self): 
        dao = BatteryDAO()
        result = dao.getAllBattery()
        result_list = []
        for row in result:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Battery=result_list)

    def getAllAvailableBattery(self): 
        dao = BatteryDAO()
        result = dao.getAllAvailableBattery()
        result_list = []
        for row in result:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Battery=result_list)

    def getAllReservedBattery(self): 
        dao = BatteryDAO()
        result = dao.getAllReservedBattery()
        result_list = []
        for row in result:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Battery=result_list)

    def getBatteryById(self, resource_id): 
        dao = BatteryDAO()
        row = dao.getBatteryById(resource_id)
        if not row:
            return jsonify(Error = "Battery Not Found"), 404
        else:
            battery = self.build_battery_dict(row)
            return jsonify(Battery = battery)

    def getBatteryBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error="Supplier Not Found"), 404
        #else:
            battery_dao = BatteryDAO()
            result_list = []
            battery_list = battery_dao.getBatteryBySupplierId(supplier_id)
            for row in battery_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
            return jsonify(Ice=result_list)

    def searchBattery(self, args): 
        Battery_power_capacity = args.get('power_capacity')
        Battery_power_condition = args.get('power_condition')
        Battery_type = args.get('battery_type')
        dao = BatteryDAO()
        battery_list = []
        if (len(args) == 1) and Battery_power_capacity:
            battery_list = dao.getBatteryByPowerCapacity(Battery_power_capacity)
        elif (len(args) == 1) and Battery_power_condition:
            battery_list = dao.getBatteryByPowerCondition(Battery_power_condition)
        elif (len(args) == 1) and Battery_type:
            battery_list = dao.getBatteryByType(Battery_type)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Battery=result_list)

    def insertBattery(self, json):
        supplier_id = json['supplier_id']
        battery_name = json['battery_name'] 
        battery_brand = json['battery_brand'] 
        battery_quantity = json['battery_quantity'] 
        battery_price = json['battery_price'] 
        power_capacity = json['power_capacity'] 
        power_condition =json['power_condition'] 
        battery_type =json['battery_type'] 
        if battery_name and battery_brand and battery_quantity and battery_price and power_capacity and power_condition and battery_type:
            res_dao = ResourceDAO()
            resource_id = res_dao.insert(supplier_id, battery_name, battery_brand, battery_quantity, battery_price)
            power_dao = PowerDAO()
            power_id = power_dao.insert(resource_id, power_capacity,  power_condition)
            battery_dao = BatteryDAO()
            battery_id = battery_dao.insert(resource_id, power_id, battery_type)
            result = self.build_battery_attributes(supplier_id, resource_id, power_id, battery_id, battery_name, battery_brand, battery_quantity, battery_price, power_capacity, power_condition, battery_type)
            return jsonify(Battery=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteBaterry(self, battery_id):
        battery_dao = BatteryDAO()
        if not battery_dao.getBatteryById(battery_id):
            return jsonify(Error = "Battery not found."), 404
        else:
            power_id = battery_dao.delete(battery_id)
            power_dao = PowerDAO()
            resource_id = power_dao.delete(power_id)
            res_dao = ResourceDAO()
            res_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateBattery(self, battery_id, json):
        battery_dao = BatteryDAO()
        if not battery_dao.getBatteryById(battery_id):
            return jsonify(Error = "Battery not found."), 404
        else:
            supplier_id = json['supplier_id']
            battery_name = json['battery_name'] 
            battery_brand = json['battery_brand']
            battery_quantity = json['battery_quantity']
            battery_price = json['battery_price']
            power_capacity = json['power_capacity']
            power_condition = json['power_condition']
            battery_type = json['battery_type']
            if battery_name and battery_brand and battery_quantity and battery_price and power_capacity and power_condition and battery_type:
                res_dao = ResourceDAO()
                resource_id = res_dao.insert(supplier_id, battery_name, battery_brand, battery_quantity, battery_price)
                power_dao = PowerDAO()
                power_id = power_dao.insert(resource_id, power_capacity,  power_condition)
                battery_id = battery_dao.insert(resource_id, power_id, battery_type)
                result = self.build_battery_attributes(supplier_id, resource_id, power_id, battery_id, battery_name, battery_brand, battery_quantity, battery_price, power_capacity, power_condition, battery_type)
                return jsonify(Battery=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400
