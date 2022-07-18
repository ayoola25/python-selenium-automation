from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
# SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ORDERS_BTN = (By.ID, 'nav-orders')
INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()


@when('Search for {search_word}')
def search_amazon(context, search_word):
    # context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_amazon(search_word)


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select books department')
def select_dept(context):
    context.app.header.select_dept()


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()


@then("Verify books department is selected")
def verify_department(context):
    context.app.header.verify_department()


@then('Verify hamburger menu btn present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU_BTN)


@then('Verify there are {expected_amount} footer links')
def verify_footer_links_count(context, expected_amount):
    expected_amount = int(expected_amount)  # '38' => 38

    footer_links = context.driver.find_elements(*FOOTER_LINKS)  # [Webelement1, Webelement2, ..]

    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'
