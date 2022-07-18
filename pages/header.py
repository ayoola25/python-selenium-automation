from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class Header(Page):
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    DEPARTMENT_SUB_NAV = (By.CSS_SELECTOR, "[data-category='books']")
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag-us')
    ICON_BTN = (By.XPATH, "//div[@id='nav-cart-count-container']//span[@class='nav-cart-icon nav-sprite']")
    ORDERS_LNK = (By.CSS_SELECTOR, "a[href*='/gp/css/order-history?ref_=nav_orders_first']")
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SPANISH_LANG = (By.CSS_SELECTOR, "[href ='#switch-lang=es_US']")

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def hover_lang(self):
        actions = ActionChains(self.driver)
        flag = self.find_element(*self.FLAG)
        actions.move_to_element(flag)
        actions.perform()

    def select_dept(self):
        department_select = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department_select)
        select.select_by_value('search-alias=stripbooks')

    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def verify_department(self):
        self.wait_for_element_appear(*self.DEPARTMENT_SUB_NAV)

    def click_on_cart_icon(self):
        self.click(*self.ICON_BTN)

    def click_orders_link(self):
        self.click(*self.ORDERS_LNK)

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

