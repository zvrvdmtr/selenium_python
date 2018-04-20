from pages.intranet.Authorization.login_page import LoginPageIntra
from utilities.markstatus import MarkStatus
import pytest
import unittest
import time

@pytest.mark.usefixtures('each_function_setup')
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, each_function_setup):
        self.lp = LoginPageIntra(self.driver)
        self.ts = MarkStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        self.lp.login(login='ABondarenko')
        self.lp.password(password='Grn82MqpK!@#$%')
