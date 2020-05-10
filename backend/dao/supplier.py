from config.dbconfig import pg_config
import psycopg2
class SupplierDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
        
    #supplier = user_id, supplier_id, supplier_firstname, supplier_lastname, supplier_date_birth, supplier_email, supplier_phone

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users natural inner join user_phone;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getSupplierById(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users natural inner join user_phone where user_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def getAllSupplierResources(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from resource where supplier_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByFirstnameAndLastname(self,supplier_firstname, supplier_lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users natural inner join user_phone where user_firstname = %s and user_lastname = %s;"
        cursor.execute(query, (supplier_firstname, supplier_lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByFirstname(self,supplier_firstname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users natural inner join user_phone where user_firstname = %s;"
        cursor.execute(query, (supplier_firstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByLastname(self,supplier_lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users natural inner join user_phone where user_lastname = %s;"
        cursor.execute(query, (supplier_lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        
    def getSupplierByEmail(self,supplier_email):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users natural inner join user_phone where user_email = %s;"
        cursor.execute(query, (supplier_email,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getSupplierByPhone(self,supplier_phone):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users natural inner join user_phone where user_phone = %s;"
        cursor.execute(query, (supplier_phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getSuppliersByDateOfBirth(self,supplier_date_birth):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users natural inner join user_phone where user_date_birth = %s;"
        cursor.execute(query, (supplier_date_birth,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByCompanyId(self, company_id):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users natural inner join user_phone natural inner join represents WHERE company_id = %s;"
        cursor.execute(query, (company_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, user_id):
        cursor = self.conn.cursor()
        query = "insert into supplier(user_id) values (%s) returning supplier_id;"
        cursor.execute(query, (user_id,))
        supplier_id = cursor.fetchone()[0]
        self.conn.commit()
        return supplier_id

    def update(self, supplier_id):
        return supplier_id

    def delete(self, supplier_id):
        return supplier_id