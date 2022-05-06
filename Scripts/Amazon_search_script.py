from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')

driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"coffee"'
actual_result = driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text

assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}"
print('Test case Passed')
driver.quit()