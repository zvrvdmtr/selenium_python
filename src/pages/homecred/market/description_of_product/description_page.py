import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class DescriptionPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    # Locators
    _main_button_order = "//*[contains(@class, 'best-offers__button___')]"
    _title = "//*[contains(@class, 'product-title-block__title___')]"
    _button_all_offers = "//*[contains(@class, 'offer-item-btn__deskButton___')]"
    _button_favorite = "//*[contains(@class, 'favorite-button__largeBtn___')]"

    # installment_plan
    _list_of_installment_plan = "//*[contains(@class, 'best-offers__dropDown___')]"
    _second_instalment_plan = "//*[contains(@class, 'best-offers__listItemClassName___')/div/div[1]/div[2]]"
    _third_instalment_plan = "//*[contains(@class, 'best-offers__listItemClassName___')]/div/div[1]/div[3]"

    # complain_on_price
    _button_complain_on_price = "//*[contains(@class, 'compile-price-content__link___')]"
    _complain_on_price = "//*[contains(@class, 'compile-price-content__link___')]"
    _button_close_on_complain_window = "//*[contains(@class, 'compile-price-content__link___')]"
    _set_email_or_fhonenumber_in_complain_on_price = "//*[contains(@class, 'unauthorized-modal__input-mixin___')]"
    _button_submit_in_complain_on_price = "//*[contains(@class, 'unauthorized-modal__input-mixin___')]"
    _button_back_to_calatog = "//*[contains(@class, 'product-not-avaible__backToCatalog___')][text()='Вернуться в каталог']"

    # Attributes
    _url_delivery = '/item/yamaha-c40'
    _url_pickup = '/item/astralux-starlet-i'

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver = driver
        self.url = url

    def open_page_delivery(self, path=_url_delivery):
        self.open(self.url, path)

    def open_page_pickup(self, path=_url_pickup):
        self.open(self.url, path)

    def click_button_best_order(self):
        self.element_click(locator=self._button_all_offers, locator_type='xpath')

    # Actions
    def fill_fields(self):
        pass






