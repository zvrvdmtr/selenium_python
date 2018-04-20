from testrail_api.testrail import *
from pprint import pprint


def add_suite():
    """
    Ручка для создания нового сьюта и добавления его в проект.
    Входящий параметр: project_id
    Data: name
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('add_suite/5', {'name': 'Example_suite'})
    pprint(case)

add_suite()


def get_suite():
    """
    Ручка для получения информации о сьюта.
    Входящий параметр: suite_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_suite/51')
    pprint(case)


def get_suites():
    """
    Ручка для получения информации о сьютах в проекте.
    Входящий параметр: project_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_suites/5')
    pprint(case)


def update_suite():
    """
    Ручка для изменения существующего сьюта.
    Входящий параметр: suite_id
    Data: name
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('update_suite/51', {'name': 'Update_first_by_API'})
    pprint(case)


def delete_suite():
    """
    Ручка для удаления существующего сьюта.
    Входящий параметр: suite_id
    Data: пусто
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('delete_suite/54', '')
    pprint(case)


