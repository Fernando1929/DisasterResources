class CustomerDAO:
    def __init__(self):
        super().__init__()

    # Customer = user_id, user_firstname, user_lastname, user_date_birth, user_email, user_phone, customer_id
    def getAllCustomers(self):
        result = [
            ["1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777" , "1"],
            ["2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888" , "2"]
        ]
        return result

    def getCustomerById(self, customer_id):
        result = ["1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777" , "1"]
        return result

    def getCustomerByFirstname(self, customer_firstname):
        result = [
            ["1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777" , "1"],
            ["2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888" , "2"]
        ]
        return result

    def getCustomerByLastname(self, customer_lastname):
        result = [
            ["1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777" , "1"],
            ["2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888" , "2"]
        ]
        return result
    def getCustomerByFirstnameAndLastname(self, customer_firstname, customer_lastname):
        result = [
            ["1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777" , "1"],
            ["2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888" , "2"]
        ]
        return result

    def getCustomerByEmail(self, customer_email):
        result = [
            ["1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777" , "1"],
            ["2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888" , "2"]
        ]
        return result

    def insert(self, customer_id):
        customer_id = 1
        return customer_id

    def update(self, customer_id):
        user_id = 1
        return user_id

    def delete(self, customer_id):
        user_id = 1
        return user_id