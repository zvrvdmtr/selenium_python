"""
Класс реализующий проверку тестов
"""
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
from testrail_api.tests import get_test
from testrail_api.results import add_result
from testrail_api.tests import get_tests
import inspect


class MarkStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(MarkStatus, self).__init__(driver)
        self.resultList = {}
        self.result_count = 0
        self.result_steps = None
        self.run_id = 0
        self.test_id = None

    def get_step(self, case_id=None, new_run=None):
        """
        Setting up run, steps, cases on TestRail
        :param case_id: case_id from TestRail
        :param new_run: run_id from TestRail (generate run_id on test class)
        :return:
        """
        if new_run is not None:
            run_id = get_tests(new_run['id'])
            for i in run_id:
                if i['case_id'] == case_id:
                    self.test_id = i['id']
        if self.test_id is not None:
            self.result_steps = get_test(test_id=self.test_id)['custom_steps_separated']
            self.run_id = get_test(test_id=self.test_id)['run_id']

    def setResult(self, result, resultMessage):
        """
        Setting up status of test assertions
        :param result: see function mark
        :param resultMessage: see function markFinal
        :return:
        """
        try:
            if result is not None:
                if result:
                    self.resultList[resultMessage] = 'PASS'
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                    if self.result_steps is not None:
                        self.result_steps[self.result_count]['actual'] = 'PASS'
                        self.result_steps[self.result_count]['status_id'] = 1
                else:
                    self.resultList[resultMessage] = 'FAIL'
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    if self.result_steps is not None:
                        self.result_steps[self.result_count]['actual'] = 'FAIL'
                        self.result_steps[self.result_count]['status_id'] = 5
                    self.take_screen(resultMessage, inspect.stack()[2][3], self.run_id)
            else:
                self.resultList[resultMessage] = 'FAIL'
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                if self.result_steps is not None:
                    self.result_steps[self.result_count]['actual'] = 'FAIL'
                    self.result_steps[self.result_count]['status_id'] = 5
                self.take_screen(resultMessage, inspect.stack()[2][3], self.run_id)
            self.result_count += 1
        except:
            self.resultList[resultMessage] = 'FAIL'
            self.log.error("### Exception Occurred !!!")
            if self.result_steps is not None:
                self.result_steps[self.result_count]['actual'] = 'BLOCKED'
                self.result_steps[self.result_count]['status_id'] = 2
            self.take_screen(resultMessage, inspect.stack()[2][3], self.run_id)

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        :param result: bool from tests class
        :param resultMessage: str from tests class. Comment to verification step
        :return:
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This should be final test status of the test case
        :param testName: str from tests class. Comment to verification test
        :param result: bool from tests class
        :param resultMessage: str from tests class. Comment to verification step
        :return:
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList.values():
            self.log.error(testName + " ### TEST FAILED")
            if self.result_steps is not None:
                add_result(test_id=self.test_id, status_id='5', result=self.result_steps)
            self.resultList.clear()
            self.log.info('-' * 80)
            assert True is False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            if self.result_steps is not None:
                add_result(test_id=self.test_id, status_id='1', result=self.result_steps)
            self.resultList.clear()
            self.log.info('-'*80)
            assert True is True