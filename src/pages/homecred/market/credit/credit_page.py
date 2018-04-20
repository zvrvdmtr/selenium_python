import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
from pages.homecred.market.credit.personal_data import PersonalData
from pages.homecred.market.credit.delivery_pickup_page import DeliveryPickup
from pages.homecred.market.credit.additional_page import AdditionalInformation


class CreditPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    # Locators
    _title_ordering_options = "//*[contains(@class, 'credit-process-component__title___')]"
    _button_order = "//*[contains(@class, 'total__send___')]"
    _order_sms = "//*[@id='creditProcess.smsCode']"
    _resent_order_sms = "//*[contains(@class, 'total__link___')]"

    # Login
    _cookie_link = "//*[contains(@class, 'cookie-link__cookieLink___')]"
    _open_cookie_page = "//*[contains(@class, 'cookie-link__cookieLink___')]"

    # Личный кабинет
    _personal_area = "//*[contains(@class, 'orders__caption___')][text()='История заказов']"

    # Destination for Pickup
    _list_pickup = "//*[contains(@class, 'delivery-list__list___')]"
    _open_pickup_location_point = "//*[contains(@class, 'delivery-item__itemWrp___')]"
    _select_pickup = "//*[contains(@class, 'button__small___')][text()='Выбрать']"
    _button_back_in_pickup = "//*[contains(@class, 'selected-outpost__back___')]/span[text()='Назад']"
    _choose_other_pickup = "//*[contains(@class, 'selected-outpost__linkWrapper___')][text()='Выбрать другой пункт']"

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver = driver
        self.url = url
        self.personal_data = PersonalData(driver)
        self.delivery_pickup = DeliveryPickup(driver)
        self.additional_information = AdditionalInformation(driver)

    # Actions
    def verify_login_successful(self):
        result = self.element_is_present('//*[contains(@class, "personal-account-link__avatar___")]', locator_type='xpath')
        return result

    def click_button_order(self):
        self.element_click(locator=self._button_order, locator_type='xpath')

    def set_order_sms(self, text=''):
        self.element_send_keys(locator=self._order_sms, locator_type='xpath', data=text)

    def check_order_sms(self):
        order_sms = self.element_attribute(locator=self._order_sms, locator_type='xpath', attr_name='value')
        return order_sms

    def fill_pickup_data(self, city=None, street=None, house=None, apartment=None):
        self.delivery_pickup.fill_pickup_fields_data(city=city, street=street, house=house, apartment=apartment)

    def clear_pickup_data(self, city=None, street=None, house=None, apartment=None):
        self.delivery_pickup.clear_pickup_fields_data(city=city, street=street, house=house, apartment=apartment)

    def fill_personal_data(self, lastName=None, name=None, patronymic=None,
                           birthday=None, mobile=None, email=None, series=None, monthlyIncome=None):
        self.personal_data.fill_personal_data_fields(lastName=lastName, name=name,
                                                     patronymic=patronymic, birthday=birthday, mobile=mobile,
                                                     email=email, series=series, monthlyIncome=monthlyIncome)

    def clear_personal_data(self, lastName=None, name=None, patronymic=None,
                            birthday=None, mobile=None, email=None, series=None, monthlyIncome=None):
        self.personal_data.clear_personal_data_fields(lastName=lastName, name=name,
                                                      patronymic=patronymic, birthday=birthday, mobile=mobile,
                                                      email=email, series=series, monthlyIncome=monthlyIncome)

    def open_additional_fields(self):
        self.additional_information.click_button_additional_data()

    def fill_additional_data(self, passportDate=None, code=None, passportIssuedBy=None, birthplace=None):
        self.additional_information.fill_additional_fields_data(passportDate=passportDate, code=code,
                                                                passportIssuedBy=passportIssuedBy, birthplace=birthplace)

    def clear_additional_data(self, passportDate=None, code=None, passportIssuedBy=None, birthplace=None):
        self.additional_information.clear_additional_fields_data(passportDate=passportDate, code=code,
                                                                 passportIssuedBy=passportIssuedBy, birthplace=birthplace)

    def click_first_pickup(self):
        self.element_click(locator=self._open_pickup_location_point, locator_type='xpath')

    def click_button_select(self):
        self.element_click(locator=self._select_pickup, locator_type='xpath')
