from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.saucedemo.com/')

user_name = driver.find_element(By.ID, 'user-name').send_keys('standard_user')
time.sleep(2)

password = driver.find_element(By.ID, 'password').send_keys('secret_sauce')
time.sleep(2)

buttonClick = driver.find_element(By.ID, 'login-button').click()
time.sleep(2)

click_Burgerbutton = driver.find_element(By.ID, 'react-burger-menu-btn').click()
time. sleep(3)

print('click burger success')