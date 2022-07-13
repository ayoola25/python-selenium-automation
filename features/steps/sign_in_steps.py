from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# ORDERS_LNK = (By.CSS_SELECTOR, "a[href*='/gp/css/order-history?ref_=nav_orders_first']")
SEARCH_RESULT_TEXT = (By.NAME, 'Sign-In')


@when('Click Amazon Orders link')
def click_on(context):
    # context.driver.find_element(*ORDERS_LNK).click()
    context.app.header.click_orders_link()

@then('Verify Sign In page is opened')
def verify_signin_opened(context):
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin?_encoding=UTF8&accountStatusPolicy=P1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_orders_first&pageId=webcs-yourorder&showRmrMe=1'))
    context.app.signin_page.verify_signin_page_is_opened()

