from config.dbconfig import pg_config
import psycopg2

class CompanyDAO:

    #company = company_id, company_name, company_address, company_phone
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    
    def getAllCompanies(self):
        cursor = self.conn.cursor()
        query = "Select * from company;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCompanyById(self, company_id):
        cursor = self.conn.cursor()
        query = "Select * from company where company_id = %s;"
        cursor.execute(query,(company_id,))
        result = cursor.fetchone()
        return result

    def getCompanyByName(self, company_name):
        cursor = self.conn.cursor()
        query = "Select * from company where company_name = %s;"
        cursor.execute(query,(company_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCompanyByAddress(self, company_address):
        cursor = self.conn.cursor()
        query = "Select * from company where company_address = %s;"
        cursor.execute(query,(company_address,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCompanyByPhone(self, company_phone): #needs test
        cursor = self.conn.cursor()
        query = "Select * from company where company_phone = %s;"
        cursor.execute(query,(company_phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCompanyBySupplierId(self, supplier_id):
        cursor = self.conn.cursor()
        query = "Select * from company Natural Inner Join represents where supplier_id = %s;"
        cursor.execute(query,(supplier_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, company_name, company_address, company_phone):
        cursor = self.conn.cursor()
        query = "insert into company(company_name, company_address, company_phone) values(%s,%s,%s) returning company_id;"
        cursor.execute(query,(company_name, company_address, company_phone))
        company_id = cursor.fetchone()[0]
        self.conn.commit()
        return company_id

    def update(self, company_id, company_name, company_address, company_phone):
        cursor = self.conn.cursor()
        query = "update company set company_name = %s, company_address = %s, company_phone = %s where company_id = %s;"
        cursor.execute(query,(company_name, company_address, company_phone,company_id))
        self.conn.commit()
        return company_id

    def delete(self, company_id):
        cursor = self.conn.cursor()
        query = "delete from company where company_id = %s;"
        cursor.execute(query,(company_id,))
        self.conn.commit()
        return company_id