import socket
from contextlib import closing


def test_text_is_show(driver):
    driver.get('http://localhost:8000')
    assert 'This is just a demo.' in driver.page_source
