from flask import jsonify
from dao.supplier import SupplierDAO
from dao.user import UserDAO


class SupplierHandler:

        #supplier = user_id, supplier_id, supplier_firstname, supplier_lastname, asupplier_date_birth, supplier_email, supplier_phone
        #resource = resource_id, resource_name, resource_description, resource_brand, resource_quantity,resource_price
    def build_supplier_attributes(self, user_id, supplier_id, supplier_firstname, supplier_lastname, supplier_date_birth, supplier_email, supplier_phone):
        result = {}
        result['user_id'] = user_id
        result['supplier_id'] = supplier_id
        result['supplier_firstname'] = supplier_firstname
        result['supplier_lastname'] = supplier_lastname
        result['supplier_date_birth'] = supplier_date_birth
        result['supplier_email'] = supplier_email
        result['supplier_phone'] = supplier_phone
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['supplier_id'] = row[1]
        result['supplier_firstname'] = row[2]
        result['supplier_lastname'] = row[3]
        result['supplier_date_birth'] = row[4]
        result['supplier_email'] = row[5]
        result['supplier_phone'] = row[6]
        return result 

    def build_resource_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['resource_id'] = row[1]
        result['resource_name'] = row[2]
        result['resource_brand'] = row[3]
        result['resource_quantity'] = row[4]
        result['resource_price'] = row[5]
        return result

    def getAllSupplier(self):
        dao = SupplierDAO()
        result = dao.getAllSupplier()
        result_list = []
        for row in result:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, supplier_id):
        dao = SupplierDAO()
        row = dao.getSupplierById(supplier_id)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier=supplier)
    
    def getAllSupplierResources(self, supplier_id):
        dao = SupplierDAO()
        result = dao.getAllSupplierResources(supplier_id)
        result_list = []
        for row in result:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getSupplierResourceById(self, supplier_id, resource_id):
        dao = SupplierDAO()
        row = dao.getSupplierResourceById(supplier_id,resource_id)
        if not row:
            return jsonify(Error = "Resoruce Not Found"), 404
        else:
            supplier = self.build_resource_dict(row)
            return jsonify(Resources=supplier)

    def searchSupplier(self, args):
        supplier_firstname = args.get("firstname")
        supplier_lastname = args.get("lastname")
        supplier_email = args.get('email')
        dao = SupplierDAO()
        supplier_list = []
        if (len(args) == 2) and supplier_firstname and supplier_lastname:
            supplier_list = dao.getSupplierByFirstnameAndLastname(supplier_firstname , supplier_lastname)
        elif (len(args) == 1) and supplier_firstname:
            supplier_list = dao.getSupplierByFirstname(supplier_firstname)
        elif (len(args) == 1) and supplier_lastname:
            supplier_list = dao.getSupplierByLastname(supplier_lastname)
        elif(len(args) == 1) and supplier_email:
            supplier_list = dao.getSupplierByEmail(supplier_email)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def insertSupplier(self, json):
        supplier_firstname = json['supplier_firstname']
        supplier_lastname = json['supplier_lastname']
        supplier_date_birth = json['supplier_date_birth']
        supplier_email = json['supplier_email']
        supplier_phone = json['supplier_phone']
        if supplier_firstname and supplier_lastname and supplier_date_birth and supplier_email and supplier_phone:
            dao_supplier = SupplierDAO()
            dao_user = UserDAO()
            user_id = dao_user.insert(supplier_firstname, supplier_lastname, supplier_date_birth,supplier_email,supplier_phone)
            supplier_id = dao_supplier.insert( supplier_firstname, supplier_lastname, supplier_date_birth, supplier_email,supplier_phone)
            result = self.build_supplier_attributes(supplier_id, user_id, supplier_firstname, supplier_lastname, supplier_date_birth, supplier_email, supplier_phone)
            return jsonify(Supplier=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteSupplier(self, supplier_id):
        dao_supplier = SupplierDAO()
        dao_user = UserDAO()
        if not dao_supplier.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            dao_supplier.delete(supplier_id)
            dao_user.delete(supplier_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateSupplier(self, supplier_id, json):
        dao_supplier = SupplierDAO()
        dao_user = UserDAO()
        if not dao_supplier.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            supplier_firstname = json['supplier_firstname']
            supplier_lastname = json['supplier_lastname']
            supplier_date_birth = json['supplier_date_birth']
            supplier_email = json['supplier_email']
            supplier_phone = json['supplier_phone']
            if supplier_firstname and supplier_lastname and supplier_date_birth and supplier_email and supplier_phone:
                user_id = dao_supplier.update(supplier_id)
                dao_user.update(user_id, supplier_firstname, supplier_lastname, supplier_date_birth, supplier_email, supplier_phone)
                result = self.build_supplier_attributes(user_id, supplier_id, supplier_firstname, supplier_lastname, supplier_date_birth, supplier_email, supplier_phone)
                return jsonify(Supplier=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400
