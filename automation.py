from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

print('Show Message' in driver.page_source)

user_message = driver.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('wooooooooooooooooo')

show_message_button = driver.find_element(By.CSS_SELECTOR, '.btn')

show_message_button.click()
