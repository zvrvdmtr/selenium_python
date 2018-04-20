from testrail_api.testrail import *
from pprint import pprint


def add_run(case_id=None):
    """
    Ручка для создания нового тест рана
    Входящий параметр: project_id
    Data: suite_id, name
    """
    run = None
    if case_id is not None:
        client = APIClient('https://testrail.homecred.it')
        client.user = 'dmitriy.zverev@homecredit.ru'
        client.password = 'Qwerty_22'
        run = client.send_post('add_run/5', {'suite_id': '59', 'name': 'новый ран', 'include_all': False,
                                             'case_ids': case_id})
    return run


def get_run():
    """
    Ручка для получения информации о ране
    Выходящий параметр: run_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    run = client.send_get('get_run/28')
    pprint(run)


def get_runs():
    """
    Ручка для получения информации о всех ранах входящих в проект
    Входящий параметр: project_id
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    run = client.send_get('get_runs/5')
    pprint(run)


def update_run():
    """
    Ручка для обновления данных тест рана
    Входящий параметр: run_id
    Data: name
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    run = client.send_post('update_run/21', {'name': 'update_test_run'})
    pprint(run)


def close_run():
    """
    Ручка для закрытия тест рана
    Входящий параметр: run_id
    Data: пусто
    На текущий момент закрытый ран удалить нельзя!!!
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    run = client.send_post('close_run/21', {})
    pprint(run)


def delete_run():
    """
    Ручка для удаления тест рана
    Входящий параметр: run_id
    Data: пусто
    """
    client = APIClient('https://testrail.homecred.it')
    client.user = 'dmitriy.zverev@homecredit.ru'
    client.password = 'Qwerty_22'
    run = client.send_post('delete_run/22', {})
    pprint(run)
