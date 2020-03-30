from flask import jsonify
from dao.medDevice import MedDeviceDAO
from dao.resource import ResourceDAO
from dao.user import UserDAO

class MedDeviceHandler:
    def build_mdevice_dict(self, row):
        result = {}
        result['mdevice_id'] = row[0]
        result['resource_id'] = row[1]
        result['supplier_id'] = row[2]
        result['mdevice_name'] = row[3]
        result['mdevice_brand'] = row[4]
        result['mdevice_quantity'] = row[5]
        result['mdevice_price'] = row[6]
        result['mdevice_type'] = row[7]
        result['mdevice_model'] = row[8]
        result['mdevice_condition'] = row[9]
        result['mdevice_power_type'] = row[10]
        return result

    def build_mdevice_attributes(self, mdevice_id, resource_id, supplier_id, mdevice_name, mdevice_brand, mdevice_quantity, mdevice_price, mdevice_type, mdevice_model, mdevice_condition, mdevice_power_type):
        result = {}
        result['mdevice_id'] = mdevice_id
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        result['mdevice_name'] = mdevice_name
        result['mdevice_brand'] = mdevice_brand
        result['mdevice_quantity'] = mdevice_quantity
        result['mdevice_price'] = mdevice_price
        result['mdevice_type'] = mdevice_type
        result['mdevice_model'] = mdevice_model
        result['mdevice_condition'] = mdevice_condition
        result['mdevice_power_type'] = mdevice_power_type
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

    def getAllMedDevice(self):
        dao = MedDeviceDAO()
        mdevice_list = dao.getAllMedDevice()
        result_list = []
        for row in mdevice_list:
            result = self.build_mdevice_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevice = result_list)

    def getAllAvailableMedDevice(self):
        dao = MedDeviceDAO()
        mdevice_list = dao.getAllAvailableMedDevice()
        result_list = []
        for row in mdevice_list:
            result = self.build_mdevice_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevice = result_list)

    def getAllReservedMedDevice(self):
        dao = MedDeviceDAO()
        mdevice_list = dao.getAllReservedMedDevice()
        result_list = []
        for row in mdevice_list:
            result = self.build_mdevice_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevice = result_list)

    def getAllRequestedMedDevice(self):
        dao = MedDeviceDAO()
        mdevice_list = dao.getAllRequestedMedDevice()
        result_list = []
        for row in mdevice_list:
            result = self.build_mdevice_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevice = result_list)

    def getMedDeviceById(self, mdevice_id):
        dao = MedDeviceDAO()
        row = dao.getMedDeviceById(mdevice_id)
        if not row:
            return jsonify(Error = "Medical Device Not Found"), 404
        else:
            mdevice = self.build_mdevice_dict(row)
            return jsonify(MedicalDevice = mdevice)

    def getMedDeviceByResourceId(self, resource_id):
        dao = MedDeviceDAO()
        row = dao.getMedDeviceByResourceId(resource_id)
        if not row:
            return jsonify(Error = "Medical Device Not Found"), 404
        else:
            hequip = self.build_mdevice_dict(row)
            return jsonify(MedicalDevice = hequip)

    def getMedDeviceBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:
            mdevice_list = []
            result_list = []
            mdevice_dao = MedDeviceDAO()
            mdevice_list = mdevice_dao.getMedDeviceBySupplierId(supplier_id)
            for row in mdevice_list:
                result = self.build_mdevice_dict(row)
                result_list.append(result)
            return jsonify(MedicalDevice = result_list)

    def getAllAvailableMedDeviceBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:
            mdevice_list = []
            result_list = []
            mdevice_dao = MedDeviceDAO()
            mdevice_list = mdevice_dao.getAllAvailableMedDeviceBySupplierId(supplier_id)
            for row in mdevice_list:
                result = self.build_mdevice_dict(row)
                result_list.append(result)
            return jsonify(MedicalDevice = result_list)

    def getAllReservedMedDeviceBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:
            mdevice_list = []
            result_list = []
            mdevice_dao = MedDeviceDAO()
            mdevice_list = mdevice_dao.getAllReservedMedDeviceBySupplierId(supplier_id)
            for row in mdevice_list:
                result = self.build_mdevice_dict(row)
                result_list.append(result)
            return jsonify(MedicalDevice = result_list)

    def getAllRequestedMedDeviceBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO()
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error = "Supplier not found."), 404
        #else:
            mdevice_list = []
            result_list = []
            mdevice_dao = MedDeviceDAO()
            mdevice_list = mdevice_dao.getAllRequestedMedDeviceBySupplierId(supplier_id)
            for row in mdevice_list:
                result = self.build_mdevice_dict(row)
                result_list.append(result)
            return jsonify(MedicalDevice = result_list)

    def searchMedDevice(self, args):
        mdevice_brand = args.get("mdevice_brand")
        mdevice_type = args.get("mdevice_type")
        mdevice_condition = args.get("mdevice_condition")
        dao = MedDeviceDAO()
        mdevice_list = []
        if (len(args) == 1) and mdevice_brand:
            mdevice_list = dao.getMedDeviceByBrand(mdevice_brand)
        elif (len(args) == 1) and mdevice_type:
            mdevice_list = dao.getMedDeviceByType(mdevice_type)
        elif (len(args) == 1) and mdevice_condition:
            mdevice_list = dao.getMedDeviceByCondition(mdevice_condition)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in mdevice_list:
            result = self.build_mdevice_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevice = result_list)

    def getMedDeviceAddress(self, mdevice_id):
        mdevice_dao = MedDeviceDAO()
        user_id = mdevice_dao.getMedDeviceById(mdevice_id)[2]
        user_dao = UserDAO()
        if not user_dao.getUserById(user_id):
            return jsonify(Error = "User not found."), 404
        else:
            row = mdevice_dao.getMedDeviceAddress(user_id)
            if not row:
                return jsonify(Error = "Address Not Found"), 404
            else:
                address = self.build_address_dict(row)
                return jsonify(Address = address)

    def insertMedDevice(self, json):
        supplier_id = json["supplier_id"]
        mdevice_name = json["mdevice_name"]
        mdevice_brand = json["mdevice_brand"]
        mdevice_quantity = json["mdevice_quantity"]
        mdevice_price = json["mdevice_price"]
        mdevice_type = json["mdevice_type"]
        mdevice_model = json["mdevice_model"]
        mdevice_condition = json["mdevice_condition"]
        mdevice_power_type = json["mdevice_power_type"]
        if supplier_id and mdevice_name and mdevice_brand and mdevice_quantity and mdevice_price and mdevice_type and mdevice_model and mdevice_condition and mdevice_power_type:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, mdevice_name, mdevice_brand, mdevice_quantity, mdevice_price)
            mdevice_dao = MedDeviceDAO()
            mdevice_id = mdevice_dao.insert(resource_id, mdevice_type, mdevice_model, mdevice_condition, mdevice_power_type)
            result = self.build_mdevice_attributes(mdevice_id, resource_id, supplier_id, mdevice_name, mdevice_brand, mdevice_quantity, mdevice_price, mdevice_type, mdevice_model, mdevice_condition, mdevice_power_type)
            return jsonify(MedicalDevice = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateMedDevice(self, mdevice_id, json):
        mdevice_dao = MedDeviceDAO()
        if not mdevice_dao.getMedDeviceById(mdevice_id):
            return jsonify(Error = "Medical Device not found."), 404
        else:
            supplier_id = json["supplier_id"]
            mdevice_name = json["mdevice_name"]
            mdevice_brand = json["mdevice_brand"]
            mdevice_quantity = json["mdevice_quantity"]
            mdevice_price = json["mdevice_price"]
            mdevice_type = json["mdevice_type"]
            mdevice_model = json["mdevice_model"]
            mdevice_condition = json["mdevice_condition"]
            mdevice_power_type = json["mdevice_power_type"]
            if supplier_id and mdevice_name and mdevice_brand and mdevice_quantity and mdevice_price and mdevice_type and mdevice_model and mdevice_condition and mdevice_power_type:
                resource_id = mdevice_dao.update(mdevice_id, mdevice_type, mdevice_model, mdevice_condition, mdevice_power_type)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, mdevice_name, mdevice_brand, mdevice_quantity, mdevice_price)
                result = self.build_mdevice_attributes(mdevice_id, resource_id, supplier_id, mdevice_name, mdevice_brand, mdevice_quantity, mdevice_price, mdevice_type, mdevice_model, mdevice_condition, mdevice_power_type)
                return jsonify(Medical_Device = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteMedDevice(self, mdevice_id):
        mdevice_dao = MedDeviceDAO()
        if not mdevice_dao.getMedDeviceById(mdevice_id):
            return jsonify(Error = "Medical Device not found."), 404
        else:
            resource_id = mdevice_dao.delete(mdevice_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200