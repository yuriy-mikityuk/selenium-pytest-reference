from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class RequestCollector:
    def __init__(self, driver: WebDriver, url_patterns, timeout=5):
        self.timeout = timeout
        self.handler_id = None
        self.requests = []
        self.url_patterns = url_patterns
        self.driver = driver

    def __enter__(self):
        self.requests = []
        self.handler_id = self.driver.network.add_request_handler(
            self.url_patterns,
            self.requests.append,
        )
        return self

    def __exit__(self, *args):
        self.driver.network.remove_request_handler(self.handler_id)
        return False

    def wait_for(self,count=1, timeout=None):
        if timeout is None:
            timeout = self.timeout
        WebDriverWait(self.driver, timeout=timeout).until(
            lambda _: len(self.requests) >= count
        )

    def __getitem__(self, index):
        return self.requests[index]
