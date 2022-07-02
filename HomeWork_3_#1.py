from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

baseUrl = 'https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'
driver.get(baseUrl)

logoByCSS = driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
if logoByCSS is not None:
    print('We found logo element by CSS')

acctByXPATH = driver.find_element(By.XPATH, "//div[@class='a-box a-spacing-extra-large']//h1[@class='a-spacing-small']")
if acctByXPATH is not None:
    print("We found 'Create Account' element by XPATH")

NameByID = driver.find_element(By.ID, 'ap_customer_name')
if NameByID is not None:
    print('We found Name element by ID')

emailByID = driver.find_element(By.ID, 'ap_email')
if emailByID is not None:
    print('We found Email element by ID')

psswdByID = driver.find_element(By.ID, 'ap_password')
if psswdByID is not None:
    print('We found Password element by ID')

charByXPATH = driver.find_element(By.XPATH, "//div[@class='auth-require-fields-match-group']//div[@class='a-alert-content']")
if charByXPATH is not None:
    print("We found 'PassWord Character' element by XPATH")

pcheckByID = driver.find_element(By.ID, 'ap_password_check')
if pcheckByID is not None:
    print("We found 'Re-enter Password' element by ID")

cntByID = driver.find_element(By.ID, 'continue')
if cntByID is not None:
    print('We found Continue element by ID')

useByCSS = driver.find_element(By.CSS_SELECTOR, "[href*='/gp/help/customer/display']")
if useByCSS is not None:
    print('We found "Conditions of Use" element by CSS')

privByCSS = driver.find_element(By.CSS_SELECTOR, "[href*='gp/help/customer/display.html']")
if privByCSS is not None:
    print('We found "Privacy Notice" element by CSS')

signByCss = driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')
if signByCss is not None:
    print('We found "Sign-in" element by CSS')

driver.quit()