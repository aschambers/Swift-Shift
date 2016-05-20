from system.core.model import Model
import re

class Customer(Model):
    def __init__(self):
        super(Customer, self).__init__()

    def select_all_customers(self):
        query = "SELECT * FROM customers"
        return self.db.query_db(query)

    def select_customer_by_id(self, id):
        query = "SELECT * FROM customers WHERE id = '{}'".format(id)
        return self.db.query_db(query)

    def update_customer(self, update):
        query = "UPDATE customers SET first_name=%s, last_name=%s, phone=%s, address=%s WHERE id=%s"
        data_info = [update['first_name'], update['last_name'], update['phone'], update['address'], update['id']]
        return self.db.query_db(query, data_info)

    def new_customer(self,customer_info):
        errors = []
        if not customer_info['first_name']:
            errors.append('First Name cannot be empty')
        if len(customer_info['first_name']) < 3:
            errors.append('First Name must be longer than 3 character')
        if not customer_info['last_name']:
            errors.append('Name cannot be empty.')
        if len(customer_info['last_name']) < 3:
            errors.append('Last Name must be longer than 3 character')
        if not customer_info['phone']:
        	errors.append('You must enter a phone number.')
        if len(customer_info['phone']) < 9:
        	errors.append('Phone number is not valid')
        if not customer_info['address']:
        	errors.append('You must enter an address.')
        if errors:
            return {'status': False, 'errors' : errors}
        else:
            query = "INSERT INTO customers (first_name,last_name,phone,address,created_at,updated_at) VALUES (%s,%s,%s,%s,NOW(),NOW())"
            data = [customer_info['first_name'],customer_info['last_name'],customer_info['phone'],customer_info['address']]
            self.db.query_db(query, data)
            get_customer = "SELECT * FROM customers ORDER BY id DESC LIMIT 1"
            customer = self.db.query_db(get_customer)
            return {'status' : True , 'customer' : customer[0]}