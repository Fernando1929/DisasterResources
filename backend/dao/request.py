class RequestDAO:

    def __init__(self):
        super().__init__()

    def getAllRequest(self):
        result = [
            [1, 1, "Water Request", 10, "3/16/2020"],
            [2, 1, "Cloth Request", 2, "3/16/2020"]
        ]
        return result

    def getRequestById(self, request_id):
        result = [2, 1, "Cloth Request", 2, "3/16/2020"]
        return result

    def getRequestByCustomerId(self, customer_id):
        result = [
            [1, 1, "Water Request", 10, "3/16/2020"],
            [2, 1, "Cloth Request", 2, "3/16/2020"]
        ]
        return result

    def getRequestByTitle(self, request_title):
        result = [
            [1, 1, "Water Request", 10, "3/16/2020"],
            [2, 1, "Cloth Request", 2, "3/16/2020"]
        ]
        return result

    def insert(self, customer_id, request_title, request_quantity, request_date):
        request_id = 1
        return request_id

    def update(self, request_id, customer_id, request_title, request_quantity, request_date):
        return request_id

    def delete(self, request_id):
        return request_id