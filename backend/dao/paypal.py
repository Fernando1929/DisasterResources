class PaypalDAO:
    def __init__(self):
        super().__init__()

    def getAllPaypal(self):
        result = [
            [1, 1, 1, "Sam23", "Samuel1234"],
            [2, 2, 2, "AliceRiz", "AliciaMartinez"]
        ]
        return result

    def getPaypalById(self, paypal_id):
        result = [1, 1, 1, "Sam23", "Samuel1234"]
        return result

    def getPaypalByUsername(self, paypal_username):
        result = [1, 1, 1, "Sam23", "Samuel1234"]
        return result

    def getPaypalByPassword(self, paypal_password):
        result = [1, 1, 1, "Sam23", "Samuel1234"]
        return result

    def insert(self, payment_id, paypal_username, paypal_password):
        paypal_id = 1
        return paypal_id

    def update(self, paypal_id):
        payment_id = 1
        return payment_id

    def delete(self, paypal_id):
        payment_id = 1
        return payment_id