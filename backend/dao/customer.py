class CustomerDAO:
    def __init__(self):
        super().__init__()

    # Customer = user_id, customer_id, customer_firstname, customer_lastname, customer_date_birth, customer_email, customer_phone
    def getAllCustomer(self):
        result = [
            ["1",  "1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777"],
            ["2",  "2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888"]
        ]
        return result

    def getCustomerById(self, customer_id):
        result = ["1", "1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777"]
        return result

    def getCustomerByFirstname(self, customer_firstname):
        result = [
            ["1",  "1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777"],
            ["2",  "2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888"]
        ]
        return result

    def getCustomerByLastname(self, customer_lastname):
        result = [
            ["1",  "1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777"],
            ["2",  "2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888"]
        ]
        return result

    def getCustomerByFirstnameAndLastname(self, customer_firstname, customer_lastname):
        result = [
            ["1",  "1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777"],
            ["2",  "2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888"]
        ]
        return result

    def getCustomerByEmail(self, customer_email):
        result = [
            ["1",  "1", "Alex", "Vargas", "05/15/1992", "alexvargas1@gmail.com", "787-777-7777"],
            ["2",  "2", "Sam", "Scarlet", "01/03/1996", "sammyscarlet7@gmail.com", "787-777-8888"]
        ]
        return result

    def insert(self, customer_id):
        return customer_id

    def update(self, customer_id):
        user_id = 1
        return user_id

    def delete(self, customer_id):
        user_id = 1
        return user_id