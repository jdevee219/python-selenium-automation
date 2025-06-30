from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open sign in page')
def open_target_sign_in_page(context):
    context.app.target_sign_in_page.open_target_sign_in()

@when('Store original window')
def store_window(context):
    context.original_window = context.app.target_sign_in_page.get_current_window_id()
    sleep(2)

@when('Click on Target terms and conditions link')
def click_terms_link(context):
    context.app.target_sign_in_page.click_terms_link()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_conditions_page.verify_tc_opened()

@then('User can close new window and switch back to original')
def close_page(context):
    context.app.base_page.close_window()
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)