from system.core.controller import *
# from twilio.rest import TwilioRestClient
# import twilio.twiml

class Employees(Controller):
    def __init__(self, action):
        super(Employees, self).__init__(action)
        self.load_model('Employee')
        self.load_model('Customer')
    
    def index(self):
        return self.load_view('index.html')
    
    def register(self):
        employee_info = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password'],
        'employee_level' : 'employee'
        }
        create_status = self.models['Employee'].register_employee(employee_info)
        if create_status['status'] == True:
            session['id'] = create_status['employee']['id']
            if create_status['employee']['id'] == 1:
                self.models['Employee'].change_to_admin()
                return redirect('/admindash')
            else:
                return redirect('/dashboard')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')
   
    def login(self):
        employee_info = {
        'email' : request.form['email'],
        'password' : request.form['password']
        }
        my_status = self.models['Employee'].login_employee(employee_info)
        if my_status['status'] == True:
            if my_status['employee']['employee_level'] == 'admin' or my_status['employee']['employee_level'] == 'manager':
                session['id'] = my_status['employee']['id']
                session['first_name'] = my_status['employee']['first_name']
                session['last_name'] = my_status['employee']['last_name']
                session['email'] = my_status['employee']['email']
                session['phone'] = my_status['employee']['phone']
                session['address'] = my_status['employee']['address']
                return redirect('/admindash')
            else:
                session['id'] = my_status['employee']['id']
                session['first_name'] = my_status['employee']['first_name']
                session['last_name'] = my_status['employee']['last_name']
                session['email'] = my_status['employee']['email']
                session['phone'] = my_status['employee']['phone']
                session['address'] = my_status['employee']['address']
                return redirect('/dashboard')
        else:
            for message in my_status['errors']:
                flash(message, 'Login_errors')
            return redirect('/')
    
    def dashboard(self):
        employees = self.models['Employee'].select_all_employees()
        return self.load_view('dashboard.html', employees=employees)
        # return self.load_view('dispatchjob.html')
    
    def admindash(self):
        employees = self.models['Employee'].select_all_employees()
        customers = self.models['Customer'].select_all_customers()
        return self.load_view('admindash.html', employees=employees, customers=customers)
    
    def logout(self):
        session['id'] = ''
        session['first_name'] = ''
        session['last_name'] = ''
        session['email'] = ''
        session['password'] = ''
        return redirect('/')

    def process_employee(self):
        employee_info = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password'],
        'employee_level' : 'employee'
        }
        create_status = self.models['Employee'].register_employee(employee_info)
        if create_status['status'] == True:
            return redirect('/admindash')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/add_employee')

    def new_customer(self):
        customer_info = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'phone' : request.form['phone'],
        'address' : request.form['address']
        }
        create_status = self.models['Customer'].new_customer(customer_info)
        if create_status['status'] == True:
            return redirect('/admindash')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/add_customer')

    def add_employee(self):
        return self.load_view('addemployee.html')

    def add_customer(self):
        return self.load_view('addcustomer.html')

    def edit_employee(self, id):
        employees = self.models['Employee'].select_employee_by_id(id)
        return self.load_view('editemployee.html', employees=employees)

    def update_employee(self, id):
        data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'phone' : request.form['phone'],
        'address' : request.form['address'],
        'employee_id' : request.form['employee_id'],
        'hiredate' : request.form['hiredate'],
        'workday' : request.form['workday'],
        'employee_level' : request.form['employee_level'],
        'id' : id
        }
        self.models['Employee'].update_employee(data)
        return redirect('/admindash')

    def edit_profile(self, id):
        employees = self.models['Employee'].select_employee_by_id(id)
        return self.load_view('editprofile.html', employees=employees)

    def show_employee(self, id):
        employees = self.models['Employee'].select_employee_by_id(id)
        return self.load_view('showemployee.html', employees=employees)

    def show_customer(self, id):
        customers = self.models['Customer'].select_customer_by_id(id)
        return self.load_view('showcustomer.html', customers=customers)

    def edit_customer(self, id):
        customers = self.models['Customer'].select_customer_by_id(id)
        return self.load_view('editcustomer.html', customers=customers)

    def update_customer(self, id):
        update = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'phone' : request.form['phone'],
        'address' : request.form['address'],
        'id' : id
        }
        self.models['Customer'].update_customer(update)
        return redirect('/admindash')

    def update_profile(self, id):
        profile = {
        'first_name' : session['first_name'],
        'last_name' : session['last_name'],
        'email' : session['email'],
        'phone' : session['phone'],
        'address' : session['address'],
        'id' : id
        }
        self.models['Employee'].update_info(profile)
        return redirect('/dashboard')

    def dispatch(self):
        jobs = self.models['Employee'].get_job()
        return self.load_view('dispatch.html', jobs=jobs)

    def dispatchone(self):
        return redirect('/dispatch')

    def dispatchtwo(self):
        return redirect('/dispatch')

    def get_job(self):
        return redirect('/dispatch')

    def destroy_employee(self, id):
        self.models['Employee'].destroy_employee(id)
        return redirect('/admindash')

    def destroy_customer(self, id):
        self.models['Employee'].destroy_customer(id)
        return redirect('/admindash')

    def fools(self):
        return self.load_view('fools.html')

    # def call(self):
    #     account = "AC266b857d0aa9fed47804dc70894f7811"
    #     token = "cfbc9f1d252249675be1c5b463034e19"
    #     client = TwilioRestClient(account, token)
    #     client.calls.create(to="2097539260", from_="12093170952", url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    #     return redirect('/admindash')

    # def text(self):
    #     account = "AC266b857d0aa9fed47804dc70894f7811"
    #     token = "cfbc9f1d252249675be1c5b463034e19"
    #     client = TwilioRestClient(account, token)
    #     client.messages.create(to="+12097539260", from_="+12093170952", body="name")
    #     client.messages.get('SMded4cb9e199b78e382b3e98d035bcfa3') 
    #     return redirect('/admindash')