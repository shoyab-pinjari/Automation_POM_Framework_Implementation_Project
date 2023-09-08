# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # //a[normalize-space()='September 2023']
#
# driver =webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
#
# uname = driver.find_element(By.XPATH,"//*[@id='Email']")
# uname.clear()
# uname.send_keys("admin@yourstore.com")
#
# password = driver.find_element(By.XPATH,"//*[@id='Password']")
# password.clear()
# password.send_keys("admin")
#
# login = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button")
# login.click()
#
# left_menu_panel = driver.find_elements(By.XPATH,"//nav[@class='mt-2']/ul/li/a")
#
# for i in left_menu_panel:
#     if i.text == "Sales":
#         i.click()
#         time.sleep(5)
#         break
#
# mywait = WebDriverWait(driver,10)
# shipments = mywait.until(EC.presence_of_element_located((By.XPATH,"//p[contains(.,'Shipments')]")))
# shipments.click()
#
# start_date = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/form[1]/section/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[2]/span/span/span")
# start_date.click()
#
# time.sleep(5)
#
#
#
# mon_yr = driver.find_element(By.XPATH,"//a[normalize-space()='September 2023']")
# print(mon_yr.text)
# backbtn = driver.find_element(By.XPATH,"//span[@class='k-icon k-i-arrow-60-left']")
#
# while True:
#     if mon_yr.text == 'May 2022':
#         time.sleep(2)
#         break
#     else:
#         backbtn.click()
#
# dates = driver.find_elements(By.XPATH,"//div[@class='k-calendar-view']//tbody/tr/td/a")
#
# for dt in dates:
#     if dt.text == '1':
#         dt.click()
#         time.sleep(2)
#
# time.sleep(3)