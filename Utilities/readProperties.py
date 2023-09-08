import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    # Add new customer
    @staticmethod
    def getEmail():
        email = config.get('add new customer', 'email')
        return email

    @staticmethod
    def SetPassword_():
        password = config.get('add new customer', 'password')
        return password

    @staticmethod
    def getFirstName():
        firstname = config.get('add new customer', 'firstname')
        return firstname

    @staticmethod
    def getLastName():
        lastname = config.get('add new customer', 'lastname')
        return lastname

    @staticmethod
    def getCompanyName():
        companyname = config.get('add new customer', 'companyname')
        return companyname

    @staticmethod
    def getAdminComment():
        admincomment = config.get('add new customer', 'admincomment')
        return admincomment

    @staticmethod
    def getDOB():
        dob = config.get('add new customer', 'dob')
        return dob

    @staticmethod
    def getCompanyName():
        companyname = config.get('add new customer', 'companyname')
        return companyname

    @staticmethod
    def getAdminComment():
        admincomment = config.get('add new customer', 'admincomment')
        return admincomment