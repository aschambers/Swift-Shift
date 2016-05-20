"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Employees'
routes['POST']['/register'] = 'Employees#register'
routes['POST']['/login'] = 'Employees#login'
routes['GET']['/dashboard'] = 'Employees#dashboard'
routes['GET']['/admindash'] = 'Employees#admindash'
routes['GET']['/logout'] = 'Employees#logout'
routes['GET']['/addemployee'] = 'Employees#add_employee'
routes['GET']['/addcustomer'] = 'Employees#add_customer'
routes['GET']['/edit/<id>'] = 'Employees#edit_employee'
routes['POST']['/update/<id>'] = 'Employees#update_employee'
routes['GET']['/editprofile/<id>'] = 'Employees#edit_profile'
routes['GET']['/showemployee/<id>'] = 'Employees#show_employee'
routes['GET']['/edit/new/<id>'] = 'Employees#edit_customer'
routes['GET']['/show/new/<id>'] = 'Employees#show_customer'
routes['POST']['/update/customer/<id>'] = 'Employees#update_customer'
routes['POST']['/update/profile/<id>'] = 'Employees#update_profile'
routes['POST']['/update/new/<id>'] = 'Employees#process_customer'
routes['POST']['/process'] = 'Employees#process_employee'
routes['POST']['/new/customer'] = 'Employees#new_customer'
routes['GET']['/destroy/employee/<id>'] = 'Employees#destroy_employee'
routes['GET']['/destroy/customer/<id>'] = 'Employees#destroy_customer'
routes['GET']['/dispatch'] = 'Employees#dispatch'
routes['GET']['/getjob'] = 'Employees#get_job'
routes['GET']['/dispatchone'] = 'Employees#dispatchone'
routes['GET']['/dispatchtwo'] = 'Employees#dispatchtwo'
routes['GET']['/fools'] = 'Employees#fools' 
routes['GET']['/call'] = 'Employees#call'
routes['GET']['/text'] = 'Employees#text'
"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
