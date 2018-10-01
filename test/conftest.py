import os
import platform

import pytest
from selenium import webdriver


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
        driver_ = webdriver.PhantomJS()
    else:
        driver_ = webdriver.PhantomJS(path)
    yield driver_
    driver_.quit()