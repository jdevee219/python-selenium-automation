from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_MESSAGE = (By.XPATH, "//h1[text()='Your cart is empty']")
CART_ITEM = (By.ID, "item-title-c9e389b1-43fb-11f0-9035-c92b32874ab7")

# Cart is empty
@then('Verify "Your cart is empty" message is shown')
def verify_cart_message(context):
    actual_text = context.driver.find_element(*CART_MESSAGE)
    assert actual_text.text == 'Your cart is empty'

# Item in cart
@then('Verify item has been added to cart')
def verify_item_added(context):
    expected_item = 'LEGO Star Wars Millennium Falcon 25th Anniversary Buildable Starship Model 75375'
    actual_item = context.driver.find_element(*CART_ITEM)
    assert expected_item == actual_item, f'Error, expected {expected_item} did not match {actual_item}'
