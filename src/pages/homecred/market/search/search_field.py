import logging

import utilities.custom_logger as cl
from pages.homecred.header import BasePage


class SearchField(BasePage):

    log = cl.customLogger(logging.DEBUG)

    # Locators
    _path = ''
    _highlight_product = "//*[contains(@class, 'search-suggest__searchSuggest___')]//*[contains(@class, 'search-suggest-item-name__highlightString___')][text()]"
    _title_of_product = "//*[contains(@class, 'product-title-block__title___')][text()]"
    _all_search_results = "//*[contains(@class, 'search-suggest-btn__suggestBtn___')]"
    _clear_search_field = "//*[contains(@class, 'search-close-icon__activeCloseIcon___')]"
    _products_not_found = "//*[contains(@class, 'search-suggest__headerText___')][text() = 'По вашему запросу товаров не найдено.']"

    def __init__(self, driver, url):
        super().__init__(driver, url, self._path)
        self.driver = driver
        self.basePage = BasePage(driver, url, self._path)

    # Actions

    def search_string(self, text):
        self.basePage.open_page(self._path)
        self.basePage.click_search_field()
        self.basePage.enter_data_search(text=text)

    def visible_find_area(self):
        self.element_visibility_wait_for(locator=self._highlight_product, locator_type='xpath')
        self.element_is_clickable(locator=self._highlight_product, locator_type='xpath')

    def click_on_product(self):
        self.element_click(self._highlight_product, locator_type='xpath')

    def check_name_of_product(self):
        x = self.get_text(locator=self._title_of_product, locator_type='xpath')
        return x

