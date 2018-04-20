from pages.homecred.market.search.search_field import SearchField
from utilities.markstatus import MarkStatus
import pytest
import time


class TestSearch:

#@pytest.mark.usefixtures('each_function_setup')
#class TestSearch(unittest.TestCase):

    @pytest.fixture()
    def search(self, each_function_setup, setup_path):
        return SearchField(each_function_setup, setup_path)

    @pytest.fixture()
    def mark_status(self, each_function_setup):
        return MarkStatus(each_function_setup)


   # @pytest.fixture(autouse=True)
   # def class_setup(self, each_function_setup, setup_path):
    #    self.search = SearchField(self.driver, setup_path)
    #    self.MarkStatus = MarkStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_find_product(self, search, mark_status):
        search.search_string(text='HP 80 Magenta (C4874A)')
        time.sleep(1)
        search.visible_find_area()
        search.click_on_product()
        result = search.check_name_of_product()
        print(result)
        mark_status.markFinal('HP 80 Magenta (C4874A)', result == 'HP 80 Magenta (C4874A)', 'verify title on page')
