from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ICON_BTN = (By.XPATH, "//div[@id='nav-cart-count-container']//span[@class='nav-cart-icon nav-sprite']")


@given('Navigate to Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('click on {icon_pic}')
def click_on(context, icon_pic):
    context.driver.find_element(*ICON_BTN).click()



