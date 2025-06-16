from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Product search
@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(By.ID, 'search').send_keys(search_word)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

# Going into the Cart
@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartLink']").click()
    sleep(5)

# Sign In
@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    sleep(5)
    context.driver.find_element(By.XPATH, "//button[@type='button' and text()='Sign in or create account']").click()
    sleep(5)




# Number of links
@then('Verify header has {number} links')
def verify_header_links(context, number):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print(links)
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'