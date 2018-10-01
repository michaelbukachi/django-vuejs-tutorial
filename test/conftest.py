import os
import platform

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='session')
def path():
    if platform.system() == 'Linux':
        return 'bin/phantomjs-linux'
    elif platform.system() == 'Darwin':
        return 'bin/phantomjs-mac'
    elif platform.system() == 'Windows':
        return 'bin/phantomjs.exe'


@pytest.fixture(scope='session')
def driver(path):
    if os.getenv('CI_TEST', None):
        options = Options()
        options.add_argument('--headless')
        driver_ = webdriver.Firefox(firefox_options=options)
    else:
        driver_ = webdriver.PhantomJS(path)
    yield driver_
    driver_.quit()