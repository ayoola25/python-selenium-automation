from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ICON_BTN = (By.XPATH, "//div[@id='nav-cart-count-container']//span[@class='nav-cart-icon nav-sprite']")


@when('click on {icon_pic}')
def click_on(context, icon_pic):
    context.driver.find_element(*ICON_BTN).click()



