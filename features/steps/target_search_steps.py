from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

# Scenario: User can search for a product on Target
@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('Verify search worked')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"


# Scenario: User can view Cart on Target
@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartLink']").click()
    sleep(5)

@then('Verify "Your cart is empty" message is shown')
def verify_cart_message(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
    assert actual_text.text == 'Your cart is empty'


# Scenario: User can navigate to Sign In
@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    sleep(5)
    context.driver.find_element(By.XPATH, "//button[@type='button' and text()='Sign in or create account']").click()
    sleep(5)

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    expected_text = 'Sign in or create account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    assert expected_text == actual_text, f'Error, expected {expected_text} did not match {actual_text}'