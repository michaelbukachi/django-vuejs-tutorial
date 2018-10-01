import socket
from contextlib import closing


def test_text_is_show(driver):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex(('localhost', 8000)) == 0:
            driver.get('http://localhost:8000')
            assert 'This is just a demo.' in driver.page_source
