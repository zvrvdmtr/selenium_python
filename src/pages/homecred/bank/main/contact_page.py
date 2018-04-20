import logging

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from pages.homecred.header import Header


class ContactPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver = driver
        self.url = url
        self.header = Header(driver)

# Attributes
    path = "contacts"
    title = "Контакты - Хоум Кредит Банк"

# Locators
    _map = "//*[contains(@class, 'central-office-map__mapElement___')]"

    def open_page(self, path=path):
        self.open(self.url, path)

    def visible_map(self):
        self.element_visibility_wait_for(locator=self._map, locator_type='xpath')

    def header_click_logo(self):
        self.header.click_logo()
