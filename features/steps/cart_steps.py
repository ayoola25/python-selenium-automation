from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then('Verify Your Amazon Cart is empty text present')
def verify_amazonCart_empty(context):
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart'))
    context.app.cart_page.verify_amazonCart_empty()
