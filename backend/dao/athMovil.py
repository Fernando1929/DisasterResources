class AthMovilDAO:
    def __init__(self):
        super().__init__()

    def getAllAthMovil(self):
        result = [
            [1, 1, 1, "7877778888"],
            [2, 2, 2, "7878887777"]
        ]
        return result

    def getAthMovilById(self, ath_movil_id):
        result = [1, 1, 1, "7877778888"]
        return result

    def getAthMovilByPhone(self, ath_movil_phone):
        result = [1, 1, 1, "7877778888"]
        return result

    def insert(self, payment_id, ath_movil_phone):
        ath_movil_id = 1
        return ath_movil_id

    def update(self, ath_movil_id):
        payment_id = 1
        return payment_id

    def delete(self, ath_movil_id):
        payment_id = 1
        return payment_id