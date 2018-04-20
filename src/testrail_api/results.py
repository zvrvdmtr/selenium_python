from testrail_api.testrail import *
from pprint import pprint


def get_results():
    """
    Ручка для получения информации о результатх прогона кейсов.
    Входящий параметр: test_id (из тест рана)
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_results/1357')
    pprint(case)


def get_results_for_case():
    """
    Ручка для получения информации о кейсе.
    Входящий параметр: run_id/case_id (из тест сьюта)
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_results_for_case/23/1101')
    pprint(case)


def get_results_for_run():
    """
    Ручка для получения информации о кейсе.
    Входящий параметр: run_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_results_for_run/23')
    pprint(case)


def add_result(test_id, status_id, result):
    """
    Ручка для создания нового кейса и добавления его в сьют.
    Входящий параметр: test_id (из тест рана)
    Data: status_id, comment, custom_step_results (позволяет переименовывать в рамках теста шаги (видимо это плохо))
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post("add_result/%s" % test_id, {'status_id': status_id, 'comment': 'All good',
                                                        'custom_step_results': result})


def add_results_for_case():
    """
    Ручка для создания нового кейса и добавления его в сьют.
    Входящий параметр: run_id/case_id (из тест сьюта)
    Data: title
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('add_result_for_case/23/1101', {'status_id': '5', 'comment': 'All good'})
    pprint(case)


def add_results():
    """
    Ручка для создания нового кейса и добавления его в сьют.
    Входящий параметр: run_id
    Data: test_id (из тест рана), status_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('add_results/26', {'results': [{'test_id': '1385', 'status_id': '1',
                                                            'custom_step_results':
                                                                [{'content': 'First example content',
                                                                  'expected': 'First example expected',
                                                                  'actual': 'First example expected',
                                                                  'status_id': '1'},
                                                                 {'content': 'Second example content',
                                                                  'expected': 'Second example expected',
                                                                  'actual': 'Second example expected',
                                                                  'status_id': '1'},
                                                                 {'content': 'Third example content',
                                                                  'expected': 'Third example expected',
                                                                  'actual': 'Third example expected',
                                                                  'status_id': '1'}]},
                                                           {'test_id': '1386', 'status_id': '1',
                                                            'custom_step_results':
                                                                [{'content': 'First example content',
                                                                  'expected': 'First example expected',
                                                                  'actual': 'First example expected',
                                                                  'status_id': '1'},
                                                                 {'content': 'Second example content',
                                                                  'expected': 'Second example expected',
                                                                  'actual': 'Second example expected',
                                                                  'status_id': '1'},
                                                                 {'content': 'Third example content',
                                                                  'expected': 'Third example expected',
                                                                  'actual': 'Third example expected',
                                                                  'status_id': '1'}]}

                                                           ]})
    pprint(case)


def add_results_for_cases():
    """
    Ручка для создания нового кейса и добавления его в сьют.
    Входящий параметр: run_id
    Data: case_id (из сьюта), status_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('add_results_for_cases/23', {'results': [{'case_id': '1101', 'status_id': '1'}]})
    pprint(case)
