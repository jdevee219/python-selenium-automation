from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")
CART_ITEM = (By.ID, "item-title-c9e389b1-43fb-11f0-9035-c92b32874ab7")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')

# Cart is empty
@then('Verify "Your cart is empty" message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

# Correct item in cart
@then('Verify cart has correct product')
def verify_product_name(context):
    product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    print('Name in cart ', product_name_in_cart)
    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'

@then('Verify Cart page opened')
def verify_page_open(context):
    context.app.cart_page.verify_cart_opened()