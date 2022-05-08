from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULT_TEXT = (By.XPATH, "//div[@id='sc-active-cart']//*[contains(text(),'Your Amazon Cart is empty')]")

@then('Verify click result {expected_result} is shown')
def verify_click_result(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert expected_result == \
           actual_result, f"Error! Actual text {actual_result} did not match Expected {expected_result}"


