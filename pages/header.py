from selenium.webdriver.common.by import By

from old_base_page import Page


class Header(Page):
    ICON_BTN = (By.XPATH, "//div[@id='nav-cart-count-container']//span[@class='nav-cart-icon nav-sprite']")
    ORDERS_LNK = (By.CSS_SELECTOR, "a[href*='/gp/css/order-history?ref_=nav_orders_first']")
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')

    def click_on_cart_icon(self):
        self.click(*self.ICON_BTN)

    def click_orders_link(self):
        self.click(*self.ORDERS_LNK)

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

