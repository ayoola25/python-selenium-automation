from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    EMPTY_CART_TEXT = (By.XPATH, '//h2')

    def verify_amazonCart_empty(self):
        self.verify_text('Your Amazon Cart is empty', *self.EMPTY_CART_TEXT)
