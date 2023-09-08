import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

email = driver.find_element(By.ID,"Email")
email.clear()
email.send_keys("admin@yourstore.com")

password = driver.find_element(By.ID,"Password")
password.clear()
password.send_keys("admin")

login = driver.find_element(By.XPATH,"//button[.='Log in']")
login.click()

#driver.execute_script("window.scrollBy(0,3000)","")
time.sleep(3)

element = driver.find_element(By.XPATH,"//div[@id='order-incomplete-report-card']")

driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(3)