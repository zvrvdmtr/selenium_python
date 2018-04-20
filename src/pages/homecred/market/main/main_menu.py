from base.selenium_driver import SeleniumDriver
from pages.homecred.menu import Menu

import logging
import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
import time

class MainMenu(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, url):
        super().__init__(driver)
        self.menu = Menu(driver)
        self.url = url

    def open_main_page(self):
        self.open(self.url)

    def click_installment_card(self):
        self.menu.click_installment_card_link()

    def click_cards(self):
        self.menu.click_cards_link()

    def click_credits(self):
        self.menu.click_credits_link()

    def click_savings(self):
        self.menu.click_savings_link()



    _expected_url_about_card = 'https://www.homecredit.ru/wow/'
    _expected_title_about_card = 'Онлайн-заявка на Карту рассрочки | Оформить в Банке Хоум Кредит'

    _expected_url_partners = 'https://www.homecredit.ru/shopping/partners/'
    _expected_title_partners = 'Партнёры Карты рассрочки - Хоум Кредит Банк'

    _expected_url_credit_cards = 'https://www.homecredit.ru/cards/credit'
    _expected_title_credit_cards = 'Кредитные карты - Хоум Кредит Банк'

    _expected_url_debet_rub = 'https://www.homecredit.ru/cards/debet_rub'
    _expected_title_debet_rub = 'Дебетовые карты в рублях - Хоум Кредит Банк'

    _expected_url_debet_val = 'https://www.homecredit.ru/cards/debet_val'
    _expected_title_debet_val = 'Дебетовые карты в валюте - Хоум Кредит Банк'

    _expected_url_cash_load = 'https://www.homecredit.ru/loans/index.php'
    _expected_title_cash_load = 'Кредит наличными в Москве в Банке Хоум Кредит'

    _expected_url_credit_for_goods = 'https://www.homecredit.ru/loans/loans_pos.php'
    _expected_title_credit_for_goods = 'ООО "Хоум Кредит энд Финанс Банк" | Потребительский кредит'

    _expected_url_how_repay_loan = 'https://www.homecredit.ru/loans/loans_how.php'
    _expected_title_how_repay_loan = 'Получить потребительский кредит наличными в банке без справок и поручителей'

    _expected_url_deposits_rub = 'https://www.homecredit.ru/deposits/rub'
    _expected_title_deposits_rub = 'Выгодные вклады в рублях. Высокие проценты по рублевым вкладам - Хоум Кредит Банк'

    _expected_url_deposits_val = 'https://www.homecredit.ru/deposits/val'
    _expected_title_deposits_val = 'Валютные вклады, вклады в иностранной валюте - Хоум Кредит Банк'

    _expected_url_investment_account = 'https://www.homecredit.ru/deposits/iis/'
    _expected_title_investment_account =  'Выгодные вклады в банках. Самые высокие проценты по вкладам'

    def confirm_region(self):
        self.menu.click_confirm_button()

    def click_about_card(self):
        self.menu.click_about_card_link()

    def click_partners(self):
        self.menu.click_partners_link()

    def click_credit_cards(self):
        self.menu.click_credit_cards_link()

    def click_debet_cards_rub(self):
        self.menu.click_debet_cards_rub_link()

    def click_debet_cards_val(self):
        self.menu.click_debet_cards_val_link()

    def click_cash_loan(self):
        self.menu.click_cash_loan_link()

    def click_credit_for_goods(self):
        self.menu.click_credit_for_goods_link()

    def click_how_repay_loan(self):
        self.menu.click_how_repay_loan_link()

    def click_deposits_rub(self):
        self.menu.click_deposits_rub_link()

    def click_deposits_val(self):
        self.menu.click_deposits_val_link()

    def click_investment_account(self):
        self.menu.click_investment_account_link()



    def verify_page(self, expected_url, expected_title):
        this_url = self.get_url()
        this_title = self.get_title()
        result = None
        if (this_url==expected_url) or (this_title==expected_title):
            result=this_url
        else:
            result is None
        return result

    def verify_about_card_page(self):
        result = self.verify_page(self._expected_url_about_card, self._expected_title_about_card)
        return result

    def verify_partners_page(self):
        result = self.verify_page(self._expected_url_partners, self._expected_title_partners)
        return result

    def verify_credit_cards_page(self):
        result = self.verify_page(self._expected_url_credit_cards, self._expected_title_credit_cards)
        return result

    def verify_debet_cards_rub_page(self):
        result = self.verify_page(self._expected_url_debet_rub, self._expected_title_debet_rub)
        return result

    def verify_debet_cards_val_page(self):
        result = self.verify_page(self._expected_url_debet_val, self._expected_title_debet_val)
        return result

    def verify_cash_loan_page(self):
        result = self.verify_page(self._expected_url_cash_load, self._expected_title_cash_load)
        return result

    def verify_credit_for_goods_page(self):
        result = self.verify_page(self._expected_url_credit_for_goods, self._expected_title_credit_for_goods)
        return result

    def verify_how_repay_loan_page(self):
        result = self.verify_page(self._expected_url_how_repay_loan, self._expected_title_how_repay_loan)
        return result

    def verify_deposits_rub_page(self):
        result = self.verify_page(self._expected_url_deposits_rub, self._expected_title_deposits_rub)
        return result

    def verify_deposits_val_page(self):
        result = self.verify_page(self._expected_url_deposits_val, self._expected_title_deposits_val)
        return result

    def verify_investment_account_page(self):
        result = self.verify_page(self._expected_url_investment_account, self._expected_title_investment_account)
        return result