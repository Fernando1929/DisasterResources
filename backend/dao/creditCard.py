class CreditCardDAO:
    def __init__(self):
        super().__init__()

    def getAllCreditCard(self):
        result = [
            [1, 1, 1, "Samuel Ramirez", "1234567898765432", "000", "02/23"],
            [2, 2, 2, "Alice Scarlet", "1234567898765432", "001", "01/23"]
        ]
        return result

    def getCreditCardById(self, creditcard_id):
        result = [1, 1, 1, "Samuel Ramirez", "1234567898765432", "000", "02/23"]
        return result

    def getCreditCardByName(self, creditcard_name):
        result = [
            [1, 1, 1, "Samuel Ramirez", "1234567898765432", "000", "02/23"],
            [2, 2, 2, "Alice Scarlet", "1234567898765432", "001", "01/23"]
        ]
        return result

    def getCreditCardByNumber(self, creditcard_number):
        result = [
            [1, 1, 1, "Samuel Ramirez", "1234567898765432", "000", "02/23"],
            [2, 2, 2, "Alice Scarlet", "1234567898765432", "001", "01/23"]
        ]
        return result

    def getCreditCardByCustomerId(self, customer_id):
        result = [1, 1, 1, "Samuel Ramirez", "1234567898765432", "000", "02/23"]
        return result

    def insert(self, payment_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date):
        creditcard_id = 1
        return creditcard_id

    def update(self, creditcard_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date):
        payment_id = 1
        return payment_id

    def delete(self, creditcard_id):
        payment_id = 1
        return payment_id