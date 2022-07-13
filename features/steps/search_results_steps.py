from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class = 'a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")


@then('Verify search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    # actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    # assert expected_result == actual_result, f"Error! Actual text {actual_result} did not match Expected {expected_result}"
    context.app.search_results_page.verify_search_results(expected_result)
