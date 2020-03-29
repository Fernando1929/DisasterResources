from flask import jsonify
from dao.resource import ResourceDAO
from dao.food import FoodDAO
from dao.user import UserDAO

class FoodHandler:
    def build_food_dict(self, row):
        result = {}
        result['food_id'] = row[0]
        result['resource_id'] = row[1]
        result['supplier_id'] = row[2]
        result['food_name'] = row[3]
        result['food_brand'] = row[4]
        result['food_quantity'] = row[5]
        result['food_price'] = row[6]
        result['food_category'] = row[7]
        result['food_container'] = row[8]
        result['food_type'] = row[9]
        result['food_ounces'] = row[10]
        result['food_expdate'] = row[11]
        return result

    def build_food_attributes(self, food_id, resource_id, supplier_id, food_name, food_brand, food_quantity, food_price, food_category, food_container, food_type, food_ounces, food_expdate):
        result = {}
        result['food_id'] = food_id
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        result['food_name'] = food_name
        result['food_brand'] = food_brand
        result['food_quantity'] = food_quantity
        result['food_price'] = food_price
        result['food_category'] = food_category
        result['food_container'] = food_container
        result['food_type'] = food_type
        result['food_ounces'] = food_ounces
        result['food_expdate'] = food_expdate
        return result

    def build_address_dict(self, row):
        result = {}
        result["address_id"] = row[0]
        result["user_id"] = row[1]
        result["addressline"] = row[2]
        result["city"] = row[3]
        result["state_province"] = row[4]
        result["country"] = row[5]
        result["zipcode"] = row[6]
        return result

    def getAllFoods(self):
        dao = FoodDAO()
        food_list = dao.getAllFoods()
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Foods = result_list)

    def getAllAvailableFoods(self):
        dao = FoodDAO()
        food_list = dao.getAllAvailableFood()
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food = result_list)

    def getAllReservedFoods(self):
        dao = FoodDAO()
        food_list = dao.getAllReservedFood()
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food = result_list)

    def getAllRequestedFoods(self):
        dao = FoodDAO()
        food_list = dao.getAllRequestedFood()
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food = result_list)

    def getFoodById(self, food_id):
        dao = FoodDAO()
        row = dao.getFoodById(food_id)
        if not row:
            return jsonify(Error = "Food Not Found"), 404
        else:
            food = self.build_food_dict(row)
            return jsonify(Food = food)

    def getFoodBySupplierId(self, supplier_id):
        food_list = []
        result_list = []
        food_dao = FoodDAO()
        food_list = food_dao.getFoodsBySupplierId(supplier_id)
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food = result_list)

    def getAllAvailableFoodBySupplierId(self, supplier_id):
        food_list = []
        result_list = []
        food_dao = FoodDAO()
        food_list = food_dao.getAllAvailableFoodBySupplierId(supplier_id)
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food = result_list)

    def getAllReservedFoodBySupplierId(self, supplier_id):
        food_list = []
        result_list = []
        food_dao = FoodDAO()
        food_list = food_dao.getAllReservedFoodBySupplierId(supplier_id)
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food = result_list)

    def getAllRequestedFoodBySupplierId(self, supplier_id):
        food_list = []
        result_list = []
        food_dao = FoodDAO()
        food_list = food_dao.getAllRequestedFoodBySupplierId(supplier_id)
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food = result_list)

    def getFoodAddress(self, food_id):
        food_dao = FoodDAO()
        supplier_id = food_dao.getFoodById(food_id)[2]
        user_dao = UserDAO()
        if not user_dao.getUserById(supplier_id):
            return jsonify(Error = "User not found."), 404
        else:
            row = food_dao.getFoodAddress(supplier_id)
            if not row:
                return jsonify(Error = "Address not found."), 404
            else:
                food_address = self.build_address_dict(row)
                return jsonify(Address = food_address)

    def searchFood(self, args):
        food_brand = args.get("food_brand")
        food_category = args.get("food_category")
        food_container = args.get("food_container")
        food_type = args.get("food_type")
        food_ounces = args.get("food_ounces")
        food_expdate = args.get("food_expdate")

        dao = FoodDAO()
        food_list = []
        if (len(args) == 1) and food_brand:
            food_list = dao.getFoodByBrand(food_brand)
        elif (len(args) == 1) and food_category:
            food_list = dao.getFoodsByCategory(food_category)
        elif (len(args) == 1) and food_container:
            food_list = dao.getFoodsByContainer(food_container)
        elif (len(args) == 1) and food_ounces:
            food_list = dao.getFoodsByOunces(food_ounces)
        elif (len(args) == 1) and food_type:
            food_list = dao.getFoodsByType(food_type)
        elif (len(args) == 2) and food_category and food_type:
            food_list = dao.getFoodsByCategoryAndType(food_category, food_type)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food = result_list)

    def insertFood(self, json):
        supplier_id = json["supplier_id"]
        food_name = json["food_name"]
        food_brand = json["food_brand"]
        food_quantity = json["food_quantity"]
        food_price = json["food_price"]
        food_category = json["food_category"]
        food_container = json["food_container"]
        food_type = json["food_type"]
        food_ounces = json["food_ounces"]
        food_expdate = json["food_expdate"]

        if supplier_id and food_name and food_brand and food_quantity and food_price and food_category and food_container and food_type and food_ounces and food_expdate:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, food_name, food_brand, food_quantity, food_price)
            food_dao = FoodDAO()
            food_id = food_dao.insert(resource_id, food_category, food_container, food_type, food_ounces, food_expdate)
            result = self.build_food_attributes(food_id, resource_id, supplier_id, food_name, food_brand, food_quantity, food_price, food_category, food_container, food_type, food_ounces, food_expdate)
            return jsonify(Food = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateFood(self, food_id, json):
        food_dao = FoodDAO()
        if not food_dao.getFoodById(food_id):
            return jsonify(Error = "Food not found."), 404
        else:
            supplier_id = json["supplier_id"]
            food_name = json["food_name"]
            food_brand = json["food_brand"]
            food_quantity = json["food_quantity"]
            food_price = json["food_price"]
            food_category = json["food_category"]
            food_container = json["food_container"]
            food_type = json["food_type"]
            food_ounces = json["food_ounces"]
            food_expdate = json["food_expdate"]

            if supplier_id and food_name and food_brand and food_quantity and food_price and food_category and food_container and food_type and food_ounces and food_expdate:
                resource_id = food_dao.update(food_id, food_category, food_container, food_type, food_ounces, food_expdate)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, food_name, food_brand, food_quantity, food_price)
             
                result = self.build_food_attributes(food_id, resource_id, supplier_id, food_name, food_brand, food_quantity, food_price, food_category, food_container, food_type, food_ounces, food_expdate)
                return jsonify(Food = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteFood(self, food_id):
        food_dao = FoodDAO()
        if not food_dao.getFoodById(food_id):
            return jsonify(Error = "Food not found."), 404
        else:
            resource_id = food_dao.delete(food_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200