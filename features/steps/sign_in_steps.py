from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# ORDERS_LNK = (By.CSS_SELECTOR, "a[href*='/gp/css/order-history?ref_=nav_orders_first']")
from features.steps.amazon_main_page_steps import SIGN_IN_BTN

SEARCH_RESULT_TEXT = (By.NAME, 'Sign-In')


@when('Click Amazon Orders link')
def click_on(context):
    # context.driver.find_element(*ORDERS_LNK).click()
    context.app.header.click_orders_link()


@when('Click on button from SignIn popup')
def click_sign_in_btn(context):
    sign_in_btn = context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable'
    )
    sign_in_btn.click()


@when('wait for {seconds} seconds')
def wait_sec(context, seconds):
    sleep(int(seconds)) # "5" => 5


@then('Verify Sign In page is opened')
def verify_signin_opened(context):
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'), message = 'Sign In page never opened')
    context.app.signin_page.verify_signin_page_is_opened()


@then('SignIn popup is present')
def verify_signin_popup_present(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable')


@then('SignIn popup disappears')
def verify_signin_popup_not_present(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn did not disappear')
