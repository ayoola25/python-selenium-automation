from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.logger import logger


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, *locator):
        logger.info(f'clicking on {locator}')
        self.driver.find_element(*locator).click()

    def open_page(self, page_address=''):
        self.driver.get(f'{self.base_url}{page_address}')

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, \
            f"Error! Actual text {actual_text} did not match Expected {expected_text}"

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'

    def open_page(self, end_url=''):
        logger.info(f'Opening {self.base_url}{end_url}...')
        self.driver.get(f'{self.base_url}{end_url}')