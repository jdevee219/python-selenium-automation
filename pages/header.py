from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.XPATH, "//*[@data-test='@web/CartLink']")

    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart(self):
        self.click(*self.CART_ICON)
        # self.wait_for_element(*self.CART_ICON)
        # self.wait_for_element_click(*self.CART_ICON)

        # Stale El Ref Exception
        # element = self.driver.find_element(*self.CART_ICON)
        # print(element)
        # self.driver.refresh()
        # element = self.driver.find_element(*self.CART_ICON)
        # print(element)
        # element.click()