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
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getSupplierById(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join users where user_id = %s;"
        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        return result

    def getAllSupplierResources(self, supplier_id):
        result = [
           [1, 2, 'Battery', 'Duracel', 10, 7.00],
           [1, 3, 'ice', 'el angel', 10, 2.50],
           [1, 4, 'generator', 'CAT', 8, 500]
        ]
        return result

    def getSuppliersByFirstnameAndLastname(self,supplier_firstname, supplier_lastname):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def getSuppliersByFirstname(self,supplier_firstname):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def getSuppliersByLastname(self,supplier_lastname):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result
        
    def getSupplierByEmail(self,supplier_email):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result
    
    def getSupplierByPhone(self,supplier_phone):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result
    
    def getSuppliersByDateOfBirth(self,supplier_date_birth):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def getSuppliersByCompanyId(self, company_id):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999'],
            [2, 2, 'Miranda', 'Torres', '23/12/85', 'mtorres@gymail.com', '9999999999']
        ]
        return result

    def insert(self, user_id):
        cursor = self.conn.cursor()
        query = "insert into supplier(user_id) values (%s) returning supplier_id;"
        cursor.execute(query, (user_id,))
        supplier_id = cursor.fetchone()[0]
        self.conn.commit()
        return supplier_id

    def update(self, supplier_id):
        resource_id = 1
        return resource_id

    def delete(self, supplier_id):
        resource_id = 1
        return resource_id

    