
from pages.homecred.market.main.main_page import MainPage
from pages.homecred.market.main.main_menu import MainMenu
from utilities.markstatus import MarkStatus

import pytest

import time


class TestRedirect:
    @pytest.fixture()
    def main_page(self, each_function_setup, setup_path):
        return MainPage(each_function_setup, setup_path)

    @pytest.fixture()
    def mark_status(self, each_function_setup):
        return MarkStatus(each_function_setup)

    @pytest.fixture ()
    def main_menu (self, each_function_setup, setup_path):
        return MainMenu(each_function_setup, setup_path)
    #
    @pytest.mark.run(order=1)
    def test_about_card (self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_installment_card()
        main_menu.click_about_card()
        time.sleep(5)
        main_menu.switch_window(1)
        result = main_menu.verify_about_card_page()
        mark_status.markFinal('test_about_card', result, 'Installment Card Redirect Test Verification')

    @pytest.mark.run(order=2)
    def test_partners(self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_installment_card()
        main_menu.click_partners()
        time.sleep(5)
        main_menu.switch_window(1)
        result = main_menu.verify_partners_page()
        mark_status.markFinal('test_redirect_partners', result, 'Installment Card Redirect Test Verification')


    @pytest.mark.run(order=3)
    def test_credit_cards(self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_cards()
        main_menu.click_credit_cards()
        time.sleep(5)
        main_menu.switch_window(1)
        time.sleep(10)
        result = main_menu.verify_credit_cards_page()
        mark_status.markFinal('test_credit_cards', result, 'Cards Redirect Test Verification')


    @pytest.mark.run(order=4)
    def test_debet_cards_rub(self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_cards()
        main_menu.click_debet_cards_rub()
        time.sleep(5)
        main_menu.switch_window(1)
        result = main_menu.verify_debet_cards_rub_page()
        mark_status.markFinal('test_debet_cards_rub', result, 'Cards Redirect Test Verification')

    @pytest.mark.run(order=5)
    def test_debet_cards_val(self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_cards()
        main_menu.click_debet_cards_val()
        time.sleep(5)
        main_menu.switch_window(1)
        time.sleep(10)
        result = main_menu.verify_debet_cards_val_page()
        mark_status.markFinal('test_debet_cards_val', result, 'Cards Redirect Test Verification')

    @pytest.mark.run(order=6)
    def test_cash_loan(self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_credits()
        main_menu.click_cash_loan()
        time.sleep(5)
        main_menu.switch_window(1)
        time.sleep(10)
        result = main_menu.verify_cash_loan_page()
        mark_status.markFinal('test_cash_loan', result, 'Credits Redirect Test Verification')

    @pytest.mark.run(order=7)
    def test_credit_for_goods(self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_credits()
        main_menu.click_credit_for_goods()
        time.sleep(5)
        main_menu.switch_window(1)
        time.sleep(10)
        result = main_menu.verify_credit_for_goods_page()
        mark_status.markFinal('test_credit_for_goods_loan', result, 'Credits Redirect Test Verification')

    @pytest.mark.run(order=8)
    def test_how_repay_loan(self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_credits()
        main_menu.click_how_repay_loan()
        # time.sleep(5)
        main_menu.switch_window(1)
        # time.sleep(10)
        result = main_menu.verify_how_repay_loan_page()
        mark_status.markFinal('test_how_repay_loan', result, 'Credits Redirect Test Verification')

    @pytest.mark.run(order=9)
    def test_deposits_rub(self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_savings()
        main_menu.click_deposits_rub()
        time.sleep(5)
        main_menu.switch_window(1)
        time.sleep(10)
        result = main_menu.verify_deposits_rub_page()
        mark_status.markFinal('test_deposits_rub', result, 'Savings Redirect Test Verification')


    @pytest.mark.run(order=10)
    def test_deposits_val(self, main_menu, mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_savings()
        main_menu.click_deposits_val()
        # time.sleep(5)
        main_menu.switch_window(1)
        # time.sleep(10)
        result = main_menu.verify_deposits_val_page()
        mark_status.markFinal('test_deposits_val', result, 'Savings Redirect Test Verification')


    @pytest.mark.run(order=11)
    def test_investment_account(self,main_menu,mark_status):
        main_menu.open_main_page()
        main_menu.confirm_region()
        main_menu.click_savings()
        main_menu.click_investment_account()
        main_menu.switch_window(1)
        result = main_menu.verify_investment_account_page()
        mark_status.markFinal('test_investment_account',result, 'Savings Redirect Test Verification')