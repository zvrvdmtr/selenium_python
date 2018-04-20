
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class Menu(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Menu
    _installment_card_link = "//*[contains(@data-reactid, '35')]"
    _cards_link = "//*[contains(@data-reactid, '36')]"
    _credits_link = "//*[contains(@data-reactid, '37')]"
    _savings_link = "//*[contains(@data-reactid, '38')]"
    _confirm_button = '//*[contains(text(),"Да")]'

    def click_confirm_button(self):
        self.element_click(self._confirm_button, locator_type='xpath')

    def click_installment_card_link(self):
        self.element_click(locator=self._installment_card_link, locator_type='xpath')

    def click_cards_link(self):
        self.element_click(locator=self._cards_link, locator_type='xpath')

    def click_credits_link(self):
        self.element_click(self._credits_link, locator_type='xpath')

    def click_savings_link(self):
        self.element_click(self._savings_link, locator_type='xpath')


    # Submenu

    _about_card_link = '//*[contains(@href, "https://www.homecredit.ru/wow/") or contains (text(), "О карте")]'
    _partners_link = '//*[contains(@href, "https://www.homecredit.ru/shopping/partners/")]'
    _credit_cards_link = '//*[contains(@href, "https://www.homecredit.ru/cards/credit")]'
    _debet_cards_rub_link = '//*[contains(@href, "https://www.homecredit.ru/cards/debet_rub")]'
    _debet_cards_val_link = '//*[contains(@href, "https://www.homecredit.ru/cards/debet_val")]'
    _cash_loan_link = '//*[contains(@href, "https://www.homecredit.ru/loans/index.php")]'
    _credit_for_goods_link = '//*[contains(@href, "https://www.homecredit.ru/loans/loans_pos.php")]'
    _how_repay_loan_link = '//*[contains(@href, "https://www.homecredit.ru/loans/loans_how.php")]'
    _deposits_rub_link = '//*[contains(@href, "https://www.homecredit.ru/deposits/rub")]'
    _deposits_val_link = '//*[contains(@href, "https://www.homecredit.ru/deposits/val")]'
    _investment_account_link = '//*[contains(@href, "https://www.homecredit.ru/deposits/iis")]'

    def click_about_card_link(self):
        self.element_click(self._about_card_link, locator_type='xpath')

    def click_partners_link(self):
        self.element_click(self._partners_link, locator_type='xpath')

    def click_credit_cards_link(self):
        self.element_click(self._credit_cards_link, locator_type='xpath')

    def click_debet_cards_rub_link(self):
        self.element_click(self._debet_cards_rub_link, locator_type='xpath')

    def click_debet_cards_val_link(self):
        self.element_click(self._debet_cards_val_link, locator_type='xpath')

    def click_cash_loan_link(self):
        self.element_click(self._cash_loan_link, locator_type='xpath')

    def click_credit_for_goods_link(self):
        self.element_click(self._credit_for_goods_link, locator_type='xpath')

    def click_how_repay_loan_link(self):
        self.element_click(self._how_repay_loan_link, locator_type='xpath')

    def click_deposits_rub_link(self):
        self.element_click(self._deposits_rub_link, locator_type='xpath')

    def click_deposits_val_link(self):
        self.element_click(self._deposits_val_link, locator_type='xpath')

    def click_investment_account_link(self):
        self.element_click(self._investment_account_link, locator_type='xpath')