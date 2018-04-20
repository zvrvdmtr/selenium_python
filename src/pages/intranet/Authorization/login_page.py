from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class LoginPageIntra(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _LoginField = 'username'
    _PasswordField = 'password'
    _LoginButton = 'page-form--submit'
    # _Menu = 'Avatar-kMBfmL'
    _SettingsMenu = '//header/div[2]/div'
    _LogOut = "//*[text()='Выйти']"

    def click_LoginField (self, login=''):
        self.sendKeys(self._LoginField, locator_type='name', data=login)

    def click_PasswordField (self, password=''):
        self.sendKeys(self._PasswordField, locator_type='name', data=password)

    def click_LoginButton (self):
        self.elementClick(self._LoginButton, locator_type='class')

    def _SettingsMenu (self):
        self.elementClick(self._SettingsMenu, locator_type='xpath')

    def click_LogOut (self):
        self.elementClick(self._LogOut, locator_type='xpath')



#Action
    def login(self, login):
        self.click_LoginField(login=login)

    def password(self, password):
        self.click_PasswordField(password=password)
        self.click_LoginButton()
        self.click_SettingsMenu()
        self.click_LogOut()




