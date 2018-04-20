"""
Файл содержищий фикстуры типа setup и teardown для запуска тестов
Реализует флаги командной строки: browser, headless, project
"""
import pytest
from base.webdriverfactory import WebDriverFactory
import csv
import os


@pytest.fixture(scope='function')
def each_function_setup(request, browser, headless):
    """
    Setting up options to webdriver
    :param request: service attribute
    :param browser: from pytest_addoption
    :param headless: from pytest_addoption
    :return: webdriver instance
    """
    wdf = WebDriverFactory(browser, headless)
    driver = wdf.get_webdriver_instance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def one_time_setup(request, browser, headless):
    """
    Setting up options to webdriver
    :param request: service attribute
    :param browser: from pytest_addoption
    :param headless: from pytest_addoption
    :return: webdriver instance
    """
    wdf = WebDriverFactory(browser,headless)
    driver = wdf.get_webdriver_instance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def setup_path(project, test_data):
    """
    Setting up project URL
    :param project: from pytest_addoption
    :return: project URL
    """
    url = project
    if project == 'market':
        url = test_data[0]['url']
    elif project == 'bank':
        url = test_data[0]['url']
    elif project == 'intranet':
        url = test_data[0]['url']
    return url


def pytest_addoption(parser):
    """
    Setup flags for project
    :param parser:
    :return:
    """
    parser.addoption("--browser")
    parser.addoption("--headless")
    parser.addoption("--project")


@pytest.fixture(scope="session")
def browser(request):
    """
    Setup browser type flag
    :param request:
    :return: flag browser value
    """
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def headless(request):
    """
    Setup headless flag
    :param request:
    :return: flag headless value
    """
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def project(request):
    """
    Setup project flag
    :param request:
    :return: flag project value
    """
    return request.config.getoption("--project")


@pytest.fixture()
def test_data(project):
    """
    Parsing csv file with project settings
    :param project: from pytest_addoption
    :return: list with values from csv file
    """
    path = None
    csv_list = []
    if project == 'market':
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/market_test_data.csv')
    elif project == 'bank':
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/bank_test_data.csv')
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_list.append(row)
    return csv_list

