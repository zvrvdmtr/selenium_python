from testrail_api.testrail import *
from pprint import pprint


def get_test(test_id=''):
    """
    Ручка для получения информации о тест (из тест-рана)
    Выходящий параметр: test_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    test = client.send_get('get_test/%s' % test_id)
    return test


def get_tests(run_id):
    """
    Ручка для получения информации о тест (из тест-рана)
    Выходящий параметр: test_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    tests = client.send_get('get_tests/%s' % run_id)
    return tests

