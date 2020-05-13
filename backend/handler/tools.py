from flask import jsonify
from dao.resource import ResourceDAO
from dao.tools import ToolDAO
from dao.user import UserDAO
from dao.supplier import SupplierDAO

class ToolHandler:
    def build_tool_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['tool_id'] = row[1]
        result['tool_material'] = row[2]
        result['tool_condition'] = row[3]
        result['tool_pwtype'] = row[4]
        result['supplier_id'] = row[5]
        result['category_id'] = row[6]
        result['tool_name'] = row[7]
        result['tool_brand'] = row[8]
        result['tool_quantity'] = row[9]
        result['tool_price'] = row[10]
        return result

    def build_tool_attributes(self, tool_id, resource_id, supplier_id, category_id, tool_name, tool_brand, tool_quantity, tool_price, tool_material, tool_condition, tool_pwtype):
        result = {}
        result['tool_id'] = tool_id
        result['resource_id'] = resource_id
        result['supplier_id'] = supplier_id
        result['category_id'] = category_id
        result['tool_name'] = tool_name
        result['tool_brand'] = tool_brand
        result['tool_quantity'] = tool_quantity
        result['tool_price'] = tool_price
        result['tool_material'] = tool_material
        result['tool_condition'] = tool_condition
        result['tool_pwtype'] = tool_pwtype
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

    # def getAllRequestedTools(self):
    #     dao = ToolDAO()
    #     tool_list = dao.getAllRequestedTools()
    #     result_list = []
    #     for row in tool_list:
    #         result = self.build_tool_dict(row)
    #         result_list.append(result)
    #     return jsonify(Tools = result_list)

    def getToolById(self, tool_id):
        dao = ToolDAO()
        row = dao.getToolById(tool_id)
        if not row:
            return jsonify(Error = "Tool Not Found"), 404
        else:
            tool = self.build_tool_dict(row)
            return jsonify(Tool = tool)

    def getToolByResourceId(self, resource_id):
        dao = ToolDAO()
        row = dao.getToolByResourceId(resource_id)
        if not row:
            return jsonify(Error = "Tool Not Found"), 404
        else:
            tool = self.build_tool_dict(row)
            return jsonify(Tool = tool)

    def getToolsBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            tool_list = []
            result_list = []
            tool_dao = ToolDAO()
            tool_list = tool_dao.getToolsBySupplierId(supplier_id)
            for row in tool_list:
                result = self.build_tool_dict(row)
                result_list.append(result)
            return jsonify(Tools = result_list)

    def getAllAvailableToolsBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            tool_list = []
            result_list = []
            tool_dao = ToolDAO()
            tool_list = tool_dao.getAllAvailableToolsBySupplierId(supplier_id)
            for row in tool_list:
                result = self.build_tool_dict(row)
                result_list.append(result)
            return jsonify(Tools = result_list)

    def getAllReservedToolsBySupplierId(self, supplier_id):
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "Supplier not found."), 404
        else:
            tool_list = []
            result_list = []
            tool_dao = ToolDAO()
            tool_list = tool_dao.getAllReservedToolsBySupplierId(supplier_id)
            for row in tool_list:
                result = self.build_tool_dict(row)
                result_list.append(result)
            return jsonify(Tools = result_list)

    # def getAllRequestedToolsBySupplierId(self, supplier_id):
    #     supplier_dao = SupplierDAO()
    #     if not supplier_dao.getSupplierById(supplier_id):
    #         return jsonify(Error = "Supplier not found."), 404
    #     else:
    #         tool_list = []
    #         result_list = []
    #         tool_dao = ToolDAO()
    #         tool_list = tool_dao.getAllRequestedToolsBySupplierId(supplier_id)
    #         for row in tool_list:
    #             result = self.build_tool_dict(row)
    #             result_list.append(result)
    #         return jsonify(Tools = result_list)

    def getToolAddress(self, tool_id):
        tool_dao = ToolDAO()
        supplier_id = tool_dao.getToolById(tool_id)[5]
        supplier_dao = SupplierDAO()
        if not supplier_dao.getSupplierById(supplier_id):
            return jsonify(Error = "User not found."), 404
        else:
            row = tool_dao.getToolAddress(supplier_id)
            if not row:
                return jsonify(Error = "Address not found."), 404
            else:
                tool_address = self.build_address_dict(row)
                return jsonify(Address = tool_address)

    def searchTools(self, args):
        tool_brand = args.get("tool_brand")
        tool_material = args.get("tool_material")
        tool_condition = args.get("tool_condition")
        tool_pwtype = args.get("tool_pwtype")

        dao = ToolDAO()
        tool_list = []
        if (len(args) == 1) and tool_brand:
            tool_list = dao.getToolsByBrand(tool_brand)
        elif (len(args) == 1) and tool_material:
            tool_list = dao.getToolsByMaterial(tool_material)
        elif (len(args) == 1) and tool_condition:
            tool_list = dao.getToolsByCondition(tool_condition)
        elif (len(args) == 1) and tool_pwtype:
            tool_list = dao.getToolsByPowerType(tool_pwtype)
        elif (len(args) == 2) and tool_material and tool_pwtype:
            tool_list = dao.getToolsByMaterialAndPowerType(tool_material, tool_pwtype)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in tool_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tools = result_list)

    def insertTool(self, json):
        supplier_id = json["supplier_id"]
        category_id = json['category_id']
        tool_name = json["tool_name"]
        tool_brand = json["tool_brand"]
        tool_quantity = json["tool_quantity"]
        tool_price = json["tool_price"]
        tool_material = json["tool_material"]
        tool_condition = json["tool_condition"]
        tool_pwtype = json["tool_pwtype"]

        if supplier_id and category_id and tool_name and tool_brand and tool_quantity and (tool_price>=0) and tool_material and tool_condition and tool_pwtype:
            resource_dao = ResourceDAO()
            resource_id = resource_dao.insert(supplier_id, category_id, tool_name, tool_brand, tool_quantity, tool_price)
            tool_dao = ToolDAO()
            tool_id = tool_dao.insert(resource_id, tool_material, tool_condition, tool_pwtype)
            result = self.build_tool_attributes(tool_id, resource_id, supplier_id, category_id, tool_name, tool_brand, tool_quantity, tool_price, tool_material, tool_condition, tool_pwtype)
            return jsonify(Tool = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateTool(self, tool_id, json):
        tool_dao = ToolDAO()
        if not tool_dao.getToolById(tool_id):
            return jsonify(Error = "Tool not found."), 404
        else:
            supplier_id = json["supplier_id"]
            category_id = json['category_id']
            tool_name = json["tool_name"]
            tool_brand = json["tool_brand"]
            tool_quantity = json["tool_quantity"]
            tool_price = json["tool_price"]
            tool_material = json["tool_material"]
            tool_condition = json["tool_condition"]
            tool_pwtype = json["tool_pwtype"]

            if supplier_id and category_id and tool_name and tool_brand and tool_quantity and (tool_price>=0) and tool_material and tool_condition and tool_pwtype:
                resource_id = tool_dao.update(tool_id, tool_material, tool_condition, tool_pwtype)
                resource_dao = ResourceDAO()
                resource_dao.update(resource_id, supplier_id, category_id, tool_name, tool_brand, tool_quantity, tool_price)
                result = self.build_tool_attributes(tool_id, resource_id, supplier_id, category_id, tool_name, tool_brand, tool_quantity, tool_price, tool_material, tool_condition, tool_pwtype)
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