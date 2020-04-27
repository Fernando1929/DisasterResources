from config.dbconfig import pg_config
import psycopg2

class ToolDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # tools = tool_id, resource_id, supplier_id, resource_category, tool_name, tool_brand, tool_quantity, tool_price, 
    #           tool_material, tool_condition, tool_pwtype

    def getAllTools(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableTools(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedTools(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource NATURAL INNER JOIN resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedTools(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource NATURAL INNER JOIN resource_requests;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolById(self, tool_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE tool_id = %s;"
        cursor.execute(query, (tool_id,))
        result = cursor.fetchone()
        return result

    def getToolByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getToolsByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE resource_brand = %s;"
        cursor.execute(query, (resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolsByMaterial(self, tool_material):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE tool_material = %s;"
        cursor.execute(query, (tool_material,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolsByCondition(self, tool_condition):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE tool_condition = %s;"
        cursor.execute(query, (tool_condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolsByPowerType(self, tool_pwtype):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE tool_pwtype = %s;"
        cursor.execute(query, (tool_pwtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolsByMaterialAndPowerType(self, tool_material, tool_pwtype):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE tool_material = %s AND tool_pwtype = %s;"
        cursor.execute(query, (tool_material, tool_pwtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableToolsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource WHERE supplier_id = %s AND resource_quantity > 0;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedToolsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource NATURAL INNER JOIN resource_reservations WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRequestedToolsBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM tools NATURAL INNER JOIN resource NATURAL INNER JOIN resource_requests WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getToolAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT * FROM address NATURAL INNER JOIN supplier WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self, resource_id, tool_material, tool_condition, tool_pwtype):
        cursor = self.conn.cursor()
        query = "INSERT INTO tools (resource_id, tool_material, tool_condition, tool_pwtype) VALUES (%s, %s, %s, %s) RETURNING tool_id;"
        cursor.execute(query, (resource_id, tool_material, tool_condition, tool_pwtype,))
        tool_id = cursor.fetchone()[0]
        self.conn.commit()
        return tool_id

    def delete(self, tool_id):
        return tool_id

    def update(self, tool_id, tool_material, tool_condition, tool_pwtype):
        return tool_id