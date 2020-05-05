from config.dbconfig import pg_config
import psycopg2

class AdminDAO:
    
    #admin = user_id, admin_id, admin_firstname, admin_lastname, admin_date_birth, admin_email, admin_phone
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s"% (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
        
    def getAllAdmins(self):
        cursor = self.conn.cursor()
        query = "Select * from admin Natural Inner Join users Natural Inner Join user_phone;" 
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAdminById(self, admin_id):
        cursor = self.conn.cursor()
        query = "Select * from admin Natural Inner Join users Natural Inner Join user_phone where admin_id = %s;"
        cursor.execute(query,(admin_id,))
        result = cursor.fetchone()
        return result

    def getAdminsByFirstname(self, admin_firstname):
        cursor = self.conn.cursor()
        query = "Select * from admin Natural Inner Join users Natural Inner Join user_phone where user_firstname = %s;"
        cursor.execute(query,(admin_firstname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminsByLastname(self, admin_lastname):
        cursor = self.conn.cursor()
        query = "Select * from admin Natural Inner Join users Natural Inner Join user_phone where user_lastname = %s;"
        cursor.execute(query,(admin_lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminsByEmail(self, admin_email):
        cursor = self.conn.cursor()
        query = "Select * from admin Natural Inner Join users Natural Inner Join user_phone where  user_email = %s;"
        cursor.execute(query,(admin_email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminsByFirstnameAndLastname(self, admin_firstname, admin_lastname):#verify if is need to change the var admin_name to user_name
        cursor = self.conn.cursor()
        query = "Select * from admin Natural Inner Join users Natural Inner Join user_phone where  user_firstname = %s and user_lastname = %s;"
        cursor.execute(query,(admin_firstname, admin_lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getAdminByPhone(self, admin_phone):
        cursor = self.conn.cursor()
        query = "Select * from users Natural Inner Join admin Natural Inner Join user_phone where user_phone = %s;"
        cursor.execute(query,(admin_phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminsByDateOfBirth(self, admin_date_birth):
        cursor = self.conn.cursor()
        query = "Select * from admin Natural Inner Join users Natural Inner Join user_phone where user_date_birth = %s;"
        cursor.execute(query,(admin_date_birth,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, user_id):
        cursor = self.conn.cursor()
        query = "insert into admin(user_id) values(%s) returning admin_id;"
        cursor.execute(query,(user_id,))
        admin_id = cursor.fetchone()[0]
        self.conn.commit()
        return admin_id

    def update(self, admin_id): #Verify this method and maybe fix implementations (tentative)
        cursor = self.conn.cursor()
        query = "Select * from users Natural Inner Join admin Natural Inner Join user_phone where admin_id = %s returning user_id;"
        cursor.execute(query,(admin_id,))
        user_id = cursor.fetchone()[0] #verify what it returns 
        return user_id

    def delete(self, user_id):
        cursor = self.conn.cursor()
        query = "delete from resource where user_id = %s;"
        cursor.execute(query,(user_id))
        self.conn.commit()
        return user_id