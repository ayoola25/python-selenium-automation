from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')

SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class = 'a-color-state a-text-bold']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@then('Verify search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert expected_result == \
           actual_result, f"Error! Actual text {actual_result} did not match Expected {expected_result}"
