from flask import jsonify
from dao.address import AddressDAO
from dao.user import UserDAO

class AddressHandler:

    def build_address_dict(self, row):
        result = {}
        result['address_id'] = row[0]
        result['user_id'] = row[1]
        result['addressline'] = row[2]
        result['city'] = row[3]
        result['state_province'] = row[4]
        result['country'] = row[5]
        result['zipcode'] = row[6]
        return result

    def build_address_attributes(self, address_id, user_id, addressline, city, state_province, country, zipcode):
        result = {}
        result['address_id'] = address_id
        result['user_id'] = user_id
        result['addressline'] = addressline
        result['city'] = city
        result['state_province'] = state_province
        result['country'] = country
        result['zipcode'] = zipcode
        return result

    def getAllAddresses(self):
        dao = AddressDAO()
        address_list = dao.getAllAddresses()
        result_list = []
        for row in address_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

    def getAddressById(self, address_id):
        dao = AddressDAO()
        row = dao.getAddressById(address_id)
        if not row:
            return jsonify(Error = "Address Not Found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address = address)

    def getAddressesByUserId(self, user_id):
        user_dao = UserDAO()
        if not user_dao.getUserById(user_id):
            return jsonify(Error = "User not found."), 404
        else:
            address_list = []
            result_list = []
            dao = AddressDAO()
            address_list = dao.getAddressesByUserId(user_id)
            # if not address_list:
            #     return jsonify(Error = "Address Not Found"), 404
            # else:
            for row in address_list:
                result = self.build_address_dict(row)
                result_list.append(result)
            return jsonify(Addresses = result_list)

    def searchAddresses(self, args):
        city = args.get("city")
        state_province = args.get("state_province")
        country = args.get("country")
        zipcode = args.get("zipcode")

        dao = AddressDAO()
        address_list = []
        if (len(args) == 1) and city:
            address_list = dao.getAddressesByCity(city)
        elif (len(args) == 1) and state_province:
            address_list = dao.getAddressesByStateOrProvince(state_province)
        elif (len(args) == 1) and country:
            address_list = dao.getAddressesByCountry(country)
        elif (len(args) == 1) and zipcode:
            address_list = dao.getAddressesByZipcode(zipcode)
        elif (len(args) == 2) and city and country:
            address_list = dao.getAddressesByCityAndCountry(city, country)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in address_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

    def insertAddress(self, json):
        user_id = json["user_id"]
        addressline = json["addressline"]
        city = json["city"]
        state_province = json["state_province"]
        country = json["country"]
        zipcode = json["zipcode"]

        if user_id and addressline and city and state_province and country and zipcode:
            address_dao = AddressDAO()
            address_id = address_dao.insert(user_id, addressline, city, state_province, country, zipcode)
            result = self.build_address_attributes(address_id, user_id, addressline, city, state_province, country, zipcode)
            return jsonify(Address = result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateAddress(self, address_id, json):
        address_dao = AddressDAO()
        if not address_dao.getAddressById(address_id):
            return jsonify(Error = "Address not found."), 404
        else:
            user_id = json["user_id"]
            addressline = json["addressline"]
            city = json["city"]
            state_province = json["state_province"]
            country = json["country"]
            zipcode = json["zipcode"]

            if user_id and addressline and city and state_province and country and zipcode:
                address_dao = AddressDAO()
                address_id = address_dao.update(address_id, user_id, addressline, city, state_province, country, zipcode)
                result = self.build_address_attributes(address_id, user_id, addressline, city, state_province, country, zipcode)
                return jsonify(Address = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteAddress(self, address_id):
        address_dao = AddressDAO()
        if not address_dao.getAddressById(address_id):
            return jsonify(Error = "Address not found."), 404
        else:
            address_dao.delete(address_id)
            return jsonify(DeleteStatus = "OK"), 200