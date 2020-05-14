from flask import jsonify
from dao.medDevice import MedDeviceDAO
from dao.resource import ResourceDAO
from dao.user import UserDAO
from dao.supplier import SupplierDAO

class MedDeviceHandler:

    def build_med_device_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['med_device_id'] = row[1]
        result['med_device_type'] = row[2]
        result['med_device_model'] = row[3]
        result['med_device_condition'] = row[4]
        result['med_device_power_type'] = row[5]
        result['supplier_id'] = row[6]
        result['category_id'] = row[7]
        result['med_device_name'] = row[8]
        result['med_device_brand'] = row[9]
        result['med_device_quantity'] = row[10]
        result['med_device_price'] = row[11]
        return result

    def build_med_device_attributes(self, med_device_id, resource_id, supplier_id, category_id, med_device_name, med_device_brand, med_device_quantity, med_device_price, med_device_type, med_device_model, med_device_condition, med_device_power_type):
        result = {}
        result['mdevice_id'] = med_device_id
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        result['category_id'] = category_id
        result['mdevice_name'] = med_device_name
        result['mdevice_brand'] = med_device_brand
        result['mdevice_quantity'] = med_device_quantity
        result['mdevice_price'] = med_device_price
        result['mdevice_type'] = med_device_type
        result['mdevice_model'] = med_device_model
        result['mdevice_condition'] = med_device_condition
        result['mdevice_power_type'] = med_device_power_type
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

    def getAllMedDevices(self):
        dao = MedDeviceDAO()
        med_device_list = dao.getAllMedDevices()
        result_list = []
        for row in med_device_list:
            result = self.build_med_device_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevices = result_list)

    def getAllAvailableMedDevices(self):
        dao = MedDeviceDAO()
        med_device_list = dao.getAllAvailableMedDevices()
        result_list = []
        for row in med_device_list:
            result = self.build_med_device_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevices  = result_list)

    def getAllReservedMedDevices(self):
        dao = MedDeviceDAO()
        med_device_list = dao.getAllReservedMedDevices()
        result_list = []
        for row in med_device_list:
            result = self.build_med_device_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevices = result_list)

    # def getAllRequestedMedDevices(self):
    #     dao = MedDeviceDAO()
    #     med_device_list = dao.getAllRequestedMedDevices()
    #     result_list = []
    #     for row in med_device_list:
    #         result = self.build_med_device_dict(row)
    #         result_list.append(result)
    #     return jsonify(MedicalDevices = result_list)

    def getMedDeviceById(self, med_device_id):
        dao = MedDeviceDAO()
        row = dao.getMedDeviceById(med_device_id)
        if not row:
            return jsonify(Error = "Medical Device Not Found"), 404
        else:
            mdevice = self.build_med_device_dict(row)
            return jsonify(MedicalDevice = mdevice)

    def getMedDeviceByResourceId(self, resource_id):
        dao = MedDeviceDAO()
        row = dao.getMedDeviceByResourceId(resource_id)
        if not row:
            return jsonify(Error = "Medical Device Not Found"), 404
        else:
            hequip = self.build_med_device_dict(row)
            return jsonify(MedicalDevice = hequip)

    def getMedDevicesBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            med_device_list = []
            result_list = []
            med_device_dao = MedDeviceDAO()
            med_device_list = med_device_dao.getMedDevicesBySupplierId(supplier_id)
            for row in med_device_list:
                result = self.build_med_device_dict(row)
                result_list.append(result)
            return jsonify(MedicalDevices = result_list)

    def getAllAvailableMedDevicesBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            med_device_list = []
            result_list = []
            med_device_dao = MedDeviceDAO()
            med_device_list = med_device_dao.getAllAvailableMedDevicesBySupplierId(supplier_id)
            for row in med_device_list:
                result = self.build_med_device_dict(row)
                result_list.append(result)
            return jsonify(MedicalDevices = result_list)

    def getAllReservedMedDevicesBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            med_device_list = []
            result_list = []
            med_device_dao = MedDeviceDAO()
            med_device_list = med_device_dao.getAllReservedMedDevicesBySupplierId(supplier_id)
            for row in med_device_list:
                result = self.build_med_device_dict(row)
                result_list.append(result)
            return jsonify(MedicalDevices = result_list)

    # def getAllRequestedMedDevicesBySupplierId(self, supplier_id):
    #     supplier_dao = SupplierDAO()
    #     if not supplier_dao.getSupplierById(supplier_id):
    #         return jsonify(Error = "Supplier not found."), 404
    #     else:
    #         med_device_list = []
    #         result_list = []
    #         med_device_dao = MedDeviceDAO()
    #         med_device_list = med_device_dao.getAllRequestedMedDevicesBySupplierId(supplier_id)
    #         for row in med_device_list:
    #             result = self.build_med_device_dict(row)
    #             result_list.append(result)
    #         return jsonify(MedicalDevice = result_list)

    def searchMedDevices(self, args):
        med_device_brand = args.get("med_device_brand")
        med_device_type = args.get("med_device_type")
        med_device_condition = args.get("med_device_condition")
        dao = MedDeviceDAO()
        med_device_list = []
        if (len(args) == 1) and med_device_brand:
            med_device_list = dao.getMedDevicesByBrand(med_device_brand)
        elif (len(args) == 1) and med_device_type:
            med_device_list = dao.getMedDevicesByType(med_device_type)
        elif (len(args) == 1) and med_device_condition:
            med_device_list = dao.getMedDevicesByCondition(med_device_condition)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in med_device_list:
            result = self.build_med_device_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevices = result_list)

    def getMedDeviceAddress(self, med_device_id):
        med_device_dao = MedDeviceDAO()
        supplier_id = med_device_dao.getMedDeviceById(med_device_id)[6]
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "User not found."), 404
        else:
            row = med_device_dao.getMedDeviceAddress(supplier_id)
            if not row:
                return jsonify(Error = "Address Not Found"), 404
            else:
                address = self.build_address_dict(row)
                return jsonify(Address = address)

    def insertMedDevice(self, json):
        supplier_id = json["supplier_id"]
        category_id = json["category_id"]
        med_device_name = json["med_device_name"]
        med_device_brand = json["med_device_brand"]
        med_device_quantity = json["med_device_quantity"]
        med_device_price = json["med_device_price"]
        med_device_type = json["med_device_type"]
        med_device_model = json["med_device_model"]
        med_device_condition = json["med_device_condition"]
        med_device_power_type = json["med_device_power_type"]

        if supplier_id and category_id and med_device_name and med_device_brand and med_device_quantity and (med_device_price>=0) and med_device_type and med_device_model and med_device_condition and med_device_power_type:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, category_id, med_device_name, med_device_brand, med_device_quantity, med_device_price)
            med_device_dao = MedDeviceDAO()
            med_device_id = med_device_dao.insert(resource_id, med_device_type, med_device_model, med_device_condition, med_device_power_type)
            result = self.build_med_device_attributes(med_device_id, resource_id, supplier_id, category_id, med_device_name, med_device_brand, med_device_quantity, med_device_price, med_device_type, med_device_model, med_device_condition, med_device_power_type)
            return jsonify(MedicalDevice = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateMedDevice(self, med_device_id, json):
        med_device_dao = MedDeviceDAO()
        if not med_device_dao.getMedDeviceById(med_device_id):
            return jsonify(Error = "Medical Device not found."), 404
        else:
            supplier_id = json["supplier_id"]
            category_id = json["category_id"]
            med_device_name = json["med_device_name"]
            med_device_brand = json["med_device_brand"]
            med_device_quantity = json["med_device_quantity"]
            med_device_price = json["med_device_price"]
            med_device_type = json["med_device_type"]
            med_device_model = json["med_device_model"]
            med_device_condition = json["med_device_condition"]
            med_device_power_type = json["med_device_power_type"]
            
            if supplier_id and category_id and med_device_name and med_device_brand and med_device_quantity and med_device_price and med_device_type and med_device_model and med_device_condition and med_device_power_type:
                resource_id = med_device_dao.update(med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, category_id, med_device_name, med_device_brand, med_device_quantity, med_device_price)
                result = self.build_med_device_attributes(med_device_id, resource_id, supplier_id, category_id, med_device_name, med_device_brand, med_device_quantity, med_device_price, med_device_type, med_device_model, med_device_condition, med_device_power_type)
                return jsonify(Medical_Device = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteMedDevice(self, med_device_id):
        med_device_dao = MedDeviceDAO()
        if not med_device_dao.getMedDeviceById(med_device_id):
            return jsonify(Error = "Medical Device not found."), 404
        else:
            resource_id = med_device_dao.delete(med_device_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200