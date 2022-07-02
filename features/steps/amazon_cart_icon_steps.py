from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ICON_BTN = (By.XPATH, "//div[@id='nav-cart-count-container']//span[@class='nav-cart-icon nav-sprite']")


@when('click on cart_icon')
def click_on(context):
    context.driver.find_element(*ICON_BTN).click()



