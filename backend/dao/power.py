from config.dbconfig import pg_config
import psycopg2

class PowerDAO:
    def _init_(self):
        super().__init__()

    def insert(self, supplier_id, condition, capacity):
        resource_id = 1
        return resource_id

    def update(self, power_id, supplier_id, condition, capacity):
        return power_id

    def delete(self, power_id):
        return power_id