from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@id='nav-cart-count-container']//span[@class='nav-cart-icon nav-sprite']")
CART_BUTTON = (By.XPATH, "")

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click

@when('Click on add to cart button')
def click_add_to_cart_button(context):
    context.driver.find_element(*CART_BUTTON).click()
    sleep(1)


