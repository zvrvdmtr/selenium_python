import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class DeliveryPickup(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    _delivery_form = '//*[contains(@class, "delivery__inputsWrapper___")]//*[contains(@id, "setting")]'

    # Delivery or Pickup
    _Pickup = "//*[contains(@class, 'radio-btn__label___')]/span[text()='Самовывоз']"  # RadioButton
    _Delivery = "//*[contains(@class, 'radio-btn__label___')]/span[text()='Курьер']"  # RadioButton

    # Destination for Delivery
    _city_field = "//*[@id='city']"
    _validate_city_field = "//div[1]/div[1]/div/div[text()='Это поле обязательное']"
    _validate_street_field = "//div[2]/div[1]/div/div[text()='Это поле обязательное']"
    _street_field = "//*[@id='creditProcess.street']"
    _house_field = "//*[@id='house']"
    _apartment_field = "//*[@id='apartment']"
    _validate_house_field = "//div[2]/div[1]/div/div/div[text()='Это поле обязательное']"

    _list_delivery = "//*[contains(@class, 'delivery__radioWrap___')]"
    _delivery_options = "//*[contains(@name, 'deliveryOption')]"  # RadioButton

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_street(self, text=''):
        self.element_send_keys(self._street_field, locator_type='xpath', data=text)

    def check_street(self):
        street = self.element_attribute(locator=self._street_field, locator_type='xpath', attr_name='value')
        return street

    def set_house(self, text=''):
        self.element_send_keys(locator=self._house_field, locator_type='xpath', data=text)

    def check_house(self):
        house = self.element_attribute(locator=self._house_field, locator_type='xpath', attr_name='value')
        return house

    def fill_pickup_fields_data(self, city=None, street=None, house=None, apartment=None):
        self.elements_send_keys(locator=self._delivery_form, city=city, street=street, house=house, apartment=apartment)

    def clear_pickup_fields_data(self, city=None, street=None, house=None, apartment=None):
        self.elements_clear(locator=self._delivery_form, city=city, street=street, house=house, apartment=apartment)
