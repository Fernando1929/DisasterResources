from flask import jsonify
from dao.ice import IceDAO
from dao.supplier import SupplierDAO
from dao.resource import ResourceDAO
from dao.user import UserDAO
from dao.supplier import SupplierDAO

class IceHandler:

    def build_ice_dict(self, row): 
        result = {} 
        result['resource_id'] = row[0]
        result['supplier_id'] = row[1]
        result['category_id'] = row[2]
        result['ice_name'] = row[3]
        result['ice_brand'] = row[4]
        result['ice_quantity'] = row[5]
        result['ice_price'] = row[6]
        result['ice_id'] = row[7]
        result['ice_weight'] = row[8]
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

    def build_ice_attributes(self, ice_id, supplier_id, resource_id, category_id, ice_name, ice_brand, ice_quantity, ice_price, ice_weight):
        result = {}  
        result['ice_id'] = ice_id
        result['supplier_id'] = supplier_id
        result['resource_id'] = resource_id
        result['category_id'] = category_id 
        result['ice_name'] = ice_name
        result['ice_brand'] = ice_brand
        result['ice_quantity'] = ice_quantity
        result['ice_price'] = ice_price
        result['ice_weight'] = ice_weight
        return result

    def getAllIce(self):
        dao = IceDAO()
        result = dao.getAllIce()
        result_list = []
        for row in result:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return jsonify(Ice = result_list)
    
    def getAllAvailableIce(self):
        dao = IceDAO()
        result = dao.getAllAvailableIce()
        result_list = []
        for row in result:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return jsonify(Ice = result_list)
    
    def getAllReservedIce(self):
        dao = IceDAO()
        result = dao.getAllReservedIce()
        result_list = []
        for row in result:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return jsonify(Ice = result_list)

    # def getAllRequestedIce(self):
    #     dao = IceDAO()
    #     result = dao.getAllRequestedIce()
    #     result_list = []
    #     for row in result:
    #         result = self.build_ice_dict(row)
    #         result_list.append(result)
    #     return jsonify(Ice = result_list)
    
    def getIceById(self, ice_id):
        dao = IceDAO()
        row = dao.getIceById(ice_id)
        if not row:
            return jsonify(Error = "Ice Not Found"), 404
        else:
            ice = self.build_ice_dict(row)
            return jsonify(Ice = ice)

    def getIceByResourceId(self, resource_id):
        dao = IceDAO()
        row = dao.getIceByResourceId(resource_id)
        if not row:
            return jsonify(Error = "Ice Not Found"), 404
        else:
            ice = self.build_ice_dict(row)
            return jsonify(Ice = ice)

    def getIceBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            ice_dao = IceDAO()
            result_list = []
            ice_list = ice_dao.getIceBySupplierId(supplier_id)
            for row in ice_list:
                result = self.build_ice_dict(row)
                result_list.append(result)
            return jsonify(Ice = result_list)

    def getAllAvailableIceBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            ice_dao = IceDAO()
            result_list = []
            ice_list = ice_dao.getAllAvailableIceBySypplierId(supplier_id)
            for row in ice_list:
                result = self.build_ice_dict(row)
                result_list.append(result)
            return jsonify(Ice = result_list)

    def getAllReservedIceBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            ice_dao = IceDAO()
            result_list = []
            ice_list = ice_dao.getAllReservedIceBySypplierId(supplier_id)
            for row in ice_list:
                result = self.build_ice_dict(row)
                result_list.append(result)
            return jsonify(Ice = result_list)

    # def getAllRequestedIceBySupplierId(self, supplier_id):
    #     supplier_dao = SupplierDAO()
    #     if not supplier_dao.getSupplierById(supplier_id):
    #         return jsonify(Error = "Supplier Not Found"), 404
    #     else:
    #         ice_dao = IceDAO()
    #         result_list = []
    #         ice_list = ice_dao.getAllRequestedIceBySypplierId(supplier_id)
    #         for row in ice_list:
    #             result = self.build_ice_dict(row)
    #             result_list.append(result)
    #         return jsonify(Ice = result_list)
    
    def searchIce(self, args):
        brand =  args.get('ice_brand')
        weight = args.get('ice_weight')
        dao = IceDAO()
        ice_list = []
        if (len(args) == 1) and brand:
            ice_list = dao.getIceByBrand(brand)
        elif (len(args) == 1) and weight:
            ice_list = dao.getIceByWeight(weight)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in ice_list:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return jsonify(Ice = result_list)


    def getIceAddress(self,ice_id):
        ice_dao = IceDAO()
        try:
            supplier_id = ice_dao.getIceById(ice_id)[1]
        except Exception:
            return jsonify(Error = "Ice not found."), 404
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            row = ice_dao.getIceAddress(supplier_id)
            if not row:
                return jsonify(Error = "Address not found."), 404
            else:
                address = self.build_address_dic(row)
                return jsonify(Address = address)


    def insertIce(self, json):
        supplier_id = json['supplier_id']
        category_id = json['category_id']
        ice_name = json['ice_name']
        ice_brand = json['ice_brand']
        ice_quantity = json['ice_quantity'] 
        ice_price = json['ice_price']
        ice_weight = json['ice_weight']

        if supplier_id and category_id and ice_name and ice_brand and ice_quantity and ice_price and ice_weight:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, category_id, ice_name, ice_brand, ice_quantity, ice_price)
            ice_dao = IceDAO()
            ice_id = ice_dao.insert(resource_id, ice_weight)
            result = self.build_ice_attributes(ice_id, resource_id, category_id, ice_name, ice_brand, ice_quantity, ice_price, ice_weight)
            return jsonify(Ice = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteIce(self, ice_id):
        ice_dao = IceDAO()
        res_dao = ResourceDAO()
        if not ice_dao.getIceById(ice_id):
            return jsonify(Error = "Ice not found."), 404
        else:
            resource_id = ice_dao.delete(ice_id)
            res_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateIce(self, ice_id, json):
        ice_dao = IceDAO()
        if not ice_dao.getIceById(ice_id):
            return jsonify(Error = "Ice not found."), 404
        else:
            supplier_id = json['supplier_id']
            category_id = json['category_id']
            ice_name = json['ice_name']
            ice_brand = json['ice_brand']
            ice_quantity = json['ice_quantity'] 
            ice_price = json['ice_price']
            ice_weight = json['ice_weight']

            if supplier_id and category_id and ice_name and ice_brand and ice_quantity and ice_price and ice_weight:
                resource_id = ice_dao.update(ice_id, ice_weight)
                res_dao = ResourceDAO()
                res_dao.update(resource_id, supplier_id, category_id, ice_name, ice_brand, ice_quantity, ice_price)
                result = self.build_ice_attributes(ice_id, supplier_id, resource_id, category_id, ice_name, ice_brand, ice_quantity, ice_price , ice_weight)
                return jsonify(Ice = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

