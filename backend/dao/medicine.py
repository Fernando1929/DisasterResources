from config.dbconfig import pg_config
import psycopg2

class MedicineDAO:
    
    # medicine = med_id, resource_id, supplier_id, resource_category, med_name, med_brand, med_quantity, med_price,med_type, med_dose, med_prescript, med_expdate
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedicines(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableMedicines(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedMedicines(self):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource NATURAL INNER JOIN resource_reservations;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicineById(self, med_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE med_id = %s;"
        cursor.execute(query, (med_id,))
        result = cursor.fetchone()
        return result

    def getMedicineByResourceId(self, resource_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getMedicinesByBrand(self, resource_brand):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE resource_brand = %s;"
        cursor.execute(query, (resource_brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicinesByType(self, med_type):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE med_type = %s;"
        cursor.execute(query, (med_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicinesByPrescription(self, med_prescript):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE med_prescript = %s;"
        cursor.execute(query, (med_prescript,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicinesByTypeAndDose(self, med_type, med_dose):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE med_type = %s AND med_dose = %s;"
        cursor.execute(query, (med_type, med_dose,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicinesByTypeAndPrescription(self, med_type, med_prescript):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE med_type = %s AND med_prescript = %s;"
        cursor.execute(query, (med_type, med_prescript,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicinesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailableMedicinesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource WHERE supplier_id = %s AND resource_quantity > 0;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservedMedicinesBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT resource_id, med_id, med_type, med_dose, med_prescript, med_expdate, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price FROM medicine NATURAL INNER JOIN resource NATURAL INNER JOIN resource_reservations WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicineAddress(self, supplier_id):
        cursor = self.conn.cursor()
        query = "SELECT address_id, user_id, addressline, city, state_province, country, zipcode FROM address NATURAL INNER JOIN supplier WHERE supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def insert(self, resource_id, med_type, med_dose, med_prescript, med_expdate):
        cursor = self.conn.cursor()
        query = "INSERT INTO medicine (resource_id, med_type, med_dose, med_prescript, med_expdate) VALUES (%s, %s, %s, %s, %s) RETURNING med_id;"
        cursor.execute(query, (resource_id, med_type, med_dose, med_prescript, med_expdate,))
        med_id = cursor.fetchone()[0]
        self.conn.commit()
        return med_id

    def delete(self, med_id):
        cursor = self.conn.cursor()
        query = "delete from medicine where med_id = %s returning resource_id;"
        cursor.execute(query,(med_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id

    def update(self, med_id, med_type, med_dose, med_prescript, med_expdate):
        cursor = self.conn.cursor()
        query = "update medicine set med_type = %s, med_dose = %s, med_prescript = %s, med_expdate = %s where med_id = %s returning resource_id;"
        cursor.execute(query, (med_type, med_dose, med_prescript, med_expdate, med_id,))
        resource_id = cursor.fetchone()[0]
        self.conn.commit()
        return resource_id
