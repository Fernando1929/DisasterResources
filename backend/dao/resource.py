class ResourceDAO:
    def _init_(self):
        super()._init_()

    def insert(self, supplier_id, address, name, brand, quantity, price):
        resource_id = 1
        return resource_id

    def update(self, resource_id, address, supplier_id, name, brand, quantity, price):
        return resource_id

    def delete(self, resource_id):
        return resource_id