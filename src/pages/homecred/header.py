"""
Класс реализвующий базовые методы для работы со всеми страница маркета и банка
"""
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class Header(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.url = url

    # Locators
    _logo_link = 'logo__logoImg___1QVe6'
    _contacts_link = 'header__contacts___1Xi10'
    _login_link = "//*[contains(@class, 'authorization__signin___')]"
    _search_field = "//*[contains(@class, 'search-input__input___')]"
    _home_chat = "webim_chat"
    _home_chat_close_button = "webim-action-close"
    _home_chat_link = "//*[contains(@class, 'home-chat__link___')]"

    def return_url(self):
        result = self.get_url()
        return result

    def return_title(self):
        result = self.get_title()
        return result

    def get_logo(self):
        result = self.element_get(locator=self._logo_link, locator_type='class')
        return result

    def click_logo(self):
        self.element_click(locator=self._logo_link, locator_type='class')

    def click_contacts_link(self):
        self.element_click(locator=self._contacts_link, locator_type='class')

    def click_login_link(self):
        self.element_click(self._login_link, locator_type='xpath')

    def click_search_field(self):
        self.element_click(self._search_field, locator_type='xpath')

    def enter_data_search(self, text=''):
        self.element_send_keys(self._search_field, locator_type='xpath', data=text)

    def click_home_chat_link(self):
        self.element_click(self._home_chat_link, locator_type='xpath')

    def click_close_home_chat(self):
        self.element_visibility_wait_for(locator=self._home_chat, locator_type='id')
        self.element_click(self._home_chat_close_button, locator_type='class')

    def display_home_chat(self):
        time.sleep(0.5)
        present = self.element_is_displayed(locator=self._home_chat, locator_type='id')
        return present