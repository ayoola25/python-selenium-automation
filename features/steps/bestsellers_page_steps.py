from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

FIVE_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

@given('Open Amazon Bestsellers page')
def open_amazon_bestsellers_page(context):
    # context.driver.get('https://www.amazon.com/gp/bestsellers/')
    context.app.bestsellers_page.open_bestsellers()


@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    # actual_links = context.driver.find_elements(*FIVE_LINKS)
    # assert len(actual_links) == int(expected_links), \
    #     f'Expected! {expected_links} but got {actual_links}'
    context.app.bestsellers_page.verify_links_present(expected_links)

@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    five_links = context.driver.find_elements(*FIVE_LINKS)

    for x in range(len(five_links)):
        link_to_click = context.driver.find_elements(*FIVE_LINKS)[x]
        link_text = link_to_click.text
        link_to_click.click()
        sleep(1)
        header_test = context.driver.find_element(*HEADER).text
        assert link_text in header_test, f'Expected {link_text} to be in {header_test}'
