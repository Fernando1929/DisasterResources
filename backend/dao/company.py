from config.dbconfig import pg_config
import psycopg2

class CompanyDAO:
    
    def __init__(self):
        super().__init__()
    
    #company = company_id, company_name, company_address, company_phone
    def getAllCompanies(self):
        result = [
            ['1', 'Baxter', 'Jayuya','7879999999'], 
            ['2', "Pepe's Company", 'San Juan','7879998999'], 
        ]
        return result

    def getCompanyById(self, company_id):
        result =  ['1', 'Baxter', 'Jayuya','7879999999']
        return result

    def getCompanyByName(self, company_name):
        result = [
            ['1', 'Baxter', 'Jayuya','7879999999'], 
            ['2', "Pepe's Company", 'San Juan','7879998999']
        ]
        return result

    def getCompanyByAddress(self, company_address):
        result = [
           ['1', 'Baxter', 'Jayuya','7879999999']
        ]
        return result

    def getCompanyByPhone(self, company_phone):
        result = [
            ['1', 'Baxter', 'Jayuya','7879999999']
        ]
        return result

    def insert(self, company_name, company_address, company_phone):
        resource_id =1
        return resource_id

    def update(self, company_id, company_name, company_address, company_phone):
        resource_id =1
        return resource_id

    def delete(self, company_id):
        resource_id =1
        return resource_id