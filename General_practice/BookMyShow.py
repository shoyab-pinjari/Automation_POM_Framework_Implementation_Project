import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver =webdriver.Chrome()
driver.maximize_window()

driver.get("https://in.bookmyshow.com/explore/home/pune")

movie = driver.find_element(By.XPATH,"//*[@id='https://in.bookmyshow.com/pune/movies/jawan/ET00330424-0']/div/div[2]/div/img")
movie.click()

book_ticket_btn = driver.find_element(By.XPATH,"//div[@id='super-container']//div[@class='sc-qswwm9-5 ghYvew']/div[2]/div/button")
book_ticket_btn.click()

time.sleep(2)