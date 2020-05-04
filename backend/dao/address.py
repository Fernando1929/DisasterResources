from config.dbconfig import pg_config
import psycopg2

class AddressDAO:
    
    # address: address_id, user_id, addressline, city, state_province, country, zipcode
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'],pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAddresses(self):
        cursor = self.conn.cursor()
        query = "Select * from address;" 
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressById(self, address_id):
        cursor = self.conn.cursor()
        query = "Select * from address where address_id = %s;"
        cursor.execute(query,(address_id,))
        result = cursor.fetchone()
        return result

    def getAddressesByCity(self, city):
        cursor = self.conn.cursor()
        query = "Select * from address where city = %s;" 
        cursor.execute(query,(city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByCountry(self, country):
        cursor = self.conn.cursor()
        query = "Select * from address where country = %s;" 
        cursor.execute(query,(country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByZipcode(self, zipcode):
        cursor = self.conn.cursor()
        query = "Select * from address where zipcode = %s;" 
        cursor.execute(query,(zipcode,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStateOrProvince(self, state_province):
        cursor = self.conn.cursor()
        query = "Select * from address where state_province = %s;" 
        cursor.execute(query,(state_province,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByCityAndCountry(self, city, country):
        cursor = self.conn.cursor()
        query = "Select * from address where city = %s and country = %s;" 
        cursor.execute(query,(city,country))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "Select * from address where user_id = %s" 
        cursor.execute(query,(user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, user_id, addressline, city, state_province, country, zipcode):
        cursor = self.conn.cursor()
        query = "insert into address(user_id, addressline, city, state_province, country, zipcode) values (%s, %s, %s, %s, %s, %s) returning address_id;"
        cursor.execute(query, (user_id, addressline, city, state_province, country, zipcode))
        address_id = cursor.fetchone()[0]
        self.conn.commit()
        return address_id

    def update(self, address_id, user_id, addressline, city, state_province, country, zipcode):
        cursor = self.conn.cursor()
        query = "update address set user_id = %s, addressline = %s, city = %s, state_province = %s, country = %s, zipcode = %s where address_id = %s;" #verify query
        cursor.execute(query, (user_id, addressline, city, state_province, country, zipcode, address_id))
        self.conn.commit()
        return address_id

    def delete(self, address_id):
        cursor = self.conn.cursor()
        query = "delete form address where address_id = %s ;" #verify query
        cursor.execute(query, (address_id,))
        self.conn.commit()
        return address_id