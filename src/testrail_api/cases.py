from testrail_api.testrail import *
from pprint import pprint


def add_case():
    """
    Ручка для создания нового кейса и добавления его в сьют.
    Входящий параметр: suite_id
    Data: title
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('add_case/89', {'title': 'First_by_API'})
    pprint(case)


def get_case():
    """
    Ручка для получения информации о кейсе.
    Входящий параметр: case_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_case/1120')
    pprint(case)


def get_cases():
    """
    Ручка для получения информации о кейсах в проекте и сьюте.
    Входящий параметр: project_id, suite_id
    Опциональный параметр: section_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_cases/5/&suite_id=49')
    pprint(case)


def update_case():
    """
    Ручка для изменения существующего кейса.
    Входящий параметр: suite_id
    Data: title
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('update_case/1079', {'title': 'Update_first_by_API'})
    pprint(case)


def delete_case():
    """
    Ручка для удаления существующего кейса.
    Входящий параметр: case_id
    Data: пусто
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('delete_case/1082', '')
    pprint(case)


def get_project():
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_project/5')
    pprint(case)
