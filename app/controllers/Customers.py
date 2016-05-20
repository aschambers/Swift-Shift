from system.core.controller import *

class Customers(Controller):
    def __init__(self, action):
        super(Customers, self).__init__(action)
        self.load_model('Customer')
        self.load_model('Employee')
    
    def index(self):
        return self.load_view('index.html')