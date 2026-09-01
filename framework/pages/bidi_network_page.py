from framework.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

class BidiNetworkPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/blank.html"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def capture_navigation_request(self, timeout=5):
        requests = []
        handler_id = self.driver.network.add_request_handler(
            [self.URL],
            requests.append
        )
        try:
            self.open()
            WebDriverWait(self.driver, timeout).until(
                lambda _: requests
        )
            return requests[0]
        finally:
            self.driver.network.remove_request_handler(handler_id)

