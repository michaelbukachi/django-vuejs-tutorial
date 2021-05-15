import os

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def path():
    return os.getenv('CHROME_DRIVER_PATH', '')


@pytest.fixture(scope='session')
def driver(path):
    driver_ = webdriver.Chrome(path)
    yield driver_
    driver_.quit()