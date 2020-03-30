from flask import jsonify
from dao.supplier import SupplierDAO
from dao.resource import ResourceDAO
from dao.power import PowerDAO
from dao.generator import GeneratorDAO
from dao.user import UserDAO

class GeneratorHandler:

    #generator = resource_id, resource_name, resource_description, resource_brand, resource_quantity, resource_price, power_capacity, power_condition, generator_fuel
    def build_generator_dict(self, row): 
        result = {}
        result['supplier_id'] = row[0]
        result['resource_id'] = row[1]
        result['power_id'] = row[2]
        result['generator_id'] = row[3]
        result['generator_name'] = row[4]
        result['generator_brand'] = row[5]
        result['generator_quantity'] = row[6]
        result['generator_price'] = row[7]
        result['power_capacity'] = row[8]
        result['power_condition'] = row[9]
        result['generator_fuel'] = row[10]
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

    def build_generator_attributes(self, supplier_id, resource_id, power_id, generator_id, generator_name, generator_brand, generator_quantity, generator_price, power_capacity, power_condition, generator_fuel):
        result = {}
        result['supplier_id'] = supplier_id
        result['resource_id'] = resource_id
        result['power_id'] = power_id
        result['generator_id'] = generator_id 
        result['generator_name'] = generator_name 
        result['generator_brand'] = generator_brand
        result['generator_quantity'] = generator_quantity
        result['generator_price'] = generator_price 
        result['power_capacity'] = power_capacity  
        result['power_condition'] = power_condition
        result['generator_fuel'] = generator_fuel
        return result

    def getAllGenerator(self): 
        dao = GeneratorDAO()
        result = dao.getAllGenerator()
        result_list = []
        for row in result:
            result = self.build_generator_dict(row)
            result_list.append(result)
        return jsonify(Generator=result_list)

    def getAllAvailableGenerator(self): 
        dao = GeneratorDAO()
        result = dao.getAllAvailableGenerator()
        result_list = []
        for row in result:
            result = self.build_generator_dict(row)
            result_list.append(result)
        return jsonify(Generator=result_list)

    def getAllReservedGenerator(self): 
        dao = GeneratorDAO()
        result = dao.getAllReservedGenerator()
        result_list = []
        for row in result:
            result = self.build_generator_dict(row)
            result_list.append(result)
        return jsonify(Generator=result_list)

    def getAllRequestedGenerator(self): 
        dao = GeneratorDAO()
        result = dao.getAllRequestedGenerator()
        result_list = []
        for row in result:
            result = self.build_generator_dict(row)
            result_list.append(result)
        return jsonify(Generator=result_list)

    def getGeneratorById(self, generator_id): 
        dao = GeneratorDAO()
        row = dao.getGeneratorById(generator_id)
        if not row:
            return jsonify(Error = "Generator Not Found"), 404
        else:
            genearator = self.build_generator_dict(row)
            return jsonify(Generator=genearator)

    def getGeneratorByResourceId(self, resource_id): 
        dao = GeneratorDAO()
        row = dao.getGeneratorByResourceId(resource_id)
        if not row:
            return jsonify(Error = "Generator Not Found"), 404
        else:
            genearator = self.build_generator_dict(row)
            return jsonify(Generator=genearator)

    def getGeneratorBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error="Supplier Not Found"), 404
        #else:
            generator_dao = GeneratorDAO()
            result_list = []
            generator_list = generator_dao.getGeneratorBySupplierId(supplier_id)
            for row in generator_list:
                result = self.build_generator_dict(row)
                result_list.append(result)
            return jsonify(Generator=result_list)

    def getAllAvailableGeneratorBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error="Supplier Not Found"), 404
        #else:
            generator_dao = GeneratorDAO()
            result_list = []
            generator_list = generator_dao.getAllAvailableGeneratorBySupplierId(supplier_id)
            for row in generator_list:
                result = self.build_generator_dict(row)
                result_list.append(result)
            return jsonify(Generator=result_list)

    def getAllReservedGeneratorBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error="Supplier Not Found"), 404
        #else:
            generator_dao = GeneratorDAO()
            result_list = []
            generator_list = generator_dao.getAllReservedGeneratorBySupplierId(supplier_id)
            for row in generator_list:
                result = self.build_generator_dict(row)
                result_list.append(result)
            return jsonify(Generator=result_list)

    def getAllRequestedGeneratorBySupplierId(self, supplier_id):
        #supplier_dao = SupplierDAO
        #if not supplier_dao.getSupplierById(supplier_id):
        #    return jsonify(Error="Supplier Not Found"), 404
        #else:
            generator_dao = GeneratorDAO()
            result_list = []
            generator_list = generator_dao.getAllRequestedGeneratorBySupplierId(supplier_id)
            for row in generator_list:
                result = self.build_generator_dict(row)
                result_list.append(result)
            return jsonify(Generator=result_list)

    def searchGenerator(self, args):
        generator_power_capacity = args.get('power_capacity')
        generator_power_condition = args.get('power_condition')
        generator_fuel = args.get('generator_fuel')
        dao = GeneratorDAO()
        generator_list = []
        if (len(args) == 1) and generator_power_capacity:
            generator_list = dao.getGeneratorByPowerCapacity(generator_power_capacity)
        elif (len(args) == 1) and generator_power_condition:
            generator_list = dao.getGeneratorByPowerCondition(generator_power_condition)
        elif (len(args) == 1) and generator_fuel:
            generator_list = dao.getGeneratorByFuel(generator_fuel)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in generator_list:
            result = self.build_generator_dict(row)
            result_list.append(result)
        return jsonify(Generator=result_list)

    def getGeneratorAddress(self, generator_id):
        generator_dao = GeneratorDAO()
        user_id = generator_dao.getGeneratorById(generator_id)[2]
        user_dao = UserDAO()
        if not user_dao.getUserById(user_id):
            return jsonify(Error = "User not found."), 404
        else:
            row = generator_dao.getGeneratorAddress(user_id)
            if not row:
                return jsonify(Error = "Address not found."), 404
            else:
                address = self.build_address_dic(row)
                return jsonify(Address = address)

    def insertGenerator(self, json):
        supplier_id = json['supplier_id']
        generator_name = json['generator_name'] 
        generator_brand = json['generator_brand'] 
        generator_quantity = json['generator_quantity'] 
        generator_price = json['generator_price'] 
        power_capacity = json['power_capacity'] 
        power_condition =json['power_condition'] 
        fuel =json['fuel'] 
        if generator_name and generator_brand and generator_quantity and generator_price and power_capacity and power_condition and fuel:
            res_dao = ResourceDAO()
            resource_id = res_dao.insert(supplier_id, generator_name, generator_brand, generator_quantity, generator_price)
            power_dao = PowerDAO()
            power_id = power_dao.insert(resource_id, power_capacity,  power_condition)
            generator_dao = GeneratorDAO()
            generator_id = generator_dao.insert(resource_id, power_id, fuel)
            result = self.build_generator_attributes(supplier_id, resource_id, power_id, generator_id, generator_name, generator_brand, generator_quantity, generator_price, power_capacity, power_condition, fuel)
            return jsonify(Generator=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteGenerator(self, generator_id):
        generator_dao = GeneratorDAO()
        if not generator_dao.getGeneratorById(generator_id):
            return jsonify(Error = "Generator not found."), 404
        else:
            power_id = generator_dao.delete(generator_id)
            power_dao = PowerDAO()
            resource_id = power_dao.delete(power_id)
            res_dao = ResourceDAO()
            res_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateGenerator(self, generator_id, json):
        generator_dao = GeneratorDAO()
        if not generator_dao.getGeneratorById(generator_id):
            return jsonify(Error = "Generator not found."), 404
        else:
            supplier_id = json['supplier_id']
            generator_name = json['generator_name'] 
            generator_brand = json['generator_brand']
            generator_quantity = json['generator_quantity']
            generator_price = json['generator_price']
            power_capacity = json['power_capacity']
            power_condition = json['power_condition']
            fuel = json['fuel']
            if generator_name  and generator_brand and generator_quantity and generator_price and power_capacity and power_condition and fuel:
                res_dao = ResourceDAO()
                resource_id = res_dao.insert(supplier_id, generator_name, generator_brand, generator_quantity, generator_price)
                power_dao = PowerDAO()
                power_id = power_dao.insert(resource_id, power_capacity,  power_condition)
                generator_id = generator_dao.insert(resource_id, power_id, fuel)
                result = self.build_generator_attributes(supplier_id, resource_id, power_id, generator_id, generator_name, generator_brand, generator_quantity, generator_price, power_capacity, power_condition, fuel)
                return jsonify(Generator=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400