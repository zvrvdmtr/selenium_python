import pytest
from configfiles.project_setting import *
from pages.homecred.bank.main.contact_page import ContactPage
from pages.homecred.bank.main.main_page import MainPage
from pages.homecred.header import Header
from utilities.markstatus import MarkStatus
from pages.homecred.common.login.login_page import LoginPage


class TestHeader:
    @pytest.fixture()
    def main_page(self, each_function_setup, setup_path):
        return MainPage(each_function_setup, setup_path)

    @pytest.fixture()
    def contact_page(self, each_function_setup, setup_path):
        return ContactPage(each_function_setup, setup_path)

    @pytest.fixture()
    def mark_status(self, each_function_setup):
        return MarkStatus(each_function_setup)

    @pytest.mark.run(order=1)
    def test_go_to_contact_page(self, main_page, contact_page, mark_status):
        main_page.open_page()
        main_page.header_click_contact_link()
        contact_page.visible_map()
        mark_status.mark(contact_page.get_title() == contact_page.title, "Title is correct")
        mark_status.markFinal("test_go_to_contact_page", bank['url'] + contact_page.path == contact_page.get_url(),
                              "URL is correct")

    @pytest.mark.run(order=1)
    def test_go_to_main_page_on_the_logo(self, main_page, contact_page, mark_status):
        contact_page.open_page()
        contact_page.header_click_logo()
        main_page.visible_market_widget_component()
        mark_status.mark(main_page.get_title() == main_page.title, "Title is correct")
        mark_status.markFinal("test_go_to_main_page_on_the_logo", bank['url'] == main_page.get_url(), "URL is correct")

    @pytest.mark.run(order=1)
    def test_display_home_chat(self, main_page, mark_status):
        main_page.open_page()
        main_page.header_click_home_chat_link()
        mark_status.markFinal("test_display_home_chat", main_page.display_home_chat() is True, "Home-chat is displayed")

    @pytest.mark.run(order=1)
    def test_close_home_chat(self, main_page, mark_status):
        main_page.open_page()
        main_page.header_click_home_chat_link()
        main_page.header_click_close_home_chat()
        mark_status.markFinal("test_close_home_chat",
                              main_page.display_home_chat() is False, "Home-chat is closed")

    @pytest.mark.run(order=1)
    def test_element_login_popup(self, main_page, mark_status):
        main_page.open_page()
        main_page.header_click_login_link()
        mark_status.mark(main_page.login_page.validate_text_credit_link("Мой кредит"), "Is correct")
        mark_status.mark(main_page.login_page.validate_text_goods_link("Товары в рассрочку"), "Is correct")
        mark_status.mark(main_page.login_page.validate_text_polza_link("Польза"), "Is correct")
        mark_status.mark(main_page.login_page.validate_text_internet_bank_link("Интернет-банк"), "Is correct")
        mark_status.markFinal("test_element_login_popup",main_page.login_page.validate_text_title("Вход"),"Elements login popup is correct")