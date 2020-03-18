from config.dbconfig import pg_config
import psycopg2

class AdminDAO:

    def __init__(self):
        super().__init__()
        
    #admin = user_id, admin_id, admin_firstname, admin_lastname, admin_date_birth, admin_email, admin_phone
    def getAllAdmin(self):
        result = [
            ['1', '1', 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999'],
            ['2', '2', 'Miranda', 'Torres', '23/12/85', 'mtorres@gymail.com', '9999999999']
        ]
        return result
    
    def getAdminById(self,admin_id):
        result = ['2', '2', 'Miranda', 'Torres', '23/12/85', 'mtorres@gymail.com', '9999999999']
        return result

    def getAdminByFirstname(self,admin_firstname):
        result = [
            ['1', '1', 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def getAdminByLastname(self,admin_lastname):
        result = [
            ['1', '1', 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def getAdminByEmail(self,admin_email):
        result = [
            ['1', '1', 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def getAdminByFirstnameAndLastname(self,admin_firstname, admin_lastname):
        result = [
            ['1', '1', 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def insert(self, user_id):
        admin_id = 1
        return admin_id

    def update(self, admin_id):
        admin_id = 1
        return admin_id
    
    def delete(self, admin_id):
        admin_id = 1
        return admin_id