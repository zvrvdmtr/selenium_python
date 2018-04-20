from base.selenium_driver import SeleniumDriver


class AdditionalInformation(SeleniumDriver):

    _additional_form = '//*[contains(@class, "additional-data__additionalData___")]//*[contains(@id, "setting")]'

    # Locators
    _visible_unvisibal_salary = "//*[contains(@class, 'input-monthly-income__eye___')]/img"
    _button_additional_data = "//*[contains(@class, 'additional-data__enterData___')][text()='Заполнить данные']"
    _pussport_data_field = "//*[@id='passportDate']"
    _pussport_code_field = "//*[@id='code']"
    _passport_issuedBy_field = "//*[@id='passportIssuedBy']"
    _birthplace_field = "//*[@id='birthplace']"
    _hide_additional_data = "//*[contains(@class, 'additional-data__arrowTop___')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_button_additional_data(self):
        self.element_click(locator=self._button_additional_data, locator_type='xpath')

    def clear_pussport_data_field(self):
        self.element_clear(locator=self._pussport_data_field, locator_type='xpath')

    def set__pussport_data(self, text=''):
        self.element_send_keys(locator=self._pussport_data_field, locator_type='xpath', data=text)

    def check_pussport_data(self):
        pussport_data = self.element_attribute(locator=self._pussport_data_field, locator_type='xpath', attr_name='value')
        return pussport_data

    def clear_pussport_code_field(self):
        self.element_clear(locator=self._pussport_code_field, locator_type='xpath')

    def set_pussport_code_field(self, text=''):
        self.element_send_keys(locator=self._pussport_code_field, locator_type='xpath', data=text)

    def check_pussport_code_field(self):
        pussport_code_field = self.element_attribute(locator=self._pussport_code_field, locator_type='xpath', attr_name='value')
        return pussport_code_field

    def clear_passport_issuedBy_field(self):
        self.element_clear(locator=self._passport_issuedBy_field, locator_type='xpath')

    def set_passport_issuedBy(self, text=''):
        self.element_send_keys(locator=self._passport_issuedBy_field, locator_type='xpath', data=text)

    def check_passport_issuedBy(self):
        passport_issuedBy = self.element_attribute(locator=self._passport_issuedBy_field, locator_type='xpath', attr_name='value')
        return passport_issuedBy

    def clear_birthplace_field(self):
        self.element_clear(locator=self._birthplace_field, locator_type='xpath')

    def set_birthplace_field(self, text=''):
        self.element_send_keys(locator=self._birthplace_field, locator_type='xpath', data=text)

    def check_birthplace_field(self):
        birthplace_field = self.element_attribute(locator=self._birthplace_field, locator_type='xpath', attr_name='value')
        return birthplace_field

    def fill_additional_fields_data(self, passportDate=None, code=None, passportIssuedBy=None, birthplace=None):
        self.elements_send_keys(locator=self._additional_form, passportDate=passportDate, code=code,
                                passportIssuedBy=passportIssuedBy, birthplace=birthplace)

    def clear_additional_fields_data(self, passportDate=None, code=None, passportIssuedBy=None, birthplace=None):
        self.elements_clear(locator=self._additional_form, passportDate=passportDate, code=code,
                            passportIssuedBy=passportIssuedBy, birthplace=birthplace)