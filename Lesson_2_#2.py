from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.maximize_window()

baseUrl = 'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'
driver.get(baseUrl)

print('Amazon logo:')
logoByXpath = driver.find_element(By.XPATH, '//div[@id="a-page"]/div[1]/div[1]/div/a/i')
if logoByXpath is not None:
    print('We found logo element by Xpath')

logoByXpath = driver.find_element(By.XPATH, "//div[@id='a-page']//a[@href='/ref=ap_frn_logo']/i[@role='img']")
if logoByXpath is not None:
    print('We found logo element by  another Xpath')

logoByCss = driver.find_element(By.CSS_SELECTOR, "[role='img']")
if logoByCss is not None:
    print('We found logo element by CSS')
    print('***********************************************************')

print('Amazon Email Field:')
emailById = driver.find_element(By.ID, 'ap_email')
if emailById is not None:
    print('We found Email element by ID')

emailByName = driver.find_element(By.NAME, 'email')
if emailByName is not None:
    print('We found Email element by Name')

emailByXpath = driver.find_element(By.XPATH, '//input[@id="ap_email"]')
if emailByXpath is not None:
    print('We found Email element by XPATH')

emailByCss = driver.find_element(By.CSS_SELECTOR, "input[class*='a-input-text']")
if emailByCss is not None:
    print('We found Email element by CSS')
    print('***********************************************************')

print('Amazon Continue button:')
contiById = driver.find_element(By.ID, 'continue')
if contiById is not None:
    print('We found "Continue" element by ID')

contiByXpath = driver.find_element(By.XPATH, '//input[@id="continue"]')
if contiByXpath is not None:
    print('We found "Continue" element by XPATH')

contiByCss = driver.find_element(By.CSS_SELECTOR, 'input[id=continue]')
if contiByCss is not None:
    print('We found "Continue" element by CSS')
    print('***********************************************************')

print('Amazon Need Help Link:')
helpByXpath = driver.find_element(By.XPATH, "//div[@id='a-page']//i[@class='a-icon a-icon-logo']")


if helpByXpath is not None:
    print('We found "Need Help" Link element by Xpath')

helpByCss = driver.find_element(By.CSS_SELECTOR, "span[class=a-expander-prompt]")
if helpByCss is not None:
    print('We found "Need Help" Link element by CSS')
    print('***********************************************************')

print('Amazon Forgot your Password:')
forgotById = driver.find_element(By.ID, 'auth-fpp-link-bottom' )
if forgotById is not None:
    print('We found "Forgot your Password" element by ID')

forgotByXpath = driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
if forgotByXpath is not None:
    print('We found "Forgot your Password" element by XPATH')

forgotByCss = driver.find_element(By.CSS_SELECTOR, 'a[class=a-link-normal]')
if forgotByCss is not None:
    print('We found "Forgot your Password" element by CSS')
    print('***********************************************************')

print('Amazon Other issues with Sign-In link:')
otherById = driver.find_element(By.ID, 'ap-other-signin-issues-link' )
if otherById is not None:
    print('We found "Other issues with Sign-In" Link element by ID')

otherByXpath = driver.find_element(By.XPATH, '//a[@id="ap-other-signin-issues-link"]')
if otherByXpath is not None:
    print('We found "Other issues with Sign-In" Link by XPATH')

otherByCss = driver.find_element(By.CSS_SELECTOR, 'a[id=ap-other-signin-issues-link]')
if otherByCss is not None:
    print('We found "Other issues with Sign-In" Link element by CSS')
    print('***********************************************************')

print('Amazon Create your Amazon account button:')
createById = driver.find_element(By.ID, 'createAccountSubmit' )
if createById is not None:
    print('We found "Create your Amazon account" button element by ID')

createByXpath = driver.find_element(By.XPATH, '//a[@id="createAccountSubmit"]')
if createByXpath is not None:
    print('We found "Create your Amazon account" button element by XPATH')

createByCss = driver.find_element(By.CSS_SELECTOR, 'a[id=createAccountSubmit]')
if createByCss is not None:
    print('We found "Create your Amazon account" button element by CSS')
    print('***********************************************************')

print('Amazon Conditions of use link:')
condByXpath = driver.find_element(By.XPATH, "//div[@id='a-page']//a[text()='Conditions of Use']")
if condByXpath is not None:
    print('We found "Conditions of use" link element by Xpath')
    print('***********************************************************')

print('Amazon Privacy Notice link:')
privByXpath = driver.find_element(By.XPATH, "//div[@id='a-page']//a[text()='Privacy Notice']")
if privByXpath is not None:
    print('We found "Privacy Notice" link element by Xpath')

driver.quit()