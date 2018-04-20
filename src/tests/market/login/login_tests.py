"""
Класс тестов для страницы логина
"""

import pytest

from pages.homecred.common.login.login_page import LoginPage
from pages.homecred.market.main.main_page import MainPage
from testrail_api.runs import add_run
from utilities.markstatus import MarkStatus


@pytest.fixture(scope='class')
def new_run():
    return add_run()


class TestLogin:

    @pytest.fixture()
    def main_page(self, each_function_setup, setup_path):
        return MainPage(each_function_setup, setup_path)

    @pytest.fixture()
    def login_page(self, each_function_setup):
        return LoginPage(each_function_setup)

    @pytest.fixture()
    def mark_status(self, each_function_setup):
        return MarkStatus(each_function_setup)

    @pytest.mark.parametrize('case_id', [1120])
    @pytest.mark.run(order=1)
    def test_valid_login(self, main_page, login_page, mark_status, case_id, new_run, test_data):
        mark_status.get_step(case_id=case_id, new_run=new_run)
        main_page.open_login_page()
        login_page.login_on_marketplace(phone=test_data[0]['phone'], birthday=test_data[0]['birthday'])
        login_page.login_sms(sms=test_data[0]['sms'])
        result = login_page.verify_login_successful()
        mark_status.mark(result, 'Try to validate apple and android')
        mark_status.mark(result, 'Second actual content')
        mark_status.mark(result, 'Third actual content')
        mark_status.markFinal('test_valid_login', result, 'Login Test Verification')

    @pytest.mark.parametrize('case_id', [1129])
    @pytest.mark.run(order=2)
    def test_mandatory_birthday(self,main_page, login_page, mark_status, case_id, new_run, test_data):
        mark_status.get_step(case_id=case_id, new_run=new_run)
        main_page.open_login_page()
        login_page.login_on_marketplace(phone=test_data[0]['phone'])
        result = login_page.verify_mandatory_fields_error()
        mark_status.markFinal('test_mandatory_birthday', result, 'Login Verification')

    def test_invalid_birthday(self, main_page, login_page, mark_status, test_data):
        main_page.open_login_page()
        login_page.login_on_marketplace(phone=test_data[0]['phone'], birthday='15.12.199')
        result = login_page.verify_mandatory_fields_error()
        mark_status.markFinal('test_mandatory_birthday', result, 'Login Verification')

    def test_invalid_birthday1(self, main_page, login_page, mark_status, test_data):
        main_page.open_login_page()
        login_page.login_on_marketplace(phone=test_data[0]['phone'], birthday='15.12.1996')
        result = login_page.verify_login_failed()
        mark_status.markFinal('test_invalid_birthday1', result, 'Login Verification')

    def test_mandatory_phone(self, main_page, login_page, mark_status, test_data):
        main_page.open_login_page()
        login_page.login_on_marketplace(birthday=test_data[0]['birthday'])
        result = login_page.verify_mandatory_fields_error()
        mark_status.markFinal('test_mandatory_phone', result, 'Login Verification')

    def test_invalid_phone1(self, main_page, login_page, mark_status, test_data):
        main_page.open_login_page()
        login_page.login_on_marketplace(phone='1114797581', birthday=test_data[0]['birthday'])
        result = login_page.verify_mandatory_fields_error()
        mark_status.markFinal('test_mandatory_phone', result, 'Login Verification')

    def test_invalid_phone2(self, main_page, login_page, mark_status, test_data):
        main_page.open_login_page()
        login_page.login_on_marketplace(phone='919479758', birthday=test_data[0]['birthday'])
        result = login_page.verify_mandatory_fields_error()
        mark_status.markFinal('test_mandatory_phone', result, 'Login Verification')

    def test_mandatory_fields(self, main_page, login_page, mark_status):
        main_page.open_login_page()
        login_page.login_on_marketplace()
        result = login_page.verify_mandatory_fields_error()
        mark_status.markFinal('test_mandatory_phone', result, 'Login Verification')

    def test_mandatory_sms(self, main_page, login_page, mark_status, test_data):
        main_page.open_login_page()
        login_page.login_on_marketplace(phone=test_data[0]['phone'], birthday=test_data[0]['birthday'])
        login_page.login_sms()
        result = login_page.verify_mandatory_fields_error()
        mark_status.markFinal('test_mandatory_phone', result, 'Login Verification')

    def test_invalid_sms(self, main_page, login_page, mark_status, test_data):
        main_page.open_login_page()
        login_page.login_on_marketplace(phone=test_data[0]['phone'], birthday=test_data[0]['birthday'])
        login_page.login_sms(sms='1235')
        result = login_page.verify_mandatory_fields_error()
        mark_status.markFinal('test_mandatory_phone', result, 'Login Verification')
