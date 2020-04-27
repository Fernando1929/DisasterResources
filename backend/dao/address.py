from config.dbconfig import pg_config
import psycopg2
class AddressDAO:
    
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # address: address_id, user_id, addressline, city, state_province, country, zipcode

    def getAllAddresses(self):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressById(self, address_id):
        result = [1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def getAddressesByCity(self, city):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressesByCountry(self, country):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressesByZipcode(self, zipcode):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressesByStateOrProvince(self, state_province):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressesByCityAndCountry(self, city, country):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressesByUserId(self, user_id):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def insert(self, user_id, addressline, city, state_province, country, zipcode):
        cursor = self.conn.cursor()
        query = "insert into address(user_id, addressline, city, state_province, country, zipcode) values (%s, %s, %s, %s, %s, %s) returning address_id;"
        cursor.execute(query, (user_id, addressline, city, state_province, country, zipcode))
        address_id = cursor.fetchone()[0]
        self.conn.commit()
        return address_id

    def update(self, address_id, user_id, addressline, city, state_province, country, zipcode):
        return address_id

    def delete(self, address_id):
        return address_id
