from testrail_api.testrail import *
from pprint import pprint


def add_section():
    """
    Ручка для создания новой секции и добавления ее в проект.
    Входящий параметр: project_id
    Data: suite_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('add_section/5', {'name': 'First_section', 'suite_id': '59'})
    pprint(case)

add_section()


def get_section():
    """
    Ручка для получения информации о секции.
    Входящий параметр: section_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_section/188')
    pprint(case)


def get_sections():
    """
    Ручка для получения информации о секциях в проекте.
    Входящий параметр: project_id, suite_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_get('get_sections/5&suite_id=53')
    pprint(case)


def update_section():
    """
    Ручка для изменения существующей секции.
    Входящий параметр: section_id
    Data: name
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('update_section/188', {'name': 'First_section_update'})
    pprint(case)


def delete_section():
    """
    Ручка для удаления существующей секции.
    Входящий параметр: suite_id
    Data: пусто
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    case = client.send_post('delete_section/189', '')
    pprint(case)
