from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app()

@given('Store original window')
def store_window(context):
    context.original_window = context.app.target_app_page.get_current_window_id()
    sleep(2)
    # print(context.original_window)
    # print(context.driver.window_handles) - gets all window handles

@when('Click Privacy Policy link')
def click_privacy_link(context):
    context.app.target_app_page.click_privacy_link()

@when('Switch to new window')
def switch_window(context):
    # sleep(2)
    # all_windows = context.driver.window_handles
    # print(context.driver.window_handles)
    #
    # context.driver.switch_to.window(all_windows[1])
    # print('Current: ', context.driver.current_window_handle)
    # sleep(15)
    context.app.base_page.switch_to_new_window()

@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.privacy_policy_page.verify_pp_opened()

@then('Close current page')
def close_page(context):
    context.app.base_page.close_window()

@then('Return to original window')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)