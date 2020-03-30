from flask import jsonify
from dao.resource import ResourceDAO

from handler.fuel import FuelHandler
from handler.food import FoodHandler
from handler.medicine import MedicineHandler
from handler.tools import ToolHandler

class ResourceHandler:

    valid_categories = ['fuel', 'food', 'medicine', 'tools']

    def build_resource_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['supplier_id'] = row[1]
        result['category'] = row[2]
        result['name'] = row[3]
        result['brand'] = row[4]
        result['quantity'] = row[5]
        result['price'] = row[6]
        return result

    def getAllResources(self):
        resouce_dao = ResourceDAO()
        resource_list = resouce_dao.getAllResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getResourceById(self, resource_id):
        resource_dao = ResourceDAO()
        row = resource_dao.getResourceById(resource_id)
        if not row:
            return jsonify(Error = "Resource not found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)

    def getResourceFullInfo(self, resource_id):
        resource_dao = ResourceDAO()
        category = resource_dao.getResourceById(resource_id)[2]
        if category in self.valid_categories:
            if category == "fuel":
                return FuelHandler().getFuelByResourceId(resource_id)
            elif category == "food":
                return FoodHandler().getFoodByResourceId(resource_id)
            elif category == "medicine":
                return MedicineHandler().getMedicineByResourceId(resource_id)
            elif category == "tools":
                return ToolHandler().getToolByResourceId(resource_id)

        return jsonify(Error = "Invalid category"), 400
        