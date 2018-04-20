import logging
from pages.homecred.header import Header
import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from pages.homecred.common.login.login_page import LoginPage


class MainPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver = driver
        self.header = Header(driver)
        self.url = url
        self.login_page = LoginPage(driver)


# Attributes
    title = "Банк Хоум Кредит |Товары в рассрочку | Вклады | Кредиты"


# Locators
    _market_widget_component = "//*[contains(@class, 'market-widget-component__widgetContainer___')]"

    def open_page(self):
        self.open(self.url)

    def visible_market_widget_component(self):
        self.element_wait_for(locator=self._market_widget_component, locator_type='xpath')

    def header_click_contact_link(self):
        self.header.click_contacts_link()

    def header_click_home_chat_link(self):
        self.header.click_home_chat_link()

    def display_home_chat(self):
        return self.header.display_home_chat()

    def header_click_close_home_chat(self):
        self.header.click_close_home_chat()

    def header_click_login_link(self):
        self.header.click_login_link()

    def validate_text_element(self,locator_type,locator, text):
        return text == self.element_get_text(locator_type=locator_type, locator=locator)