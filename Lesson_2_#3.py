from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')
search_field = driver.find_element(By.ID, 'helpsearch')

search_field.send_keys('Cancel order')
search_field.send_keys(Keys.ENTER)

expected_result = 'Help & Customer Service'
actual_result = driver.find_element(By.XPATH, "//a[@class='cs-help-title']").text

assert expected_result == actual_result, f"Error!{expected_result} did not match actual {actual_result}"
print('Test Case Passed')

driver.quit()