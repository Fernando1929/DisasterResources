# from config.dbconfig import pg_config
# import psycopg2

class AddressDAO:
    
    def __init__(self):
        super().__init__()

    # address: address_id, user_id, addressline, city, state_province, country, zipcode

    def getAllAddresses(self):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressById(self, address_id):
        result = [1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]
        return result

    def getAddressByCity(self, city):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressByCountry(self, country):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressByZipcode(self, zipcode):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressByStateOrProvince(self, state_province):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressByCityAndCountry(self, city, country):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def getAddressesByUserId(self, user_id):
        result = [[1,1, "Urb. La Quinta Calle Cartier F1", "Yauco", "N/A", "Puerto Rico", "00698"]]
        return result

    def insert(self, user_id, addressline, city, state_province, country, zipcode):
        address_id = 1
        return address_id

    def update(self, address_id, user_id, addressline, city, state_province, country, zipcode):
        return address_id

    def delete(self, address_id):
        return address_id
