from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.XPATH, "//*[@data-test='@web/CartLink']")
ACCOUNT_SIGN_IN = (By.ID, "account-sign-in")
SIGN_IN_BTN = (By.XPATH, "//button[@type='button' and text()='Sign in or create account']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

# Product search
@when('Search for {search_word}')
def search_product(context, search_word):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    # sleep(10)
    context.app.header.search_product(search_word)

# Going into the Cart
@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


# Sign In
@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(*ACCOUNT_SIGN_IN).click()

@when('From right side navigation menu, click Sign In')
def side_nav_click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BTN).click()



# Number of links
@then('Verify header has {number} links')
def verify_header_links(context, number):
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'


# Verify titles and images
@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    #context.driver.execute_script("window.scrollBy(0,2000)", "")
    #sleep(2)
    # context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    # If you ever need to scroll up, use negative numbers: context.driver.execute_script("window.scrollBy(0, -2000)", ""
    products = context.driver.find_elements(*LISTINGS)[:8]

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)