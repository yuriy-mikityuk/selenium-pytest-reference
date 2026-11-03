import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 5


class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def __str__(self):
        by, value = self.locator
        return f"{type(self).__name__}({by}={value})"

    def _wait(self, condition, state, timeout):
        # The one path to the element: every method below goes through here
        failure = f"{self} is not {state} after {timeout}s"
        try:
            element = WebDriverWait(self.driver, timeout).until(condition(self.locator), message=failure)
        except TimeoutException:
            logger.error(failure)
            raise
        logger.debug("%s is %s", self, state)
        return element

    def _log_action(self, action):
        logger.info("%s %s", self, action)

    def _log_result(self, action, result):
        logger.info("%s %s -> %r", self, action, result)
        return result

    def wait_until_present(self, timeout=DEFAULT_TIMEOUT):
        return self._wait(EC.presence_of_element_located, "present", timeout)

    def wait_until_displayed(self, timeout=DEFAULT_TIMEOUT):
        return self._wait(EC.visibility_of_element_located, "displayed", timeout)

    def wait_until_clickable(self, timeout=DEFAULT_TIMEOUT):
        return self._wait(EC.element_to_be_clickable, "clickable", timeout)

    def click(self):
        element = self.wait_until_clickable()
        self._log_action("click")
        element.click()

    def get_text(self):
        return self._log_result("get_text", self.wait_until_displayed().text)

    def scroll_into_view(self):
        element = self.wait_until_displayed()
        self._log_action("scroll_into_view")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def take_screenshot(self, file_path: str) -> bool:
        return self._log_result(f"take_screenshot({file_path!r})", self.wait_until_displayed().screenshot(file_path))

    def get_screenshot_as_png(self) -> bytes:
        png = self.wait_until_displayed().screenshot_as_png
        logger.info("%s get_screenshot_as_png -> %d bytes", self, len(png))
        return png

    # State readers wait for presence only. Waiting for visibility or clickability
    # here would turn a valid False (hidden, disabled) into a TimeoutException.

    def is_displayed(self):
        return self._log_result("is_displayed", self.wait_until_present().is_displayed())

    def is_enabled(self):
        return self._log_result("is_enabled", self.wait_until_present().is_enabled())

    def is_selected(self):
        return self._log_result("is_selected", self.wait_until_present().is_selected())

    def get_property(self, property_name):
        return self._log_result(f"get_property({property_name!r})", self.wait_until_present().get_property(property_name))

    def get_attribute(self, attribute_name):
        return self._log_result(f"get_attribute({attribute_name!r})", self.wait_until_present().get_attribute(attribute_name))
