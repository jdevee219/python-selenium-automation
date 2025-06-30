from selenium.webdriver.common.by import By

from pages.base_page import Page

class TargetSignInPage(Page):
    TC_LINK = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions']")


    def open_target_sign_in(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_terms_link(self):
        self.click(*self.TC_LINK)