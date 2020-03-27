from flask import jsonify
from dao.resource import ResourceDAO
from dao.tools import ToolDAO

class ToolHandler:
    def build_tool_dict(self, row):
        result = {}
        result['tool_id'] = row[0]
        result['resource_id'] = row[1]
        result['supplier_id'] = row[2]
        result['tool_address'] = row[3]
        result['tool_name'] = row[4]
        result['tool_brand'] = row[5]
        result['tool_quantity'] = row[6]
        result['tool_price'] = row[7]
        result['tool_material'] = row[8]
        result['tool_condition'] = row[9]
        result['tool_pwtype'] = row[10]
        return result

    def build_tool_attributes(self, tool_id, resource_id, supplier_id, tool_address, tool_name, tool_brand, tool_quantity, tool_price, tool_material, tool_condition, tool_pwtype):
        result = {}
        result['tool_id'] = tool_id
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        result['tool_address'] = tool_address
        result['tool_name'] = tool_name
        result['tool_brand'] = tool_brand
        result['tool_quantity'] = tool_quantity
        result['tool_price'] = tool_price
        result['tool_material'] = tool_material
        result['tool_condition'] = tool_condition
        result['tool_pwtype'] = tool_pwtype
        return result

    def getAllTools(self):
        dao = ToolDAO()
        tool_list = dao.getAllTools()
        result_list = []
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools = result_list)

    def getAllAvailableTools(self):
        dao = ToolDAO()
        tool_list = dao.getAllAvailableTools()
        result_list = []
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools = result_list)

    def getAllReservedTools(self):
        dao = ToolDAO()
        tool_list = dao.getAllReservedTools()
        result_list = []
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools = result_list)

    def getToolById(self, tool_id):
        dao = ToolDAO()
        row = dao.getToolById(tool_id)
        if not row:
            return jsonify(Error = "Tool Not Found"), 404
        else:
            tool = self.build_tool_dict(row)
            return jsonify(Tool = tool)

    def getToolsBySupplierId(self, supplier_id):
        tool_list = []
        result_list = []
        tool_dao = ToolDAO()
        tool_list = tool_dao.getToolsBySupplierId(supplier_id)
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools = result_list)

    def getAllAvailableToolsBySupplierId(self, supplier_id):
        tool_list = []
        result_list = []
        tool_dao = ToolDAO()
        tool_list = tool_dao.getAllAvailableToolsBySupplierId(supplier_id)
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools = result_list)

    def getAllReservedToolsBySupplierId(self, supplier_id):
        tool_list = []
        result_list = []
        tool_dao = ToolDAO()
        tool_list = tool_dao.getAllReservedToolsBySupplierId(supplier_id)
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools = result_list)

    def searchTools(self, args):
        tool_brand = args.get("tool_brand")
        tool_material = args.get("tool_material")
        tool_condition = args.get("tool_condition")
        tool_pwtype = args.get("tool_pwtype")

        dao = ToolDAO()
        tool_list = []
        if (len(args) == 1) and tool_brand:
            tool_list = dao.getToolByBrand(tool_brand)
        elif (len(args) == 1) and tool_material:
            tool_list = dao.getToolsByMaterial(tool_material)
        elif (len(args) == 1) and tool_condition:
            tool_list = dao.getToolsByCondition(tool_condition)
        elif (len(args) == 1) and tool_pwtype:
            tool_list = dao.getToolsByPowerType(tool_pwtype)
        elif (len(args) == 2) and tool_material and tool_pwtype:
            fuel_list = dao.getToolsByMaterialAndPowerType(tool_material, tool_pwtype)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools = result_list)

    def insertTool(self, json):
        supplier_id = json["supplier_id"]
        tool_address = json["tool_address"]
        tool_name = json["tool_name"]
        tool_brand = json["tool_brand"]
        tool_quantity = json["tool_quantity"]
        tool_price = json["tool_price"]
        tool_material = json["tool_material"]
        tool_condition = json["tool_condition"]
        tool_pwtype = json["tool_pwtype"]

        if supplier_id and tool_address and tool_name and tool_brand and tool_quantity and tool_price and tool_material and tool_condition and tool_pwtype:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, tool_address, tool_name, tool_brand, tool_quantity, tool_price)
            tool_dao = ToolDAO()
            tool_id = tool_dao.insert(resource_id, tool_material, tool_condition, tool_pwtype)
            result = self.build_tool_attributes(tool_id, resource_id, supplier_id, tool_addres, tool_name, tool_brand, tool_quantity, tool_price, tool_material, tool_condition, tool_pwtype)
            return jsonify(Tool = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateTool(self, tool_id, json):
        tool_dao = ToolDAO()
        if not tool_dao.getToolById(tool_id):
            return jsonify(Error = "Tool not found."), 404
        else:
            supplier_id = json["supplier_id"]
            tool_address = json["tool_address"]
            tool_name = json["tool_name"]
            tool_brand = json["tool_brand"]
            tool_quantity = json["tool_quantity"]
            tool_price = json["tool_price"]
            tool_material = json["tool_material"]
            tool_condition = json["tool_condition"]
            tool_pwtype = json["tool_pwtype"]

            if supplier_id and tool_address and tool_name and tool_brand and tool_quantity and tool_price and tool_material and tool_condition and tool_pwtype:
                resource_id = tool_dao.update(tool_id, tool_material, tool_condition, tool_pwtype)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, tool_address, tool_name, tool_brand, tool_quantity, tool_price)
                result = self.build_tool_attributes(tool_id, resource_id, supplier_id, tool_address, tool_name, tool_brand, tool_quantity, tool_price, tool_material, tool_condition, tool_pwtype)
                return jsonify(Tool = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteTool(self, tool_id):
        tool_dao = ToolDAO()
        if not tool_dao.getToolById(tool_id):
            return jsonify(Error = "Tool not found."), 404
        else:
            resource_id = tool_dao.delete(tool_id)
            resource_dao = ResourceDAO()
            resource_dao.delete(resource_id)
            return jsonify(DeleteStatus = "OK"), 200