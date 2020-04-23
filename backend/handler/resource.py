from flask import jsonify
from dao.resource import ResourceDAO

from handler.fuel import FuelHandler
from handler.food import FoodHandler
from handler.medicine import MedicineHandler
from handler.tools import ToolHandler
from handler.cloth import ClothHandler
from handler.heavyequip import HeavyEquipHandler
from handler.water import WaterHandler
from handler.medDevice import MedDeviceHandler
from handler.battery import BatteryHandler
from handler.generator import GeneratorHandler
from handler.ice import IceHandler

class ResourceHandler:

    valid_categories = ['fuel', 'food', 'medicine', 'tools', 'cloth', 'heavy_equipment', 'water', 'medical_device', 'battery', 'generator', 'ice']

    def build_resource_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['supplier_id'] = row[1]
        result['resource_category'] = row[2]
        result['resource_name'] = row[3]
        result['resource_brand'] = row[4]
        result['resource_quantity'] = row[5]
        result['resource_price'] = row[6]
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
            elif category == "cloth":
                return ClothHandler().getClothByResourceId(resource_id)
            elif category == "heavy_equipment":
                return HeavyEquipHandler().getHeavyEquipByResourceId(resource_id)
            elif category == "water":
                return WaterHandler().getWaterByResourceId(resource_id)
            elif category == "medical_device":
                return MedDeviceHandler().getMedDeviceByResourceId(resource_id)
            elif category == "battery":
                return BatteryHandler().getBatteryByResourceId(resource_id)
            elif category == "generator":
                return GeneratorHandler().getGeneratorByResourceId(resource_id)
            elif category == "ice":
                return IceHandler().getIceByResourceId(resource_id)
        else:
            return jsonify(Error = "Invalid category"), 400
        