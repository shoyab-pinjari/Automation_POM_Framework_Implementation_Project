import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    left_menu_customer = "//nav[@class='mt-2']/ul/li[4]"
    customer_click = "//a[@href='/Admin/Customer/List']"
    textbox_Email = "//input[@id='Email' and @name='Email']"
    textbox_Password = "//input[@id='Password' and @name='Password']"
    textbox_FirstName = "//input[@id='FirstName' and @name='FirstName']"
    textbox_LastName = "//input[@id='LastName' and @name='LastName']"
    radiobtn_Male = "//input[@id='Gender_Male']"
    radiobtn_Female = "//input[@id='Gender_Female']"
    datepicker_DOB = "//span[@class='k-select' and @role='button']"
    textbox_CompanyName = "//input[@id='Company' and @name='Company']"
    checkbox_IsTaxExempt = "//input[@class='check-box' and @id='IsTaxExempt']"
    dropdown_manager_of_vendor = "//select[@id='VendorId' and @name='VendorId']"
    textbox_AdminComment = "//div[@class='col-md-9']//textarea"
    button_save = "//button[@name='save' and @type='submit']"
    button_AddCustomer = "//form[@action='/Admin/Customer/List']/div/div/a"
    dob_datepicker = "//input[@id='DateOfBirth']"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.textbox_Email).clear()
        self.driver.find_element(By.XPATH,self.textbox_Email).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_Password).clear()
        self.driver.find_element(By.XPATH,self.textbox_Password).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH,self.textbox_FirstName).clear()
        self.driver.find_element(By.XPATH, self.textbox_FirstName).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH,self.textbox_LastName).clear()
        self.driver.find_element(By.XPATH, self.textbox_LastName).send_keys(lastname)

    def customerMenu(self):
        self.driver.find_element(By.XPATH,self.left_menu_customer).click()

    def clickCustomers(self):
        self.driver.find_element(By.XPATH, self.customer_click).click()
        time.sleep(3)

    def addNewCustomer(self):
        self.driver.find_element(By.XPATH,self.button_AddCustomer).click()

    def male_RadioBtn(self):
        self.driver.find_element(By.XPATH,self.radiobtn_Male).click()

    # def DOB(self,dob):
    #     self.driver.find_element(By.XPATH,self.dob_datepicker).send_keys(dob)

    def COmpanyName(self,companyname):
        self.driver.find_element(By.XPATH,self.textbox_CompanyName).send_keys(companyname)

    def Checkbox_Click(self):
        self.driver.find_element(By.XPATH,self.checkbox_IsTaxExempt).click()

    def DrpDown(self):
        ele = self.driver.find_element(By.XPATH,self.dropdown_manager_of_vendor)
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        drpd = Select (self.driver.find_element(By.XPATH,self.dropdown_manager_of_vendor))
        alloptions =drpd.options
        for opt in alloptions:
            if opt.text=="James Smith":
                opt.click()
                break

    def adminComment(self,admincomment):
        self.driver.find_element(By.XPATH,self.textbox_AdminComment).send_keys(admincomment)

    def Save(self):
        self.driver.find_element(By.XPATH,self.button_save).click()