from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@class='sg-col-inner']//span[@class='a-price']")
ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    context.driver.wait.until(EC.invisibility_of_element_located(ADD_TO_CART_BUTTON))


