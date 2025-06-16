from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Add Item to Cart
@when('Add item to cart')
def add_item(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButtonOrText']").click()
    sleep(5)

# Add Item to Cart from Side Panel
@when('Add item in side panel')
def add_item_side_panel(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'][id*='addToCartButtonOrText']").click()
    sleep(5)


# View Cart after adding item from search results
@when('View cart')
def view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()
    sleep(5)


# Search results
@then('Verify search worked for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"

