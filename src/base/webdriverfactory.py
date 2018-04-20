"""
Класс для создания инстанса webdriver
Конструктур принимает параметры: browser (тип браузера), headless (режим работы без UI)
Так же класс устанвливает неявное ожидание
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import logging
import utilities.custom_logger as cl
from configfiles.project_setting import *


class WebDriverFactory(object):

    log = cl.customLogger(logging.INFO)

    def __init__(self, browser, headless):
        self.browser = browser
        self.headless = headless

    def get_webdriver_instance(self):
        """
        Func which set webdriver preferences
        by url and type of project from fixtures
        :return: webdriver instance
        """

        if self.browser == 'chrome':
            if self.headless == 'true':
                chrome_option = ChromeOptions()
                chrome_option.add_argument('--headless')
                driver_destination = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'chromedriver')
                driver = webdriver.Chrome(executable_path=driver_destination,
                                          chrome_options=chrome_option)
                self.log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
            else:
                driver_destination = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'chromedriver')
                driver = webdriver.Chrome(executable_path=driver_destination)
                self.log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
                # driver.set_window_size(1440, 900)
        elif self.browser == 'firefox':
            if self.headless == 'true':
                firefox_options = FirefoxOptions()
                firefox_options.set_headless()
                driver_destination = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'geckodriver')
                driver = webdriver.Firefox(firefox_options=firefox_options, executable_path=driver_destination)
                driver.maximize_window()
                self.log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
            else:
                driver_destination = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'geckodriver')
                driver = webdriver.Firefox(executable_path=driver_destination)
                driver.maximize_window()
                self.log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
        elif self.browser == 'remote_firefox':
                driver = webdriver.Remote(command_executor='http://' + '1' + ':4444/wd/hub',
                                          desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True, })
                self.log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
        elif self.browser == 'remote_chrome':
                driver = webdriver.Remote(command_executor='http://' + '2' + ':4444/wd/hub',
                                          desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True, })
                self.log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
        elif self.browser == 'ie':
            driver = webdriver.Ie()
            self.log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
        elif self.browser == 'edge':
            driver = webdriver.Edge()
            self.log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
        elif self.browser == 'safari':
            driver = webdriver.Safari()
            self.log.info('Driver is set as for browser "%s". Headless is %s' % (self.browser, self.headless))
        else:
            driver = None
            self.log.error('Driver "%s" is not defined' % self.browser)

        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        return driver
