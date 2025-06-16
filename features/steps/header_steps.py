from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.XPATH, "//*[@data-test='@web/CartLink']")
ACCOUNT_SIGN_IN = (By.ID, "account-sign-in")
SIGN_IN_BTN = (By.XPATH, "//button[@type='button' and text()='Sign in or create account']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")


# Product search
@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click(SEARCH_BTN)
    sleep(5)

# Going into the Cart
@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)

# Sign In
@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(*ACCOUNT_SIGN_IN).click()
    sleep(5)
    context.driver.find_element(SIGN_IN_BTN).click()
    sleep(5)


# Number of links
@then('Verify header has {number} links')
def verify_header_links(context, number):
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'