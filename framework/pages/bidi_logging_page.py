from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from framework.elements.base_element import BaseElement
from selenium.webdriver.support.ui import WebDriverWait

class BidiLoggingPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html"
    _CONSOLE_LOG_BUTTON = (By.ID, "consoleLog")
    _JS_EXCEPTION_BUTTON = (By.ID, "jsException")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.console_log_button = BaseElement(self.driver, self._CONSOLE_LOG_BUTTON)
        self.js_exception_button = BaseElement(self.driver, self._JS_EXCEPTION_BUTTON)

    def capture_console_log(self, timeout=5):
        log_entries = []
        handler_id = self.driver.script.add_console_message_handler(
            log_entries.append
        )
        try:
            self.console_log_button.click()

            WebDriverWait(self.driver, timeout).until(
                lambda _: log_entries
            )

            return log_entries[0]
        finally:
            self.driver.script.remove_console_message_handler(handler_id)

    def capture_javascript_error(self, timeout=5):
        log_entries = []
        handler_id = self.driver.script.add_javascript_error_handler(
            log_entries.append)
        try:
            self.js_exception_button.click()

            WebDriverWait(self.driver, timeout).until(
                lambda _: log_entries
            )

            return log_entries[0]
        finally:
            self.driver.script.remove_javascript_error_handler(handler_id)
