from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
# SEARCH_BTN = (By.ID, 'nav-search-submit-button')


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()


@when('Search for {search_word}')
def search_amazon(context, search_word):
    # context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_amazon(search_word)




