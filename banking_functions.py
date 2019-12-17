from customer import Customer
from database import Database

class BankingFunctions:

    def __init__(self):
        self.customerObj = Customer()
        self.db          = Database()

        #Making all the relevant tables
        self.db.make_tables()

    def sign_up(self):

        first_name = input("Enter First Name:   ")
        last_name  = input("Enter Last Name:    ")
        age        = input("Enter Age:          ")
        city       = input("Enter City:         ")
        password   = input("Enter the password: ")

        #Setting all these values in customer object
        self.customerObj.setFirstName(first_name)
        self.customerObj.setLastName(last_name)
        self.customerObj.setage(age)
        self.customerObj.setCity(city)
        self.customerObj.setPassword(password)
        self.customerObj.setStatus("open")

        #Save the information in database
        self.db.sign_up_customer(self.customerObj)