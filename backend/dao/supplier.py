class SupplierDAO:

    def __init__(self):
        super().__init__()
        
    #supplier = user_id, supplier_id, supplier_firstname, supplier_lastname, supplier_date_birth, supplier_email, supplier_phone

    def getAllSuppliers(self):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999'],
            [2, 2, 'Miranda', 'Torres', '23/12/85', 'mtorres@gymail.com', '9999999999']
        ]
        return result
    
    def getSupplierById(self, supplier_id):
        result = [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        return result

    def getAllSupplierResources(self, supplier_id):
        result = [
           [1, 2, 'Battery', 'Duracel', 10, 7.00],
           [1, 3, 'ice', 'el angel', 10, 2.50],
           [1, 4, 'generator', 'CAT', 8, 500]
        ]
        return result

    def getSuppliersByFirstnameAndLastname(self,supplier_firstname, supplier_lastname):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def getSuppliersByFirstname(self,supplier_firstname):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def getSuppliersByLastname(self,supplier_lastname):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result
        
    def getSupplierByEmail(self,supplier_email):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result
    
    def getSupplierByPhone(self,supplier_phone):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result
    
    def getSuppliersByDateOfBirth(self,supplier_date_birth):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999']
        ]
        return result

    def getSuppliersByCompanyId(self, company_id):
        result = [
            [1, 1, 'Julio', 'Ramires', '23/01/89', 'jramires@gymail.com', '7879999999'],
            [2, 2, 'Miranda', 'Torres', '23/12/85', 'mtorres@gymail.com', '9999999999']
        ]
        return result

    def insert(self, supplier_firstname, supplier_lastname, supplier_date_birth, supplier_email, supplier_phone):
        resource_id = 1
        return resource_id

    def update(self, supplier_id):
        resource_id = 1
        return resource_id

    def delete(self, supplier_id):
        resource_id = 1
        return resource_id

    