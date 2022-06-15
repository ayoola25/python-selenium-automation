from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

FIVE_LINKS = (By.CSS_SELECTOR, '#zg_header a')

@given('Open Amazon Bestsellers page')
def open_amazon_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/')

@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*FIVE_LINKS)
    assert len(actual_links) == \
           int(expected_links), f'Expected! {expected_links} but got {actual_links}'
