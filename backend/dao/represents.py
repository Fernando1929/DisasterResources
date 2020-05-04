from config.dbconfig import pg_config
import psycopg2

class RepresentsDAO:

    # company_id, supplier_id
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self, company_id, supplier_id):
        cursor = self.conn.cursor()
        query = "insert into represents(company_id, supplier_id) values (%s, %s);"
        cursor.execute(query, (company_id, supplier_id))
        self.conn.commit()
        return None #Maybe return the tuple

    def update(self, company_id, supplier_id): #Verify implementation Maybe Not necesary (Verify later)
        cursor = self.conn.cursor()
        query = "update represents set company_id = %s where supplier_id = %s;"
        cursor.execute(query, (company_id, supplier_id))
        self.conn.commit()
        return None #Maybe return tuple 

    def delete(self, company_id, supplier_id): #Verify implementation
        cursor = self.conn.cursor()
        query = "delete from represent where company_id = %s and supplier_id = %s;"
        cursor.execute(query, (company_id, supplier_id))
        self.conn.commit()
        return None #Maybe return the tuple