from pages.homecred.market.description_of_product.description_page import DescriptionPage
from pages.homecred.market.main.main_page import MainPage
from pages.homecred.market.credit.credit_page import CreditPage
from pages.homecred.common.login.login_page import LoginPage
from utilities.markstatus import MarkStatus
import pytest


class TestDescription:

    @pytest.fixture()
    def description(self, each_function_setup, setup_path):
        return DescriptionPage(each_function_setup, setup_path)

    @pytest.fixture()
    def credit_page(self, each_function_setup, setup_path):
        return CreditPage(each_function_setup, setup_path)

    @pytest.fixture()
    def mark_status(self, each_function_setup):
        return MarkStatus(each_function_setup)

    @pytest.fixture()
    def login_page(self, each_function_setup):
        return LoginPage(each_function_setup)

    @pytest.fixture()
    def main_page(self, each_function_setup, setup_path):
        return MainPage(each_function_setup, setup_path)

    @pytest.mark.run(order=1)
    def test_buy_delivery_partner(self, description, credit_page, test_data, main_page, login_page):
        description.open_page_delivery()
        description.click_button_best_order()
        main_page.click_login()
        login_page.login_on_marketplace(phone=test_data[0]['phone'], birthday=test_data[0]['birthday'])
        login_page.login_sms(sms=test_data[0]['sms'])
        credit_page.fill_pickup_data(street=test_data[0]['street'], house=test_data[0]['house'])
        credit_page.clear_personal_data(lastName=True, name=True, patronymic=True, email=True, series=True,
                                        monthlyIncome=True)
        credit_page.fill_personal_data(lastName=test_data[0]['lastName'], name=test_data[0]['name'],
                                       monthlyIncome=test_data[0]['monthly_income'],
                                       patronymic=test_data[0]['patronymic'], email=test_data[0]['email'],
                                       series=test_data[0]['seria_and_number_of_passport'])
        credit_page.open_additional_fields()
        credit_page.clear_additional_data(passportDate=True, code=True, passportIssuedBy=True, birthplace=True)
        credit_page.fill_additional_data(passportDate=test_data[0]['passport_data'],
                                         code=test_data[0]['passport_code_field'],
                                         passportIssuedBy=test_data[0]['passport_issuedBy'],
                                         birthplace=test_data[0]['birthplace_field'])
        credit_page.click_button_order()
        credit_page.set_order_sms(text=test_data[0]['sms'])
        credit_page.click_button_order()

    @pytest.mark.run(order=2)
    def test_buy_pickup_partner(self, description, credit_page, test_data, main_page, login_page):
        description.open_page_pickup()
        description.click_button_best_order()
        credit_page.click_first_pickup()
        credit_page.click_button_select()
        main_page.click_login()
        login_page.login_on_marketplace(phone=test_data[0]['phone'], birthday=test_data[0]['birthday'])
        login_page.login_sms(sms=test_data[0]['sms'])
        credit_page.clear_personal_data(lastName=True, name=True, patronymic=True, email=True, series=True,
                                        monthlyIncome=True)
        credit_page.fill_personal_data(lastName=test_data[0]['lastName'], name=test_data[0]['name'],
                                       monthlyIncome=test_data[0]['monthly_income'],
                                       patronymic=test_data[0]['patronymic'], email=test_data[0]['email'],
                                       series=test_data[0]['seria_and_number_of_passport'])
        credit_page.open_additional_fields()
        credit_page.clear_additional_data(passportDate=True, code=True, passportIssuedBy=True, birthplace=True)
        credit_page.fill_additional_data(passportDate=test_data[0]['passport_data'],
                                         code=test_data[0]['passport_code_field'],
                                         passportIssuedBy=test_data[0]['passport_issuedBy'],
                                         birthplace=test_data[0]['birthplace_field'])
        credit_page.click_button_order()
        credit_page.set_order_sms(text=test_data[0]['sms'])
        credit_page.click_button_order()
