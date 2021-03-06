from config.dbconfig import pg_config
import psycopg2

class HeavyEquipDAO:

    # heavy_equipment = hequip_id, resource_id, supplier_id, category, hequip_name, hequip_brand, hequip_quantity, hequip_price, hequip_type, hequip_model, hequip_condition
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHeavyEquip(self):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableHeavyEquip(self):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource where resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedHeavyEquip(self):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource natural inner join resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipById(self, heavyequip_id):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource where heavyequip_id = %s;"
        cursor.execute(query, (heavyequip_id,))
        result = cursor.fetchone()
        return result

    def getHeavyEquipByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getHeavyEquipByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource where resource_brand = %s;"
        cursor.execute(query, (resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipByCondition(self, heavyequip_condition):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource where heavyequip_condition = %s;"
        cursor.execute(query, (heavyequip_condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipByType(self, heavyequip_type):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource where heavyequip_type = %s;"
        cursor.execute(query, (heavyequip_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableHeavyEquipBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource where supplier_id = %s and resource_quantity > 0;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedHeavyEquipBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, heavyequip_id, heavyequip_type, heavyequip_model, heavyequip_condition, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from heavy_equipment natural inner join resource natural inner join resource_reservations where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquipAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select address_id, user_id, addressline, city, state_province, country, zipcode from address natural inner join supplier where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self, resource_id, heavyequip_type, heavyequip_model, heavyequip_condition):
        cursor = self.conn.cursor()
        query = "insert into heavy_equipment(resource_id, heavyequip_type, heavyequip_model, heavyequip_condition) values (%s, %s, %s, %s) returning heavyequip_id;"
        cursor.execute(query, (resource_id, heavyequip_type, heavyequip_model, heavyequip_condition))
        heavyequip_id = cursor.fetchone()[0]
        self.conn.commit()
        return heavyequip_id

    def update(self, hequip_id, heavyequip_type, heavyequip_model, heavyequip_condition):
        cursor = self.conn.cursor()
        query = "update heavy_equipment set heavyequip_type = %s, heavyequip_model = %s, heavyequip_condition = %s where heavyequip_id = %s returning resource_id;"
        cursor.execute(query, (heavyequip_type, heavyequip_model, heavyequip_condition, hequip_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def delete(self, equip_id):
        cursor = self.conn.cursor()
        query = "delete from heavy_equipment where heavyequip_id = %s returning resource_id;"
        cursor.execute(query,(equip_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id