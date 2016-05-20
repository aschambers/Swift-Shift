from system.core.model import Model
import re

class Employee(Model):
    def __init__(self):
        super(Employee, self).__init__()
    def register_employee(self,employee_info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not employee_info['first_name']:
            errors.append('First Name cannot be empty')
        if len(employee_info['first_name']) < 3:
            errors.append('First Name must be longer than 3 character')
        if not employee_info['last_name']:
            errors.append('Name cannot be empty')
        if len(employee_info['last_name']) < 3:
            errors.append('Last Name must be longer than 3 character')
        if not employee_info['email']:
            errors.append('Email field cannot be empty')
        if not EMAIL_REGEX.match(employee_info['email']):
            errors.append('Email not a valid format')
        if not employee_info['password']:
            errors.append('Password field cannot be empty')
        if len(employee_info['password']) < 8:
            errors.append('Password must be longer than 7 characters')
        if not employee_info['confirm_password']:
            errors.append('Confirm Password field cannot be empty')
        if employee_info['password'] != employee_info['confirm_password']:
            errors.append('Passwords do not match')
            print errors
        if errors:
            return {'status': False, 'errors' : errors}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(employee_info['password'])
            #uses %s for user input + string type, %d would be an int value you'd like to insert into database. 
            query = "INSERT INTO employees (first_name,last_name,email,password,employee_level,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,NOW(),NOW())"
            data = [employee_info['first_name'],employee_info['last_name'],employee_info['email'],hashed_pw,employee_info['employee_level']]
            self.db.query_db(query, data)
            get_employee = "SELECT * FROM employees ORDER BY id DESC LIMIT 1"
            employee = self.db.query_db(get_employee)
            return {'status' : True , 'employee' : employee[0]}

    def login_employee(self, employee_info):
        errors = []
        if not employee_info['password']:
            errors.append('Password Cannot be empty')
        if not employee_info['email']:
            errors.append('Email Cannot be empty')
        if errors:
            return {'status' : False, 'errors': errors}
        else:
            query = 'SELECT * FROM employees WHERE email = %s'
            data = [employee_info['email']]
            employee = self.db.query_db(query,data)
            if len(employee) > 0:
                if self.bcrypt.check_password_hash(employee[0]['password'], employee_info['password']):
                    return {'status' : True, 'employee' : employee[0]}
                else:
                    errors.append('Password or Email is Invalid')
                    return {'status' : False, 'errors': errors}
            else:
                errors.append('Email was not found')
                return {'status' : False, 'errors': errors}

    def change_to_admin(self):
        query = "UPDATE employees SET employees.employee_level='admin'"
        self.db.query_db(query)
    
    def select_all_employees(self):
        query = "SELECT * FROM employees"
        return self.db.query_db(query)       

    def select_employee_by_id(self, id):
        query = "SELECT * FROM employees WHERE id = '{}'".format(id)
        return self.db.query_db(query)

    def update_employee(self, data):
        query = "UPDATE employees SET first_name=%s, last_name=%s, email=%s, address=%s, employee_id=%s, hiredate=%s, workday=%s, employee_level=%s, phone=%s WHERE id=%s"
        data_info = [data['first_name'], data['last_name'], data['email'], data['address'], data['employee_id'], data['hiredate'], data['workday'], data['employee_level'], data['phone'], data['id']]
        return self.db.query_db(query, data_info)

    def update_info(self, profile):
        query = "UPDATE employees SET first_name=%s, last_name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
        data_info = [profile['first_name'], profile['last_name'], profile['email'], profile['phone'], profile['address'], profile['id']]
        return self.db.query_db(query, data_info)

    def destroy_employee(self, id):
        query = "DELETE FROM employees WHERE id = %s"
        data = [id]
        return self.db.query_db(query, data)

    def destroy_customer(self, id):
        query = "DELETE FROM customers WHERE id = %s"
        data = [id]
        return self.db.query_db(query, data)

    def get_job(self):
        query = "SELECT customers.id, customers.first_name, customers.last_name, customers.phone, customers.address FROM customers ORDER BY RAND() LIMIT 1"
        return self.db.query_db(query)
