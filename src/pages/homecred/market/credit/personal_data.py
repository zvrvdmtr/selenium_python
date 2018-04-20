import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class PersonalData(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    # Locators
    _personal_data_form = '//*[contains(@class, "personal-data__personalData___")]//*[contains(@name, "setting")]'
    _lastName_field = "//*[@id='creditProcess.lastName']"
    _name_field = "//*[@id='creditProcess.name']"
    _patronymic_field = "//*[@id='creditProcess.patronymic']"
    _birthday_field = "//*[@id='creditProcess.birthday']"
    _phoneNumber_field = "//*[@id='phone']"
    _email_field = "//*[@id='email']"
    _seria_and_number_of_passport_field = "//*[@id='series']"
    _monthly_income_field = "//*[@id='money']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clear_lastName_field(self):
        self.element_clear(locator=self._lastName_field, locator_type='xpath')

    def set_lastName(self, text=''):
        self.element_send_keys(locator=self._lastName_field, locator_type='xpath', data=text)

    def check_lastName(self):
        lastName = self.element_attribute(locator=self._lastName_field, locator_type='xpath', attr_name='value')
        return lastName

    def clear_name_field(self):
        self.element_clear(locator=self._name_field, locator_type='xpath')

    def set_name(self, text=''):
        self.element_send_keys(locator=self._name_field, locator_type='xpath', data=text)

    def check_name(self):
        name = self.element_attribute(locator=self._name_field, locator_type='xpath', attr_name='value')
        return name

    def clear_patronymic_field(self):
        self.element_clear(locator=self._patronymic_field, locator_type='xpath')

    def set_patronymic(self, text=''):
        self.element_send_keys(locator=self._patronymic_field, locator_type='xpath', data=text)

    def check_patronymic(self):
        patronymic = self.element_attribute(locator=self._patronymic_field, locator_type='xpath', attr_name='value')
        return patronymic

    def clear_birthday_field(self):
        self.element_clear(locator=self._birthday_field, locator_type='xpath')

    def set_birthday(self, text=''):
        self.element_send_keys(locator=self._birthday_field, locator_type='xpath', data=text)

    def check_birthday(self):
        birthday = self.element_attribute(locator=self._birthday_field, locator_type='xpath', attr_name='value')
        return birthday

    def clear_email_field(self):
        self.element_clear(locator=self._email_field, locator_type='xpath')

    def set_email(self, text=''):
        self.element_send_keys(locator=self._email_field, locator_type='xpath', data=text)

    def check_email(self):
        email = self.element_attribute(locator=self._email_field, locator_type='xpath', attr_name='value')
        return email

    def clear_seria_and_number_of_passport(self):
        self.element_clear(locator=self._seria_and_number_of_passport_field, locator_type='xpath')

    def set_seria_and_number_of_passport(self, text=''):
        self.element_send_keys(locator=self._seria_and_number_of_passport_field, locator_type='xpath', data=text)

    def check_seria_and_number_of_passport(self):
        seria_and_number_of_passport = self.element_attribute(locator=self._seria_and_number_of_passport_field,
                                                              locator_type='xpath', attr_name='value')
        return seria_and_number_of_passport

    # Actions
    def clear_monthly_income(self):
        self.element_clear(locator=self._monthly_income_field, locator_type='xpath')

    def set_monthly_income(self, text=''):
        self.element_send_keys(locator=self._monthly_income_field, locator_type='xpath', data=text)

    def check_monthly_income(self):
        monthly_income = self.element_attribute(locator=self._monthly_income_field, locator_type='xpath',
                                                attr_name='value')
        return monthly_income

    def fill_personal_data_fields(self, lastName=None, name=None, patronymic=None, birthday=None,
                                  mobile=None, email=None, series=None, monthlyIncome=None):
        self.elements_send_keys(locator=self._personal_data_form,
                                lastName=lastName, name=name, patronymic=patronymic,
                                birthday=birthday, mobile=mobile, email=email,
                                series=series, monthlyIncome=monthlyIncome)

    def clear_personal_data_fields(self, lastName=None, name=None, patronymic=None, birthday=None,
                                   mobile=None, email=None, series=None, monthlyIncome=None):
        self.elements_clear(locator=self._personal_data_form,
                            lastName=lastName, name=name, patronymic=patronymic,
                            birthday=birthday, mobile=mobile, email=email,
                            series=series, monthlyIncome=monthlyIncome)