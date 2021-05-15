import os

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def path():
    return os.getenv('CHROME_DRIVER_PATH', '')


@pytest.fixture(scope='session')
def driver(path):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver_ = webdriver.Chrome(path, chrome_options=chrome_options)
    yield driver_
    driver_.quit()