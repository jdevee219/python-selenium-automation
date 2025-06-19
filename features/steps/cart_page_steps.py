from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_MESSAGE = (By.XPATH, "//h1[text()='Your cart is empty']")
CART_ITEM = (By.ID, "item-title-c9e389b1-43fb-11f0-9035-c92b32874ab7")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

# Cart is empty
@then('Verify "Your cart is empty" message is shown')
def verify_cart_message(context):
    context.app.cart_page.verify_cart_message()

# Item in cart
@then('Verify item has been added to cart')
def verify_item_added(context):
    expected_item = 'LEGO Star Wars Millennium Falcon 25th Anniversary Buildable Starship Model 75375'
    actual_item = context.driver.find_element(*CART_ITEM)
    assert expected_item == actual_item, f'Error, expected {expected_item} did not match {actual_item}'

# Correct item in cart
@then('Verify cart has correct product')
def verify_product_name(context):
    product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    print('Name in cart ', product_name_in_cart)
    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'