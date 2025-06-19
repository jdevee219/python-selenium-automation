from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Opening the webpage
@given('Open target main page')
def open_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()

# Open Target Circle
@given('Open Target Circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')


# Sign In sidebar on Main page
@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    assert expected_text == actual_text, f'Error, expected {expected_text} did not match {actual_text}'