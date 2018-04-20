"""
Класс реализующий локаторы и пользовательские действия работы со страницей логина
"""
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    # Locators
    _phone_field = 'authorization.mobilephone'
    _birthday_field = 'authorization.birthday'
    _next_button = '//*[contains(@class, "authorization__buttonWrp___")]'
    _sms_field = 'authorization.sms'
    _confirm_button = "//*[contains(@class, 'authorizaton-step__button___')]"
    _bank_stuff = '//div[@class="main-menu__item___xIkPT"][2]'
    _user_not_found = '//*[contains(@class, "authorization__userNotFound___")]'
    _close_button_popup = "//*[contains(@class, 'authorization__close___')]"
    _title_popup = "//*[contains(@class, 'choose__caption___')]"

    # Links
    _my_credit_link = "//*[contains(@class, 'choose__mycredit___')]"
    _goods_link = '//*[contains(@class, "choose__marketplace___")]'
    _polza_link = "//*[contains(@class, 'choose__polza___')]"
    _internet_bank_link = "//*[contains(@class, 'choose__bank___')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_goods_link(self):
        self.element_click(self._goods_link, locator_type='xpath')

    def enter_phone(self, phone):
        self.element_send_keys(self._phone_field, locator_type='id', data=phone)

    def enter_birthday(self, birthday):
        self.element_send_keys(self._birthday_field, locator_type='id', data=birthday)

    def click_next_button(self):
        self.element_click(self._next_button, locator_type='xpath')

    def enter_sms(self, sms):
        self.element_send_keys(self._sms_field, locator_type='id', data=sms)

    def click_confirm_button(self):
        self.element_click(self._confirm_button, locator_type='xpath')

    def clear_field(self):
        self.element_get(self._phone_field).clear()
        self.element_get(self._birthday_field).clear()

    def login_on_marketplace(self, phone='', birthday=''):
        self.click_goods_link()
        self.enter_phone(phone)
        self.enter_birthday(birthday)
        self.click_next_button()

    def login_sms(self, sms=''):
        self.element_wait_for(self._sms_field, locator_type='id', timeout=60)
        self.enter_sms(sms)
        self.click_confirm_button()

    def verify_login_successful(self):
        result = self.element_is_present('//*[contains(@class, "personal-account-link__avatar___")]', locator_type='xpath')
        return result

    def verify_mandatory_fields_error(self):
        result = self.element_presence_check('//*[contains(@class, "error__error___")]', locator_type='xpath')
        return result

    def verify_login_failed(self):
        result = self.element_get(self._user_not_found, locator_type='xpath')
        return result

    def verify_text(self, element):
        result = self.element_get_text(element=element)
        return result

    def validate_text_credit_link(self, text):
        return text == self.element_get_text(locator=self._my_credit_link, locator_type='xpath')

    def validate_text_goods_link(self, text):
        return text == self.element_get_text(locator=self._goods_link, locator_type='xpath')

    def validate_text_polza_link(self, text):
        return text == self.element_get_text(locator=self._polza_link, locator_type='xpath')

    def validate_text_internet_bank_link(self, text):
        return text == self.element_get_text(locator=self._internet_bank_link, locator_type='xpath')

    def validate_text_title(self, text):
        return text == self.element_get_text(locator=self._title_popup, locator_type='xpath')