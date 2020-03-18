from config.dbconfig import pg_config
import psycopg2

class ResourceDAO:
    def _init_(self):
        super().__init__()

    def insert(self, supplier_id, name, brand, quantity, price):
        resource_id = 1
        return resource_id

    def update(self, resource_id, supplier_id, name, brand, quantity, price):
        return resource_id

    def delete(self, resource_id):
        return resource_id