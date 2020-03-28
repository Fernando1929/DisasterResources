class ToolDAO:
    def __init__(self):
        super().__init__()

# tools = tool_id, resource_id, supplier_id, tool_name, tool_brand, tool_quantity, tool_price, 
#           tool_material, tool_condition, tool_ptype
    def getAllTools(self):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getAllAvailableTools(self):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getAllReservedTools(self):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getToolById(self, resource_id):
        result = [1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]
        return result

    def getToolByBrand(self, resource_brand):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getToolsByMaterial(self, tool_material):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getToolsByCondition(self, tool_condition):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getToolsByPowerType(self, tool_pwtype):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getToolsByMaterialAndPowerType(self, tool_material, tool_pwtype):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getToolsBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getAllAvailableToolsBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getAllReservedToolsBySupplierId(self, supplier_id):
        result = [[1, 1, 1, "Wrench", "Craftsman", 5, 40.00, "stainless steel", "New", "None"]]
        return result

    def getToolAddress(self, supplier_id):
        result = [1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def insert(self, resource_id, tool_material, tool_condition, tool_pwtype):
        tool_id = 1
        return tool_id

    def delete(self, tool_id):
        resource_id = 1
        return resource_id

    def update(self, tool_id, tool_material, tool_condition, tool_pwtype):
        resource_id = 1
        return resource_id