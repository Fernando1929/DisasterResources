from config.dbconfig import pg_config
import psycopg2
class MedDeviceDAO:

    # med_device = mdevice_id, resource_id, supplier_id, category, mdevice_name, mdevice_brand, mdevice_quantity, mdevice_price, mdevice_type, mdevice_model, mdevice_condition, mdevice_power
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedDevices(self):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableMedDevices(self):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource where resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedMedDevices(self):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource natural inner join resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedDeviceById(self, med_device_id):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource where med_device_id = %s;"
        cursor.execute(query, (med_device_id,))
        result = cursor.fetchone()
        return result

    def getMedDeviceByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getMedDevicesByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource where resource_brand = %s;"
        cursor.execute(query, (resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedDevicesByCondition(self, med_device_condition):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource where med_device_condition = %s;"
        cursor.execute(query, (med_device_condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedDevicesByType(self, med_device_type):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource where med_device_type = %s;"
        cursor.execute(query, (med_device_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedDevicesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableMedDevicesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource where supplier_id = %s and resource_quantity > 0;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedMedDevicesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select resource_id, med_device_id, med_device_type, med_device_model, med_device_condition, med_device_power_type, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price from medical_device natural inner join resource natural inner join resource_reservations where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedDeviceAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select address_id, user_id, addressline, city, state_province, country, zipcode from address natural inner join supplier where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self, resource_id, med_device_type, med_device_model, med_device_condition, med_device_power_type):
        cursor = self.conn.cursor()
        query = "insert into medical_device(resource_id, med_device_type, med_device_model, med_device_condition, med_device_power_type) values (%s, %s, %s, %s, %s) returning med_device_id;"
        cursor.execute(query, (resource_id, med_device_type, med_device_model, med_device_condition, med_device_power_type))
        med_device_id = cursor.fetchone()[0]
        self.conn.commit()
        return med_device_id

    def update(self, mdevice_id, med_device_type, med_device_model, med_device_condition, med_device_power_type):
        cursor = self.conn.cursor()
        query = "update medical_device set med_device_type = %s, med_device_model = %s, med_device_condition = %s, med_device_power_type = %s where med_device_id = %s returning resource_id;"
        cursor.execute(query, (med_device_type, med_device_model, med_device_condition, med_device_power_type, mdevice_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def delete(self, mdevice_id):
        cursor = self.conn.cursor()
        query = "delete from medical_device where med_device_id = %s returning resource_id;"
        cursor.execute(query,(mdevice_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id