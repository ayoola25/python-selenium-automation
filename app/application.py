from selenium import webdriver
from pages.article_page import ArticlePage
from pages.base_page import Page
from pages.bestsellers_page import BestsellersPage
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.no_search_results_page import NoSearchResults
from pages.right_navigation import RightNavigation
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.article_page = ArticlePage(self.driver)
        self.bestsellers_page = BestsellersPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.no_search_results_page = NoSearchResults(self.driver)
        self.page = Page(self.driver)
        self.right_navigation = RightNavigation(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.signin_page = SignInPage(self.driver)

    def quit(self):
        self.driver.quit()

    def implicitly_wait(self, time):
        self.driver.implicitly_wait(time)

    def get_product_links(self, amount):
        self.store_page.open()
        product_urls = self.store_page.find_product_urls(amount)
        return product_urls

    def add_product_to_cart(self, url):
        self.product_page.open(url)
        items = self.product_page.items_count()
        self.product_page.select()
        self.product_page.add_to_cart()
        self.product_page.wait_prod_added(items + 1)

    def remove_from_cart(self):
        self.checkout_page.open()
        total = self.checkout_page.get_total()
        prod_price = self.checkout_page.get_prod_price()
        self.checkout_page.remove_from_cart()
        self.checkout_page.check_if_correct_price(prod_price, total)