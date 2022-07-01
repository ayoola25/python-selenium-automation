from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@given('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    print(context.driver.window_handles)


@when('click on Amazon Privacy Notice link')
def click_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print("\nAfter click, windows:", context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))


@then('Close Privacy Notice')
def close_privacy_notice(context):
    context.driver.close()


@then('User can close new window and switch back to original window')
def return_to_original(context):
    context.driver.switch_to.window(context.original_window)

