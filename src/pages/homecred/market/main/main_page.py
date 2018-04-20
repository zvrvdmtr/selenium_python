from base.selenium_driver import SeleniumDriver
from pages.homecred.header import Header
from pages.homecred.common.login.login_page import LoginPage


class MainPage(SeleniumDriver):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.header = Header(driver)
        self.login_page = LoginPage(driver)
        self.url = url

    def open_main_page(self):
        self.open(self.url)

    def click_login(self):
        self.header.click_login_link()

    def open_login_page(self):
        self.open_main_page()
        self.click_login()
