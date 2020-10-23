from selenium import webdriver
from testing import registration, login

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")


registration (driver, "dmitrijzz@gmail.com", "AzzPractic")
login (driver, "dmitrijzz@gmail.com", "AzzPractic")

driver.quit()
