from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART = (By.ID, "nav-cart-count")


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == \
           actual_text, f'Expected! {expected_count} but got {actual_text}'
