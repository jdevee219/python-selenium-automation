from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    CART_MESSAGE = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_cart_message(self):
        actual_text = self.driver.find_element(*self.CART_MESSAGE).text
        assert actual_text.text == 'Your cart is empty'