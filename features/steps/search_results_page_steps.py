from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ADD_ITEM_BTN = (By.CSS_SELECTOR, "[id*='addToCartButtonOrText']")
SIDE_NAV_ADD_ITEM_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'][id*='addToCartButtonOrText']")
VIEW_CART_BTN = (By.CSS_SELECTOR, "[href='/cart']")
SEARCH_RESULTS = (By.XPATH, "//div[@data-test='lp-resultsCount']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

# Add Item to Cart
@when('Add item to cart')
def add_item(context):
    context.driver.find_element(*ADD_ITEM_BTN).click()
    sleep(5)

# Add Item to Cart from Side Panel
@when('Add item in side panel')
def add_item_side_panel(context):
    context.driver.find_element(*SIDE_NAV_ADD_ITEM_BTN).click()


# Store product name
@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name store: ', context.product_name)

# View Cart after adding item from search results
@when('View cart')
def view_cart(context):
    context.driver.find_element(*VIEW_CART_BTN).click()



# Search results
@then('Verify search worked for {product}')
def verify_search_results(context, product):
    # actual_text = context.driver.find_element(*SEARCH_RESULTS).text
    # assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"
    context.app.search_results_page.verify_search_results()
