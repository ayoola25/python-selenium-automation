from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify search results for "coffee" are shown')
def verify_search_results(context):
    expected_result = '"coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text
    assert expected_result == \
           actual_result, f"Error! Actual text {actual_result} did not match Expected {expected_result}"