import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import *
from pageObjects.Add_Customer import *
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_002_Add_Customer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmail()
    password1 = ReadConfig.SetPassword_()
    firstname = ReadConfig.getFirstName()
    lastname = ReadConfig.getLastName()
    companyname = ReadConfig.getCompanyName()
    admincomment = ReadConfig.getAdminComment()
    dob = ReadConfig.getDOB()
    companyname = ReadConfig.getCompanyName()
    admincomment = ReadConfig.getAdminComment()

    logger = LogGen.loggen()

    def test_Add_cust(self,setup):
        self.logger.info("****** Test_002_Add Customer ******")
        self.logger.info("****** Adding customer ******")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.ac = AddCustomer(self.driver)
        self.ac.customerMenu()
        self.ac.clickCustomers()
        self.ac.addNewCustomer()
        self.ac.setEmail(self.email)
        self.ac.setPassword(self.password1)
        self.ac.setFirstName(self.firstname)
        self.ac.setLastName(self.lastname)
        self.ac.male_RadioBtn()
        # self.ac.DOB(self.dob)
        self.ac.COmpanyName(self.companyname)
        self.ac.Checkbox_Click()
        self.ac.DrpDown()
        self.ac.adminComment(self.admincomment)
        self.ac.Save()
        self.logger.info("****** Customer Added ******")

        time.sleep(3)

        actual_msg = self.driver.find_element(By.XPATH,"//div[@class='content-wrapper']/div[1]").text
        #print("Actual message: ",actual_msg)

        if 'successfully.' in actual_msg:
            assert True
            self.logger.info("****** Test_002 Is PASSED ******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Add_Cust.png")
            self.driver.close()
            self.logger.error("****** Add customer test is Failed ******")
            assert False
        time.sleep(3)


